# Jira Health Report — SERVER (Core Server)
**Instance:** https://jira.mongodb.org
**Date:** 2026-05-21
**Total open issues:** 13,497
**Stale threshold:** 90 days

---

## Summary

| # | Category | Count | Severity |
|---|----------|-------|----------|
| 1 | High priority (Blocker-P1/Critical-P2), no action 90+ days | 18 | 🟡 Warning |
| 2 | Unassigned in-flight issues | 377 | 🔴 Critical |
| 3 | Orphaned issues — no epic (54% of open issues) | 7,300 | 🟡 Warning |
| 4 | Ghosts in dead epics | 0 | ✅ OK |
| 5 | Stale In Progress / In Code Review / Needs Merge (90+ days) | 44 | 🟡 Warning |
| 6 | Status inconsistencies (Resolved with open blockers) | 42 | 🟡 Warning |
| 7 | Blocker resolved, task still blocked | — | ⚪ Requires ScriptRunner (not available unauthenticated) |
| 8 | Sprint overflow (active issues in closed sprints) | 1,553 | 🔴 Critical |
| 9 | Zombie To Do (Open/Backlog untouched 90+ days) | 9,316 | 🔴 Critical |
| 10 | Reopened issues (status changed to Open in last 90 days) | 419 | 🟡 Warning |
| 11 | Done parent, open children | 0 | ✅ OK |
| 12 | Missing story points in active sprints | N/A | ⚪ Field not accessible unauthenticated |
| 13 | Fix version mismatch (released version, not Done) | 27 | 🟡 Warning |
| 14 | Heavily discussed, never resolved (≥10 comments, sample) | 6 (sample) | 🟡 Warning |
| 15 | Discussed and parked (Blocked/Waiting, stale 90+ days) | 297 | 🔴 Critical |
| 16 | Other anomalies (no description, no comments) | 144 | 🟡 Warning |

---

## Top 3 Priorities

1. **Zombie To Do backlog (9,316 issues = 69% of open issues)** — Nearly 70% of all open SERVER issues are in Open or Backlog and untouched for 90+ days. Many are assigned to deprecated "[DO NOT USE] Backlog" team queues. A bulk-triage or archival campaign is urgently needed.
2. **Sprint overflow (1,553 issues)** — Over 1,500 issues in closed sprints remain unresolved and were carried forward without resolution. This signals chronic over-commitment or missing sprint closure hygiene.
3. **Unassigned in-flight issues (377)** — 377 issues are in active work states (Blocked, In Code Review, Needs Verification) with no assignee. These are orphaned work items that cannot progress.

---

## 1. High Priority, No Action — 18 issues

Blocker-P1 or Critical-P2 issues not updated in 90+ days. Several date back years with no active owner.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-113876 | IDL fuzz test generation | Michael Merrill | Blocker - P1 | Needs Verification | 2025-11-13 |
| SERVER-111587 | Histogram CE: Deadlock in getHistogram | Unassigned | Blocker - P1 | Backlog | 2026-01-22 |
| SERVER-52256 | Enable feature flag for Limit plan cache memory | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-51953 | Create feature flag for Limit plan cache memory | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-111234 | Safer feature flag wrappers/helpers for query | Unassigned | Critical - P2 | Backlog | 2025-10-06 |
| SERVER-110957 | Investigate fields to move between OpDebug | Joe Shalabi | Critical - P2 | Investigating | 2025-10-13 |
| SERVER-107286 | Investigate memory pressure when hitting limits | Unassigned | Critical - P2 | Backlog | 2025-07-09 |
| SERVER-106353 | Move debug split step into install macros | Unassigned | Critical - P2 | Backlog | 2026-02-17 |
| SERVER-105042 | Upgrade to gcc-15 | Unassigned | Critical - P2 | Open | 2026-01-16 |
| SERVER-104873 | Prevent copts & linkopts modifications without Build team | Unassigned | Critical - P2 | Backlog | 2025-09-29 |
| SERVER-87046 | Re-enable fle2/txn_sharded.js with replication | Unassigned | Critical - P2 | Backlog | 2025-10-23 |
| SERVER-86863 | r7.0.6 included partially backported feature | MongoDB Server Releases | Critical - P2 | Needs Scheduling | 2024-02-21 |
| SERVER-82648 | Improve locking in LogicalTimeValidator | [DO NOT USE] Backlog | Critical - P2 | Open | 2024-08-07 |
| SERVER-27762 | View without collation inherits collection collation | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-18375 | High CPU during insert-only stress (heap contention) | DO NOT USE - Backlog | Critical - P2 | Open | 2020-04-09 |
| SERVER-13552 | Remove unnecessary global lock during replace action | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-9925 | Index covered binary prefix search | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-6439 | Duplicate fields at same level should not be allowed | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2026-02-17 |

*18 total — see `01_high_priority_stale.csv`.*

---

## 2. Unassigned In-Flight Issues — 377 issues

Issues in active states (Blocked, Needs Verification, In Code Review, etc.) with no assignee.

| Key | Summary | Priority | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| SERVER-127126 | Re-run existing $lookup-$unwind performance tests | Major - P3 | Blocked | 2026-05-21 |
| SERVER-127030 | Use getLatestMetrics in PDIB testing library | Major - P3 | Blocked | 2026-05-18 |
| SERVER-126812 | Block new .js test additions under jstests/sharding/ | Major - P3 | Blocked | 2026-05-21 |
| SERVER-126329 | Expose the most recent optime per collection | Major - P3 | Needs Verification | 2026-05-08 |
| SERVER-126244 | Remove multiversion_incompatible tag from collmod | Major - P3 | Blocked | 2026-05-07 |
| SERVER-125892 | Add HostUnreachable to retryable errors | Major - P3 | Blocked | 2026-05-11 |
| SERVER-124504 | Re-enable compression in join optimization testing | Major - P3 | Blocked | 2026-04-20 |
| SERVER-124457 | Simplify CqPipeline lifetime | Major - P3 | Blocked | 2026-04-17 |
| SERVER-124386 | Tighten legacy timeseries collection creation check | Major - P3 | Blocked | 2026-04-17 |
| SERVER-124073 | Use page sampling to estimate avg num recs/chunk | Major - P3 | Blocked | 2026-04-20 |
| SERVER-124038 | Update vendored libmongocrypt to 1.18.0 | Major - P3 | Blocked | 2026-04-23 |
| SERVER-123783 | Remove Feature Flag for SPM-4594 | Major - P3 | Blocked | 2026-04-17 |
| SERVER-123634 | Check TODO comment after BACKPORT-25702 | Major - P3 | Blocked | 2026-05-08 |
| SERVER-123393 | Complete TODO listed in SERVER-80719 | Major - P3 | Blocked | 2026-04-16 |
| SERVER-123055 | Add replication commands to antithesis config | Major - P3 | Blocked | 2026-04-03 |

*377 total — see `02_unassigned.csv`.*

---

## 3. Orphaned Issues — No Epic — 7,300 issues (54%)

54% of open issues have no Epic Link. Project uses Epics for some work (KIP-style tracking) but not systematically across all teams. The CSV contains the highest-severity P1/P2 orphaned issues.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-127351 | Add OTel Metrics for reshard background operations | Unassigned | Critical - P2 | Needs Scheduling | 2026-05-21 |
| SERVER-111587 | Histogram CE: Deadlock in getHistogram | Unassigned | Blocker - P1 | Backlog | 2026-01-22 |
| SERVER-52256 | Enable feature flag for Limit plan cache memory | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-51953 | Create feature flag for Limit plan cache memory | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-86863 | r7.0.6 included partially backported feature | MongoDB Server Releases | Critical - P2 | Needs Scheduling | 2024-02-21 |
| SERVER-27762 | View without collation inherits collection collation | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-18375 | High CPU during insert-only stress test | DO NOT USE - Backlog | Critical - P2 | Open | 2020-04-09 |
| SERVER-9925 | Index covered binary prefix search | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |

*7,300 total; CSV contains P1/P2 sample — see `03_no_epic.csv`.*

---

## 4. Ghosts in Dead Epics — 0 issues

No closed/resolved epics with open child issues found. ✅

---

## 5. Stale In Progress / In Code Review / Needs Merge — 44 issues

Issues in active coding states with no update for 90+ days. Several In Code Review items indicate PRs that have been submitted but not yet reviewed.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-117950 | Complete TODO listed in SERVER-92801 | Zack Winter | Major - P3 | In Progress | 2026-02-10 |
| SERVER-117947 | Complete TODO listed in SERVER-85819 | Zack Winter | Major - P3 | In Progress | 2026-02-10 |
| SERVER-116042 | Add WASM module build with Bazel | Lee Maguire | Major - P3 | In Progress | 2026-02-12 |
| SERVER-114624 | Fix incorrect use of TaskExecutor::scheduleRemoteCommand | Henri Nikku | Major - P3 | In Code Review | 2026-01-14 |
| SERVER-114051 | Deactivate SBOM Test Release task upload | Eduard Kovalets | Minor - P4 | In Code Review | 2025-11-18 |
| SERVER-110940 | Test multiplanner with CBR fallback combinations | Timour Katchaounov | Major - P3 | In Progress | 2026-01-26 |
| SERVER-110459 | Audit perf workloads for memory-tracked stages | Chris Wolff | Major - P3 | In Progress | 2025-09-26 |
| SERVER-110439 | Unify spilling metrics in serverStatus | Projjal Chanda | Major - P3 | In Code Review | 2025-12-01 |
| SERVER-110311 | Move memory tracking from DocumentSourceGroup | Romans Kasperovics | Major - P3 | In Code Review | 2025-09-16 |
| SERVER-109795 | Reduce boilerplate in QO->QE stage mapping | Romans Kasperovics | Major - P3 | In Code Review | 2025-10-30 |
| SERVER-109039 | Coverity defect 149655: Dereference before null check | Unassigned | Major - P3 | In Progress | 2025-11-17 |
| SERVER-107902 | Add 10gen/query as codeowner for jstests/libs | Catalin Sumanaru | Major - P3 | In Code Review | 2025-12-10 |
| SERVER-105088 | [v8.0] Improve FCV downgrade error message | Anna Maria Nestorov | Major - P3 | Needs Merge | 2025-08-25 |
| SERVER-103010 | Add resolved collation to query stats entries | Sam Mercier | Major - P3 | In Progress | 2026-01-06 |
| SERVER-102424 | Add DAO layer in resharding coordinator | Unassigned | Major - P3 | In Progress | 2026-01-13 |

*44 total — see `05_stale_inprogress.csv`.*

---

## 6. Status Inconsistencies — 42 issues

Resolved/Closed issues that still have unresolved blocking relationships (open issues linked as "blocks"). These upstream items are marked done but their dependents may be silently stalled.

*42 total — see `06_status_inconsistencies.csv`.*

---

## 7. Blocker Resolved, Task Still Blocked — N/A

Dedicated link traversal requires ScriptRunner JQL not available unauthenticated. The check in category 6 covers the inverse direction. Manual review recommended.

---

## 8. Sprint Overflow — 1,553 issues

Active issues found in closed sprints. This is a persistent and large problem indicating sprints are closed without resolving or explicitly deferring their contents.

| Key | Summary | Assignee | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| SERVER-127353 | Add ReshardingRecipientPostCloningDeltaCollector | Wenqin Ye | In Progress | 2026-05-21 |
| SERVER-127341 | Add waitForOplogVisibilityToAdvancePast primitive | Ernesto Rodriguez Reina | In Progress | 2026-05-21 |
| SERVER-127328 | Split large change stream test files | Unassigned | Needs Scheduling | 2026-05-21 |
| SERVER-127235 | Add timeout to CSM wait commands in coordinator | Wenqin Ye | In Progress | 2026-05-20 |
| SERVER-127234 | Integrate CSM waiting commands into coordinator | Wenqin Ye | In Progress | 2026-05-20 |
| SERVER-127233 | Introduce stub command to wait for CSM on recipient | Wenqin Ye | In Progress | 2026-05-20 |
| SERVER-126965 | Wrap _topology in synchronised_value | Daniel Khuu | Open | 2026-05-19 |
| SERVER-126816 | [v7.0] Add no_selinux tag to command_let_variables.js | Erwin Pe | Blocked | 2026-05-19 |
| SERVER-126781 | [v7.0] Upgrade passlib package in v7.0 | Erwin Pe | Blocked | 2026-05-19 |
| SERVER-126463 | Collection cloner with function_ref has memory bug | Vishnu Kaushik | In Code Review | 2026-05-20 |

*1,553 total — see `08_sprint_overflow.csv` for sample.*

---

## 9. Zombie To Do — 9,316 issues

Issues in Open, Backlog, Needs Triage, or Ready for Work status — created 90+ days ago and not updated in 90+ days. At **69% of all open issues**, this represents the most severe health problem in the project.

Notable pattern: many are assigned to "[DO NOT USE] Backlog - *" team queues, confirming these are abandoned items from retired or restructured teams.

*9,316 total (200 sampled in CSV) — see `09_zombie_todo.csv`.*

---

## 10. Reopened Issues — 419 issues

Issues whose status was changed back to Open within the last 90 days.

| Key | Summary | Assignee | Priority | Last Updated |
|-----|---------|----------|----------|--------------|
| SERVER-127325 | Complete TODO listed in SERVER-108852 | Kruti Shah | Major - P3 | 2026-05-21 |
| SERVER-127303 | failedHostPreHandshake is unused in streamable RSM | Joseph Prince | Major - P3 | 2026-05-20 |
| SERVER-127287 | [M2 - Search Extension] Sharded Execution | Unassigned | Major - P3 | 2026-05-20 |
| SERVER-127286 | Modify create_document_results_and_metadata() host service | Josh Siegel | Major - P3 | 2026-05-20 |
| SERVER-127270 | Test writeConflicts do not lead to duplicate logic | Stephanie Eristoff | Major - P3 | 2026-05-20 |
| SERVER-127267 | Add Server support for SLES 16 | Daniel Moody | Minor - P4 | 2026-05-20 |
| SERVER-127266 | Add Server Support for Debian 13 | Daniel Moody | Minor - P4 | 2026-05-20 |
| SERVER-127214 | Prevent conflicts during authoritative commits | Unassigned | Major - P3 | 2026-05-20 |
| SERVER-127213 | Prepare _configSvrCommitChunkMigrationCommand | Unassigned | Major - P3 | 2026-05-20 |
| SERVER-127162 | Complete TODO listed in SERVER-110187 | Tommaso Tocci | Major - P3 | 2026-05-21 |

*419 total — see `10_reopened.csv`.*

---

## 11. Done Parent, Open Children — 0 issues

No resolved parent issues with open subtasks found. ✅

---

## 12. Missing Story Points — N/A

The `story_points` field is not accessible to unauthenticated users. Skipped.

---

## 13. Fix Version Mismatch — 27 issues

Issues assigned to a released fix version that are still not Done/Resolved. RC version assignments (8.3.0-rc0, 9.0.0-rc0) suggest items that were planned for the release but not completed before it shipped.

| Key | Summary | Assignee | Status | Fix Version | Last Updated |
|-----|---------|----------|--------|-------------|--------------|
| SERVER-121546 | [v7.0] Remove unnecessary timeseries write path invariants | Matt Kneiser | Needs Merge | 7.0.32 | 2026-05-11 |
| SERVER-121342 | Add documentation for split horizon | Didier Nadeau | In Code Review | 8.3.0-rc0 | 2026-03-11 |
| SERVER-121284 | Update AGENTS.md with coding workflows | Mathias Stearn | In Code Review | 8.3.0-rc0 | 2026-03-10 |
| SERVER-120952 | Simplify and clean up the CMS manager API | Nic Hollingum | In Code Review | 8.3.0-rc0 | 2026-03-06 |
| SERVER-120745 | Fix test format for searchCoordinator fsync | Fiona Chang | Needs Verification | 8.3.0-rc0 | 2026-03-03 |
| SERVER-120681 | Reduce hot/cold BF thresholds for C&I | Ryan Chipman | In Code Review | 8.3.0-rc0 | 2026-04-28 |
| SERVER-120620 | Miscellaneous small fixes from core module visibility | Unassigned | Open | 8.3.0-rc0, 9.0.0-rc0 | 2026-05-05 |
| SERVER-120533 | Grant permission for search to run fsync | Fiona Chang | Needs Verification | 8.3.0-rc0 | 2026-03-02 |
| SERVER-120240 | Fix sharding passthrough suites | Yujin Kang Park | Needs Merge | 8.3.0-rc0 | 2026-03-05 |
| SERVER-120227 | Make CMSChannelManager and SLSConfigManager testable | Nic Hollingum | In Code Review | 8.3.0-rc0 | 2026-02-26 |

*27 total — see `13_fix_version_mismatch.csv`.*

---

## 14. Heavily Discussed, Never Resolved — 6 issues (500-issue sample)

Open issues with 10+ visible comments that remain unresolved. Note: MongoDB Jira restricts some comment visibility to authenticated users, so actual counts may be higher.

| Key | Summary | Comments | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| SERVER-110427 | Update Profile Data Files | 170 | Backlog | 2026-05-21 |
| SERVER-58026 | Omitted FTDC sections cause frequent schema changes | 22 | Backlog | 2026-05-14 |
| SERVER-83322 | Compound Wildcard Index bounds reverts to [MinKey, MaxKey] | 12 | Open | 2026-05-15 |
| SERVER-26665 | Clean up WTRecordStore handling of non-oplog capped collections | 11 | Backlog | 2026-05-18 |
| SERVER-121912 | Upgrade tcmalloc to include rseq bug fix | 10 | Open | 2026-05-20 |
| SERVER-35035 | Additional levels of command debugging | 10 | Backlog | 2026-05-13 |

*500-issue sample — see `14_heavily_discussed.csv`.*

---

## 15. Discussed and Parked — 297 issues

Issues in Blocked or "Waiting For User Input" status with no update for 90+ days. The majority are unassigned Blocked issues — effectively invisible in any team queue.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-118856 | Circular dependency prevents active query checking | Unassigned | Major - P3 | Blocked | 2026-02-09 |
| SERVER-118855 | Add throughputProbing parameters to fuzz config | Unassigned | Major - P3 | Blocked | 2026-02-12 |
| SERVER-118764 | Set severity to MisplacedCollection and CollectionUUID | Unassigned | Major - P3 | Blocked | 2026-02-03 |
| SERVER-117945 | Append error reporting to removeShard response | Unassigned | Major - P3 | Blocked | 2026-02-09 |
| SERVER-117486 | Shard overwrites bulk write response payload | Unassigned | Major - P3 | Blocked | 2026-02-06 |
| SERVER-117054 | Remove timeseries $-prefix upgrade test once 9.0 stable | Unassigned | Major - P3 | Blocked | 2026-01-15 |
| SERVER-116387 | Align server backpressure handling with driver spec | Unassigned | Major - P3 | Blocked | 2026-01-12 |
| SERVER-116151 | Delete the NsTargeter class hierarchy | Unassigned | Major - P3 | Blocked | 2026-01-16 |
| SERVER-115755 | Remove Feature Flag for SPM-3391 | Unassigned | Major - P3 | Blocked | 2026-02-12 |
| SERVER-115725 | Make ShardRegistry notify RSM of new nodes | Unassigned | Major - P3 | Blocked | 2026-01-19 |

*297 total — see `15_discussed_and_parked.csv`.*

---

## 16. Other Anomalies — 144 issues

Open issues with no description AND no comments. Many are very recent tickets that appear to be work-in-progress placeholders created without context.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-127353 | Add ReshardingRecipientPostCloningDeltaCollector | Wenqin Ye | Major - P3 | In Progress | 2026-05-21 |
| SERVER-127347 | Increase defaultFindReplicaSetHostTimeoutMS on mongos | Nicholas Jefferies | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127344 | Document and rename container::ExistingKeyPolicy values | Parker Felix | Major - P3 | Backlog | 2026-05-21 |
| SERVER-127343 | Revisit applyOps handling of container writes | Parker Felix | Major - P3 | Backlog | 2026-05-21 |
| SERVER-127339 | Check lastSpilledRecordId for resume decision | Gregory Noma | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127338 | Use lastSpilledRecordId when determining resume point | Gregory Noma | Major - P3 | Needs Merge | 2026-05-21 |
| SERVER-127336 | Add optional UUID field to config.shards schema | Paolo Polato | Major - P3 | In Progress | 2026-05-21 |
| SERVER-127332 | Extract query_knobs into a dedicated module | Catalin Sumanaru | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127303 | failedHostPreHandshake is unused in streamable RSM | Joseph Prince | Major - P3 | Open | 2026-05-20 |
| SERVER-127301 | Step-up after rotation testing for push mode | Unassigned | Major - P3 | Needs Scheduling | 2026-05-20 |

*144 total — see `16_other_anomalies.csv`.*
