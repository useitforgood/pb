## System Purpose

The system is a macOS command-line script that scans a user-defined set of filesystem paths, identifies files that exceed a configurable size threshold and have not been opened within a configurable number of days, identifies directories that contain more than a configurable number of direct child files and have not been opened within the same period, and writes a structured Markdown report listing both categories sorted by staleness descending. The system never modifies, moves, or deletes any file or directory. The report is written to a timestamped file in the user's home directory and a summary is printed to stdout on completion.

---

## Input Specification

| **Field** | **Type** | **Required** | **Source** | **Validation Rules** |
|-----------|----------|--------------|------------|----------------------|
| scan_roots | list[string] | yes | computed | Default: ["/Users/[current_username]"]; each path must exist and be a directory; current_username derived from `os.getlogin()` |
| excluded_path_prefixes | list[string] | yes | configuration file | Default list defined in System Constraints; each entry is an absolute path prefix |
| file_size_threshold_mb | integer | yes | configuration file | Default: 100; must be ≥ 1 |
| stale_threshold_days | integer | yes | configuration file | Default: 180; must be ≥ 1 |
| folder_file_count_threshold | integer | yes | configuration file | Default: 100; must be ≥ 1 |
| top_large_files | integer | yes | configuration file | Default: 100; must be ≥ 1 |
| top_dense_folders | integer | yes | configuration file | Default: 50; must be ≥ 1 |
| output_path | string | yes | computed | Default: "[HOME]/disk_cleanup_report_[YYYYMMDD_HHMMSS].md"; parent directory must be writable |
| cli_arg_root | list[string] | no | user-provided | Overrides scan_roots if provided; each path validated as above |
| cli_arg_size_mb | integer | no | user-provided | Overrides file_size_threshold_mb if provided |
| cli_arg_stale_days | integer | no | user-provided | Overrides stale_threshold_days if provided |
| cli_arg_folder_files | integer | no | user-provided | Overrides folder_file_count_threshold if provided |
| cli_arg_output | string | no | user-provided | Overrides output_path if provided |

---

## Processing Logic

**On startup:**

1. Parse CLI arguments: `--root PATH` (repeatable), `--size-mb N`, `--stale-days N`, `--folder-files N`, `--output PATH`.
2. Load configuration defaults for any argument not supplied via CLI.
3. IF `cli_arg_root` is non-empty: set `scan_roots` = `cli_arg_root`.
   ELSE: set `scan_roots` = ["/Users/[os.getlogin()]"].
4. IF `cli_arg_size_mb` is provided: set `file_size_threshold_mb` = `cli_arg_size_mb`.
   ELSE: retain default.
5. IF `cli_arg_stale_days` is provided: set `stale_threshold_days` = `cli_arg_stale_days`.
   ELSE: retain default.
6. IF `cli_arg_folder_files` is provided: set `folder_file_count_threshold` = `cli_arg_folder_files`.
   ELSE: retain default.
7. IF `cli_arg_output` is provided: set `output_path` = `cli_arg_output`.
   ELSE: set `output_path` = "[HOME]/disk_cleanup_report_[YYYYMMDD_HHMMSS].md" where timestamp is current UTC time.
8. Validate each path in `scan_roots`. IF any path does not exist or is not a directory: print error to stderr and remove it from `scan_roots`.
9. IF `scan_roots` is empty after validation: print "No valid scan roots. Exiting." to stderr; exit with code 1.
   ELSE: continue to step 10.
10. Set `stale_cutoff` = current UTC datetime minus `stale_threshold_days` days.
11. Set `file_size_threshold_bytes` = `file_size_threshold_mb` × 1048576.
12. Initialize `large_files` = empty list; `dense_folders` = empty list.

**Filesystem scan (repeated for each path in `scan_roots`):**

13. Begin recursive directory walk of `scan_root` using `os.walk` with `followlinks=False`.
14. At each directory `dirpath` encountered during the walk:
    a. IF `dirpath` is prefixed by any entry in `excluded_path_prefixes`: skip `dirpath` and all its descendants; continue to next directory.
       ELSE: continue.
    b. IF `dirpath` ends with any of the bundle extensions `.app`, `.framework`, `.plugin`, `.kext`, `.bundle`:
       - Compute `bundle_size` = sum of `os.stat(f).st_size` for all files under `dirpath` recursively (errors ignored per step 32).
       - Query `last_opened` for `dirpath` via `mdls` (step 26).
       - IF `bundle_size` ≥ `file_size_threshold_bytes`: append `{path: dirpath, size: bundle_size, last_opened: last_opened, type: "bundle"}` to `large_files`.
         ELSE: do not append.
       - Do not descend into `dirpath`; remove all its entries from `os.walk` dirnames in-place.
       ELSE: continue to step 15.
15. Collect `direct_child_files` = list of all non-directory, non-symlink entries in `dirpath`.
16. FOR each file `filepath` in `direct_child_files`:
    a. Retrieve `file_size` = `os.stat(filepath).st_size`. IF `OSError` is raised: skip this file; continue.
       ELSE: continue.
    b. IF `file_size` < `file_size_threshold_bytes`: skip this file; continue.
       ELSE: continue.
    c. Query `last_opened` for `filepath` via `mdls` (step 26).
    d. Append `{path: filepath, size: file_size, last_opened: last_opened, type: "file"}` to `large_files`.
17. Compute `direct_file_count` = count of `direct_child_files`.
18. IF `direct_file_count` ≥ `folder_file_count_threshold`:
       - Query `last_opened` for `dirpath` via `mdls` (step 26).
       - Compute `folder_size` = sum of `os.stat(f).st_size` for all files in `direct_child_files` (errors ignored per step 32).
       - Append `{path: dirpath, file_count: direct_file_count, folder_size: folder_size, last_opened: last_opened}` to `dense_folders`.
    ELSE: do not append.

**mdls query procedure (referenced as step 26):**

19. Invoke subprocess: `mdls -name kMDItemLastUsedDate -raw [target_path]`.
20. IF subprocess exits with non-zero code or output is "(null)" or output is empty: set `last_opened` = None.
    ELSE: parse output as datetime string in format "%Y-%m-%d %H:%M:%S +0000"; set `last_opened` = parsed UTC datetime.

**Report generation:**

21. Filter `large_files`: retain entries where `last_opened` is None or `last_opened` < `stale_cutoff`. Store as `stale_large_files`.
22. Sort `stale_large_files` by `last_opened` ascending, with None values first (oldest or never-opened first).
23. Truncate `stale_large_files` to `top_large_files` entries.
24. Filter `dense_folders`: retain entries where `last_opened` is None or `last_opened` < `stale_cutoff`. Store as `stale_dense_folders`.
25. Sort `stale_dense_folders` by `last_opened` ascending, with None values first.
26. Truncate `stale_dense_folders` to `top_dense_folders` entries.
27. Compute `total_large_file_size` = sum of `size` for all entries in `stale_large_files`.
28. Build Markdown report string (see Output Specification and Data Processing sections).
29. Write report string to `output_path`. IF write fails: print error to stderr; exit with code 1.
    ELSE: continue.
30. Print summary to stdout: "Scan complete. Found [count(`stale_large_files`)] large stale files ([total_large_file_size] GB) and [count(`stale_dense_folders`)] dense stale folders. Report written to [output_path]."

**Error handling for individual files (step 32 reference):**

31. IF `OSError` or `PermissionError` is raised for any individual file or directory during stat or mdls query: skip that entry; log a warning line to stderr in format "WARN: skipped [path]: [error message]"; continue.
    ELSE: continue normally.

---

## Data Processing

### File Size Formatting

Input data: integer byte count.
Transformation rule: IF bytes ≥ 1073741824: format as "[n] GB" rounded to two decimal places. ELSE IF bytes ≥ 1048576: format as "[n] MB" rounded to one decimal place. ELSE: format as "[n] KB" rounded to one decimal place.
Output data: human-readable size string.

### Last Opened Formatting

Input data: `last_opened` datetime or None.
Transformation rule: IF `last_opened` is None: output string "Never". ELSE: compute `days_since` = (current UTC datetime − `last_opened`).days; output string "[YYYY-MM-DD] ([days_since] days ago)".
Output data: formatted last-opened string and integer `days_since` (or 999999 when None, for sorting purposes).

### Markdown Report Assembly

Input data: `stale_large_files` list, `stale_dense_folders` list, all configuration values, scan start and end timestamps.

Transformation rule: assemble the following sections in order:

```
# Disk Cleanup Report
Generated: [ISO 8601 timestamp]
Scan roots: [comma-separated scan_roots]
Thresholds: files ≥ [file_size_threshold_mb] MB, not opened in [stale_threshold_days]+ days;
            folders with [folder_file_count_threshold]+ direct files, not opened in [stale_threshold_days]+ days

---

## Large Stale Files ([count] found, showing top [top_large_files])
Total size: [total_large_file_size formatted]

| Path | Size | Last Opened |
|------|------|-------------|
| [path] | [formatted size] | [formatted last opened] |
... (one row per entry, sorted stalest first)

---

## Dense Stale Folders ([count] found, showing top [top_dense_folders])

| Path | Direct Files | Folder Size | Last Opened |
|------|-------------|-------------|-------------|
| [path] | [file_count] | [formatted folder_size] | [formatted last opened] |
... (one row per entry, sorted stalest first)

---

## How to act on this report
- Review each listed path manually before taking any action.
- To delete a file: move it to Trash via Finder or `trash [path]` (requires the `trash` CLI tool).
- To delete a folder: move it to Trash via Finder or `trash [path]`.
- This report does not delete anything.
```

Output data: complete Markdown report string written to `output_path`.

---

## Output Specification

| **Field** | **Type** | **Always present** | **Description** |
|-----------|----------|--------------------|-----------------|
| report_file | Markdown file | yes | Full report containing large stale files and dense stale folders tables |
| stdout_summary | string | yes | One-line scan summary printed to stdout on completion |
| stderr_warnings | string | no | One line per skipped path, printed to stderr during scan |

Delivery method: `report_file` written to `output_path` on the local filesystem; `stdout_summary` printed to stdout; `stderr_warnings` printed to stderr as encountered.

---

## Error Handling

| **Error condition** | **Source** | **System behavior** | **Response to caller** |
|--------------------|------------|--------------------|-----------------------|
| `scan_roots` is empty after validation | Startup | Exit with code 1 | stderr: "No valid scan roots. Exiting." |
| Scan root path does not exist or is not a directory | Startup | Remove from scan_roots; continue with remaining roots | stderr: "WARN: scan root [path] is not a valid directory. Skipping." |
| `PermissionError` on directory during walk | Filesystem scan | Skip directory and all descendants; continue | stderr: "WARN: skipped [path]: [error message]" |
| `OSError` on `os.stat` for a file | Filesystem scan | Skip that file; continue | stderr: "WARN: skipped [path]: [error message]" |
| `mdls` subprocess exits with non-zero code | mdls query | Set `last_opened` = None; continue | No output to user; treated as "Never opened" |
| `mdls` output is "(null)" or empty | mdls query | Set `last_opened` = None; continue | No output to user; treated as "Never opened" |
| `mdls` output cannot be parsed as datetime | mdls query | Set `last_opened` = None; continue | stderr: "WARN: could not parse last-opened date for [path]" |
| Output file cannot be written | Report generation | Exit with code 1 | stderr: "ERROR: could not write report to [output_path]: [error message]" |
| CLI argument is not a valid integer where integer is required | Startup | Exit with code 1 | stderr: "ERROR: invalid value for [argument]: [value]" |

---

## System Constraints

- The system never deletes, moves, renames, or modifies any file or directory.
- The system never follows symbolic links during the filesystem walk.
- Excluded path prefixes (default, applied before any descent):
  - `/System`
  - `/Library` (root-level; `~/Library` is not excluded)
  - `/usr`
  - `/bin`
  - `/sbin`
  - `/private`
  - `/cores`
  - `/dev`
  - `/net`
  - `/Volumes/com.apple.TimeMachine.localsnapshots`
- The system requires macOS with Spotlight indexing enabled; `mdls` must be available on the system PATH.
- The system requires Python 3.8 or later.
- The system does not require any third-party Python packages; it uses only the Python standard library and the macOS `mdls` subprocess.

---

## Completion Criteria

1. When the script is run with no arguments, it scans `/Users/[current_username]` and writes a report to a timestamped file in the home directory.
2. When `--root` is provided with a valid path, the script scans that path instead of the default.
3. When a path in `scan_roots` does not exist, the script prints a warning to stderr, excludes that path, and continues with the remaining roots.
4. Every file ≥ `file_size_threshold_mb` MB whose `last_opened` is None or predates `stale_cutoff` appears in the Large Stale Files table.
5. No file whose `last_opened` is within the last `stale_threshold_days` days appears in the Large Stale Files table.
6. Every directory with ≥ `folder_file_count_threshold` direct child files whose `last_opened` is None or predates `stale_cutoff` appears in the Dense Stale Folders table.
7. Both tables are sorted with None (never-opened) entries first, followed by entries in ascending order of `last_opened` date.
8. No path prefixed by an excluded path prefix appears in either table.
9. No path under a `.app`, `.framework`, `.plugin`, `.kext`, or `.bundle` directory appears as an individual file entry; the bundle root appears as a single entry.
10. The script does not modify, delete, or move any file or directory under any condition.
11. When the report file cannot be written, the script exits with code 1 and prints an error to stderr.
12. When all files and directories are accessible and `mdls` is available, the script exits with code 0.
