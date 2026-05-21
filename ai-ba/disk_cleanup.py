#!/usr/bin/env python3
"""Disk cleanup report — macOS only. Read-only: never deletes anything."""

from __future__ import annotations

import argparse
import os
import stat
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

EXCLUDED_PREFIXES = (
    "/System",
    "/Library",
    "/usr",
    "/bin",
    "/sbin",
    "/private",
    "/cores",
    "/dev",
    "/net",
    "/Volumes/com.apple.TimeMachine.localsnapshots",
)

BUNDLE_EXTENSIONS = frozenset({".app", ".framework", ".plugin", ".kext", ".bundle"})

DEFAULT_FILE_SIZE_MB = 100
DEFAULT_STALE_DAYS = 180
DEFAULT_FOLDER_FILES = 100
DEFAULT_TOP_LARGE = 100
DEFAULT_TOP_DENSE = 50


def _excluded(path: str) -> bool:
    return any(path == p or path.startswith(p + "/") for p in EXCLUDED_PREFIXES)


def _last_opened(path: str) -> datetime | None:
    try:
        r = subprocess.run(
            ["mdls", "-name", "kMDItemLastUsedDate", "-raw", path],
            capture_output=True, text=True, timeout=10,
        )
        raw = r.stdout.strip()
        if r.returncode != 0 or not raw or raw == "(null)":
            return None
        return datetime.strptime(raw, "%Y-%m-%d %H:%M:%S +0000").replace(tzinfo=timezone.utc)
    except Exception as e:
        print(f"WARN: could not parse last-opened date for {path}: {e}", file=sys.stderr)
        return None


def _dir_total_size(path: str) -> int:
    total = 0
    for dp, _, fnames in os.walk(path, followlinks=False):
        for fn in fnames:
            try:
                total += os.stat(os.path.join(dp, fn)).st_size
            except OSError:
                pass
    return total


def _fmt_size(n: int) -> str:
    if n >= 1_073_741_824:
        return f"{n / 1_073_741_824:.2f} GB"
    if n >= 1_048_576:
        return f"{n / 1_048_576:.1f} MB"
    return f"{n / 1024:.1f} KB"


def _fmt_lo(lo: datetime | None, now: datetime) -> str:
    if lo is None:
        return "Never"
    return f"{lo.strftime('%Y-%m-%d')} ({(now - lo).days} days ago)"


def _sort_key(e: dict) -> tuple:
    lo = e["last_opened"]
    return (1, lo) if lo is not None else (0, datetime.min.replace(tzinfo=timezone.utc))


def scan(
    roots: list[str],
    size_threshold: int,
    folder_threshold: int,
) -> tuple[list[dict], list[dict]]:
    large: list[dict] = []
    dense: list[dict] = []

    for root in roots:
        for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
            if _excluded(dirpath):
                dirnames.clear()
                continue

            if Path(dirpath).suffix in BUNDLE_EXTENSIONS:
                bsize = _dir_total_size(dirpath)
                lo = _last_opened(dirpath)
                if bsize >= size_threshold:
                    large.append({"path": dirpath, "size": bsize, "last_opened": lo, "type": "bundle"})
                dirnames.clear()
                continue

            dirnames[:] = [d for d in dirnames if not _excluded(os.path.join(dirpath, d))]

            child_files: list[tuple[str, int]] = []
            for fname in filenames:
                fpath = os.path.join(dirpath, fname)
                try:
                    st = os.lstat(fpath)
                except OSError as e:
                    print(f"WARN: skipped {fpath}: {e}", file=sys.stderr)
                    continue
                if stat.S_ISLNK(st.st_mode):
                    continue
                child_files.append((fpath, st.st_size))

            for fpath, fsize in child_files:
                if fsize < size_threshold:
                    continue
                lo = _last_opened(fpath)
                large.append({"path": fpath, "size": fsize, "last_opened": lo, "type": "file"})

            if len(child_files) >= folder_threshold:
                lo = _last_opened(dirpath)
                dense.append({
                    "path": dirpath,
                    "file_count": len(child_files),
                    "folder_size": sum(s for _, s in child_files),
                    "last_opened": lo,
                })

    return large, dense


def build_report(
    stale_large: list[dict],
    stale_dense: list[dict],
    roots: list[str],
    size_mb: int,
    stale_days: int,
    folder_files: int,
    top_large: int,
    top_dense: int,
    now: datetime,
) -> str:
    total = sum(e["size"] for e in stale_large)
    lines = [
        "# Disk Cleanup Report",
        f"Generated: {now.strftime('%Y-%m-%dT%H:%M:%SZ')}",
        f"Scan roots: {', '.join(roots)}",
        f"Thresholds: files ≥ {size_mb} MB, not opened in {stale_days}+ days;",
        f"            folders with {folder_files}+ direct files, not opened in {stale_days}+ days",
        "",
        "---",
        "",
        f"## Large Stale Files ({len(stale_large)} found, showing top {top_large})",
        f"Total size: {_fmt_size(total)}",
        "",
        "| Path | Size | Last Opened |",
        "|------|------|-------------|",
    ]
    for e in stale_large:
        lines.append(f"| {e['path']} | {_fmt_size(e['size'])} | {_fmt_lo(e['last_opened'], now)} |")

    lines += [
        "",
        "---",
        "",
        f"## Dense Stale Folders ({len(stale_dense)} found, showing top {top_dense})",
        "",
        "| Path | Direct Files | Folder Size | Last Opened |",
        "|------|-------------|-------------|-------------|",
    ]
    for e in stale_dense:
        lines.append(
            f"| {e['path']} | {e['file_count']} | {_fmt_size(e['folder_size'])} | {_fmt_lo(e['last_opened'], now)} |"
        )

    lines += [
        "",
        "---",
        "",
        "## How to act on this report",
        "- Review each listed path manually before taking any action.",
        "- To delete a file: move it to Trash via Finder or `trash [path]` (requires the `trash` CLI tool).",
        "- To delete a folder: move it to Trash via Finder or `trash [path]`.",
        "- This report does not delete anything.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="Generate a disk cleanup report (macOS, read-only).")
    ap.add_argument("--root", dest="roots", action="append", metavar="PATH",
                    help="Directory to scan (repeatable; default: home directory)")
    ap.add_argument("--size-mb", type=int, default=DEFAULT_FILE_SIZE_MB, metavar="N",
                    help=f"Flag files larger than N MB (default: {DEFAULT_FILE_SIZE_MB})")
    ap.add_argument("--stale-days", type=int, default=DEFAULT_STALE_DAYS, metavar="N",
                    help=f"Flag items not opened in N+ days (default: {DEFAULT_STALE_DAYS})")
    ap.add_argument("--folder-files", type=int, default=DEFAULT_FOLDER_FILES, metavar="N",
                    help=f"Flag folders with N+ direct child files (default: {DEFAULT_FOLDER_FILES})")
    ap.add_argument("--top-large", type=int, default=DEFAULT_TOP_LARGE, metavar="N",
                    help=f"Max large files in report (default: {DEFAULT_TOP_LARGE})")
    ap.add_argument("--top-dense", type=int, default=DEFAULT_TOP_DENSE, metavar="N",
                    help=f"Max dense folders in report (default: {DEFAULT_TOP_DENSE})")
    ap.add_argument("--output", default=None, metavar="PATH",
                    help="Report output path (default: ~/disk_cleanup_report_TIMESTAMP.md)")
    args = ap.parse_args()

    for flag, val in [
        ("--size-mb", args.size_mb),
        ("--stale-days", args.stale_days),
        ("--folder-files", args.folder_files),
        ("--top-large", args.top_large),
        ("--top-dense", args.top_dense),
    ]:
        if val < 1:
            print(f"ERROR: invalid value for {flag}: {val}", file=sys.stderr)
            sys.exit(1)

    raw_roots = args.roots or [os.path.expanduser("~")]
    valid_roots: list[str] = []
    for r in raw_roots:
        if os.path.isdir(r):
            valid_roots.append(r)
        else:
            print(f"WARN: scan root {r} is not a valid directory. Skipping.", file=sys.stderr)
    if not valid_roots:
        print("No valid scan roots. Exiting.", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc)
    output_path = args.output or os.path.join(
        os.path.expanduser("~"), f"disk_cleanup_report_{now.strftime('%Y%m%d_%H%M%S')}.md"
    )
    stale_cutoff = now - timedelta(days=args.stale_days)
    size_threshold = args.size_mb * 1_048_576

    print(f"Scanning {', '.join(valid_roots)} …", flush=True)
    large, dense = scan(valid_roots, size_threshold, args.folder_files)

    stale_large = sorted(
        [e for e in large if e["last_opened"] is None or e["last_opened"] < stale_cutoff],
        key=_sort_key,
    )[:args.top_large]

    stale_dense = sorted(
        [e for e in dense if e["last_opened"] is None or e["last_opened"] < stale_cutoff],
        key=_sort_key,
    )[:args.top_dense]

    report = build_report(
        stale_large, stale_dense,
        valid_roots, args.size_mb, args.stale_days, args.folder_files,
        args.top_large, args.top_dense, now,
    )

    try:
        Path(output_path).write_text(report, encoding="utf-8")
    except OSError as e:
        print(f"ERROR: could not write report to {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

    total_size = sum(e["size"] for e in stale_large)
    print(
        f"Scan complete. Found {len(stale_large)} large stale files ({_fmt_size(total_size)}) "
        f"and {len(stale_dense)} dense stale folders. Report written to {output_path}."
    )


if __name__ == "__main__":
    main()
