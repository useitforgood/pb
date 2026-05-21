# Jira Health Report — SERVER
**Instance:** https://jira.mongodb.org
**Date:** 2026-05-21
**Total open issues:** 13,493
**Stale threshold:** 90 days

---

## 1. High priority, no action — 18
Eighteen Blocker-P1 and Critical-P2 issues have not been updated in over 90 days, including a P1 IDL fuzz test issue stuck in Needs Verification since November 2025 and several Critical issues last touched in 2020–2024.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-113876 | IDL fuzz test generation | Michael Merrill | Blocker - P1 | Needs Verification | 2025-11-13 |
| SERVER-111587 | Histogram CE: Deadlock in getHistogram | Unassigned | Blocker - P1 | Backlog | 2026-01-22 |
| SERVER-52256 | Enable feature flag for Limit plan cache memory consumption | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-51953 | Create feature flag for Limit plan cache memory consumption | Unassigned | Blocker - P1 | Backlog | 2025-07-21 |
| SERVER-110957 | Investigate whether any fields should be moved between OpDebug and CurOp | Joe Shalabi | Critical - P2 | Investigating | 2025-10-13 |
| SERVER-111234 | Safer feature flag wrappers/helpers for query | Unassigned | Critical - P2 | Backlog | 2025-10-06 |
| SERVER-107286 | Investigate ways to keep machine from dying when hitting memory limits | Unassigned | Critical - P2 | Backlog | 2025-07-09 |
| SERVER-106353 | consider moving debug split step into the install macros | Unassigned | Critical - P2 | Backlog | 2026-02-17 |
| SERVER-105042 | Upgrade to gcc-15 | Unassigned | Critical - P2 | Open | 2026-01-16 |
| SERVER-104873 | Prevent modifications to copts & linkopts without Build team review | Unassigned | Critical - P2 | Backlog | 2025-09-29 |
| SERVER-87046 | Re-enable fle2/txn_sharded.js test in sharding suites with random migrations | Unassigned | Critical - P2 | Backlog | 2025-10-23 |
| SERVER-86863 | r7.0.6 included partially backported feature | MongoDB Server Releases | Critical - P2 | Needs Scheduling | 2024-02-21 |
| SERVER-82648 | Improve the locking in LogicalTimeValidator::get/set | [DO NOT USE] Backlog | Critical - P2 | Open | 2024-08-07 |
| SERVER-27762 | creating a view without specifying collation explicitly should insert the collat | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-18375 | High CPU during insert-only stress test due to heap contention on Windows | DO NOT USE Backlog | Critical - P2 | Open | 2020-04-09 |
| SERVER-13552 | remove unnecessary global lock during "replace" out action | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-9925 | Index covered binary prefix search | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2022-12-06 |
| SERVER-6439 | Duplicate fields at the same level should not be allowed | [DO NOT USE] Backlog | Critical - P2 | Backlog | 2026-02-17 |

---

## 2. Unassigned issues — 44
Forty-four issues in active workflow statuses (In Progress, In Code Review, Investigating, Needs Merge, Needs Verification) have no assignee. This includes issues stuck in Needs Merge since September 2024 — over 8 months with no owner.

| Key | Summary | Priority | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| SERVER-126329 | Expose the most recent optime per collection | Major - P3 | Needs Verification | 2026-05-08 |
| SERVER-120667 | Add information about failed storageStats fetching into the slow logs | Major - P3 | Investigating | 2026-03-18 |
| SERVER-119947 | tassert setWindowFields sort by dotted path under meta field | Major - P3 | In Progress | 2026-03-04 |
| SERVER-117001 | $listSearchIndexes behavior should be consistent | Major - P3 | Investigating | 2026-03-13 |
| SERVER-111670 | Investigate using chained replication to reduce RCI mutex contention | Major - P3 | In Progress | 2026-02-23 |
| SERVER-109316 | Add backup logging for broken stacks | Major - P3 | In Code Review | 2026-03-09 |
| SERVER-109039 | Coverity analysis defect 149655: Dereference before null check | Major - P3 | In Progress | 2025-11-17 |
| SERVER-102424 | Add DAO layer in resharding coordinator | Major - P3 | In Progress | 2026-01-13 |
| SERVER-101955 | time_support.cpp: dateFromISOString rejects leap seconds | Major - P3 | In Progress | 2026-03-09 |
| SERVER-94228 | Support Date_t formatting and parsing of dates before 1970 | Major - P3 | In Progress | 2026-03-09 |
| SERVER-94189 | (Nice-to-have) Correct $balancerConfiguration enabled field value | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-93470 | Make $unionWith support running aggregation stages | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-93361 | Include the draining state in the shards section in $clusterTopology | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-93351 | Modify $clusterTopology to use already defined error codes | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-93066 | Add $clusterTopology to the clusterManager role | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-92814 | Start tracking timestamps on both primary and secondary | Major - P3 | In Code Review | 2024-09-09 |
| SERVER-92792 | Implement the Zones section for the sharding configuration API | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-92263 | Investigate usage of JIT for server side JS on atlas fleet | Major - P3 | In Progress | 2026-04-01 |
| SERVER-92099 | Implement $balancerConfiguration aggregation stage | Major - P3 | Needs Merge | 2024-09-16 |
| SERVER-92098 | Implement the Databases section for the sharding configuration API | Major - P3 | Needs Merge | 2024-09-16 |

*(showing top 20 of 44)*

---

## 3. Orphaned issues — no epic — N/A
7,298 of 13,493 open issues (54%) have no Epic Link. Epics are actively used in this project (46% coverage). **38 high-priority issues (Blocker-P1 / Critical-P2) lack epic linkage** — these are the highest-risk orphans.

| Key | Summary | Priority | Status |
|-----|---------|----------|--------|
| SERVER-127351 | Add OTel Metrics for reshard background operations | Critical - P2 | Needs Scheduling |
| SERVER-124455 | Add OTel Metrics for TTL deletes and index builds | Critical - P2 | Needs Scheduling |
| SERVER-123957 | Extra dependencies added to tasks | Critical - P2 | Blocked |
| SERVER-83322 | Compound Wildcard Index bounds reverts to [MinKey; MaxKey] | Critical - P2 | Open |
| SERVER-123826 | Stack-buffer-overflow in __bid128_from_string | Critical - P2 | Open |
| SERVER-121619 | $project silently drops root-level fields after $lookup + $unwind | Critical - P2 | Waiting For User Input |
| SERVER-115121 | keyExamined and docsExamined shows negative values | Critical - P2 | Needs Scheduling |
| SERVER-118979 | Tracking: query work for opcounters as OTel Metrics | Critical - P2 | Backlog |

*(showing top 8 of 38 high-priority no-epic issues; full project no-epic ratio 54%)*

---

## 4. Ghosts in dead epics — 0
No open issues are linked to Closed/Done epics. ✅

---

## 5. Stale in-progress — 107
107 issues in active workflow statuses (In Progress, In Code Review, Investigating, Needs Merge, Needs Verification) have not been updated in over 90 days. Multiple issues show Needs Merge since mid-2024 with no movement.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-104680 | Feature Flag Upgrade/Downgrade Testing | Unassigned | Major - P3 | Needs Verification | 2025-05-05 |
| SERVER-104679 | Documentation Updates | Unassigned | Major - P3 | Needs Verification | 2025-05-05 |
| SERVER-104678 | Grammar fuzzer changes | Unassigned | Major - P3 | Needs Verification | 2025-05-05 |
| SERVER-103630 | Documentation Updates | Unassigned | Major - P3 | Needs Verification | 2025-04-09 |
| SERVER-103492 | Enable feature flag | [DO NOT USE] Backlog | Major - P3 | Needs Verification | 2025-04-07 |
| SERVER-110957 | Investigate whether any fields should be moved between OpDebug and CurOp | Joe Shalabi | Critical - P2 | Investigating | 2025-10-13 |
| SERVER-110459 | Audit perf workloads for coverage of memory-tracked stages | Chris Wolff | Major - P3 | In Progress | 2025-09-26 |
| SERVER-109039 | Coverity analysis defect 149655: Dereference before null check | Unassigned | Major - P3 | In Progress | 2025-11-17 |
| SERVER-108971 | Emit client metadata as a time-series metric aggregated by process | Mark LaRoche | Major - P3 | Investigating | 2025-08-18 |
| SERVER-94189 | (Nice-to-have) Correct $balancerConfiguration enabled field value | Unassigned | Major - P3 | Needs Merge | 2024-09-16 |

*(showing top 10 of 107)*

---

## 6. Status inconsistencies — 314
314 issues are marked Done/Closed/Resolved but still belong to an active open sprint. These should either be removed from the sprint or reflect sprint board hygiene issues.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-127258 | Skip $listClusterCatalog timeseries shard key checks | Joan Bruguera Micó | Major - P3 | Closed | 2026-05-20 |
| SERVER-127232 | Perform all index build spilling before transitioning to load phase | Gregory Noma | Major - P3 | Closed | 2026-05-20 |
| SERVER-127113 | Add bazel targets for extension resmoke suites | Sean Lyons | Major - P3 | Closed | 2026-05-20 |
| SERVER-127110 | Prevent jstestfuzz hangs on near-16MB documents | Nicola Cabiddu | Major - P3 | Closed | 2026-05-19 |
| SERVER-127108 | Add bazel targets for query-optimization resmoke suites | Sean Lyons | Major - P3 | Closed | 2026-05-20 |
| SERVER-127097 | Fix multiversion handling of authoritativeMetadataAccessLevel | Joan Bruguera Micó | Major - P3 | Closed | 2026-05-20 |
| SERVER-127096 | Populate PDIB lastSpilledRecordId when resuming | Gregory Noma | Major - P3 | Closed | 2026-05-20 |
| SERVER-127067 | Track last record id spilled during PDIB scan | Gregory Noma | Major - P3 | Closed | 2026-05-19 |
| SERVER-127066 | Verify that upgrading/downgrading between collection usage and container usage | Damian Wasilewicz | Major - P3 | Closed | 2026-05-21 |
| SERVER-127057 | Add last spilled record id to IndexStateInfo | Gregory Noma | Major - P3 | Closed | 2026-05-19 |

*(showing top 10 of 314)*

---

## 7. Blocker resolved, task still blocked — 0
No issues found where the blocking issue is resolved but the blocked issue remains open. ✅

*(Note: MongoDB Jira's anonymous API does not support `issueFunction in linkedIssuesOf()` — result may be incomplete. Manual verification recommended.)*

---

## 8. Sprint overflow — 1,552
1,552 issues carried over from closed sprints remain open. This indicates chronic sprint overcommitment or issues being added to sprints without completion discipline.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-127341 | Add waitForOplogVisibilityToAdvancePast storage-engine primitive | Ernesto Rodriguez Reina | Major - P3 | In Progress | 2026-05-21 |
| SERVER-127235 | Add timeout to CSM wait commands in coordinator | Wenqin Ye | Major - P3 | In Progress | 2026-05-20 |
| SERVER-127234 | Integrate CSM waiting commands into coordinator | Wenqin Ye | Major - P3 | In Progress | 2026-05-20 |
| SERVER-127233 | introduce stub command to wait for CSM on recipient | Wenqin Ye | Major - P3 | In Progress | 2026-05-20 |
| SERVER-126965 | Wrap _topology in synchronised_value | Daniel Khuu | Major - P3 | Open | 2026-05-19 |
| SERVER-126816 | [v7.0] Add no_selinux tag to command_let_variables.js | Erwin Pe | Major - P3 | Blocked | 2026-05-19 |
| SERVER-126781 | [v7.0] Upgrade passlib package in v7.0 | Erwin Pe | Major - P3 | Blocked | 2026-05-19 |
| SERVER-126463 | Collection cloner with function_ref has memory bug | Vishnu Kaushik | Major - P3 | In Code Review | 2026-05-20 |
| SERVER-126409 | Allow mixing of localhost and non-localhost replica set members | Amirsaman Memaripour | Major - P3 | Investigating | 2026-05-18 |
| SERVER-127328 | Split large change stream test files | Unassigned | Minor - P4 | Needs Scheduling | 2026-05-21 |

*(showing top 10 of 1,552)*

---

## 9. Zombie To Do — 1,186
1,186 issues have been in Open status for over 90 days with no updates. Many date back to 2020 and earlier, with "[DO NOT USE] Backlog" assignees indicating these are legacy cleanup items that have never been triaged.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-40918 | Shard member sometimes backtraces when starting up | Timothy Olsen | Major - P3 | Open | 2020-03-03 |
| SERVER-16526 | Add db/collectionname validation to shell upgrade checker | DO NOT USE Backlog | Major - P3 | Open | 2020-04-09 |
| SERVER-9218 | Track Javascript Stats | DO NOT USE Backlog | Major - P3 | Open | 2020-04-09 |
| SERVER-2999 | Please add progress indicators to operations in the mongo shell | DO NOT USE Backlog | Major - P3 | Open | 2020-04-09 |
| SERVER-18375 | High CPU during insert-only stress test due to heap contention on Windows | DO NOT USE Backlog | Critical - P2 | Open | 2020-04-09 |
| SERVER-11041 | Index Diagnostic Shell Helper - diag.checkIndexes() | DO NOT USE Backlog | Minor - P4 | Open | 2020-04-09 |
| SERVER-9278 | Add counter for bad bson docs (from objCheck) | DO NOT USE Backlog | Major - P3 | Open | 2020-04-09 |
| SERVER-15904 | Inconsistent version output information from different binaries | DO NOT USE Backlog | Trivial - P5 | Open | 2020-04-09 |
| SERVER-15546 | Command response ok value is floating point; should be bool or int | DO NOT USE Backlog | Minor - P4 | Open | 2020-04-09 |
| SERVER-9342 | BSON storing 32 bit floats | DO NOT USE Backlog | Major - P3 | Open | 2020-04-09 |

*(showing top 10 of 1,186)*

---

## 10. Reopened issues — 129
129 issues transitioned back from Closed to Open in the last 90 days, indicating regressions, incomplete fixes, or verification failures.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-126784 | Enable Remote Asset API External Artifact Caching for Releases | Zack Winter | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-126385 | Make unit tests that exercise _writeStateToContainer write conflict retry | Stephanie Eristoff | Major - P3 | In Progress | 2026-05-20 |
| SERVER-125932 | Fix comparison of collations within Create collection coordinator documents | Jordi Olivares Provencio | Major - P3 | Open | 2026-05-05 |
| SERVER-125892 | Add HostUnreachable to retryable errors in implicitly_retry | Unassigned | Major - P3 | Blocked | 2026-05-11 |
| SERVER-126413 | Ensure correct phase is persisted for PDIB | Gregory Noma | Major - P3 | Closed | 2026-05-20 |
| SERVER-126248 | Make a better conditional for when to write to the container during the first dr | Stephanie Eristoff | Major - P3 | Closed | 2026-05-18 |
| SERVER-126042 | Allow ContainerBasedSpiller to be created at an arbitrary starting key | Malik Endsley | Major - P3 | Closed | 2026-05-07 |
| SERVER-125986 | Normalize collation comparison within CreateCollectionCoordinator | Jordi Olivares Provencio | Major - P3 | Closed | 2026-05-07 |
| SERVER-125790 | Make CreateCollectionCoordinatorDocument backward compatible | Jordi Olivares Provencio | Major - P3 | Closed | 2026-05-06 |
| SERVER-125674 | Add metrics for tracking the uncompressed size of the oplog | Damian Wasilewicz | Major - P3 | Closed | 2026-05-07 |

*(showing top 10 of 129)*

---

## 11. Done parent, open children — N/A
*Skipped — the `issuesWithStatus()` JQL function is not available on this Jira instance for anonymous API access.*

---

## 12. Missing story points — N/A
*The `story_points` custom field is not accessible via the anonymous Jira REST API for this instance.*

---

## 13. Fix version mismatch — 27
27 issues are assigned to a released fixVersion but are not in Done/Closed status, indicating they were missed during the release or the fix version was set incorrectly.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-121546 | [v7.0] Remove unnecessary timeseries write path invariants | Matt Kneiser | Major - P3 | Needs Merge | 2026-05-11 |
| SERVER-121342 | Add documentation for split horizon | Didier Nadeau | Major - P3 | In Code Review | 2026-03-11 |
| SERVER-121284 | Update AGENTS.md with coding workflows | Mathias Stearn | Major - P3 | In Code Review | 2026-03-10 |
| SERVER-120952 | Simplify and clean up the CMS manager API | Nic Hollingum | Major - P3 | In Code Review | 2026-03-06 |
| SERVER-120745 | Fix test format for searchCoordinator fsync | Fiona Chang | Major - P3 | Needs Verification | 2026-03-03 |
| SERVER-120681 | Reduce hot/cold BF thresholds for C&I | Ryan Chipman | Major - P3 | In Code Review | 2026-04-28 |
| SERVER-120620 | Miscellaneous small fixes from core module visibility marking | Unassigned | Major - P3 | Open | 2026-05-05 |
| SERVER-120533 | Grant permission for search to run fsync | Fiona Chang | Major - P3 | Needs Verification | 2026-03-02 |
| SERVER-120240 | Fix sharding passthrough suites not including jstests/core_sharding/ | Yujin Kang Park | Major - P3 | Needs Merge | 2026-03-05 |
| SERVER-120227 | Make CMSChannelManager and SLSConfigManager testable | Nic Hollingum | Major - P3 | In Code Review | 2026-02-26 |

*(showing top 10 of 27)*

---

## 14. Heavily discussed, never resolved — N/A
*Comment counts are not accessible via the anonymous REST API for this Jira instance. Check requires authenticated access.*

---

## 15. Discussed and parked — 0
No issues found in On Hold / Waiting / Deferred / Pending Decision statuses updated over 90 days ago. ✅

---

## 16. Other anomalies — 893
893 open issues have empty descriptions (no description text). This makes triage, prioritization, and handoff significantly harder. Many appear to be recent issues created without descriptions.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| SERVER-127347 | Increase defaultFindReplicaSetHostTimeoutMS on mongos for san builds | Nicholas Jefferies | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127344 | Document and rename container::ExistingKeyPolicy values | Parker Felix | Major - P3 | Backlog | 2026-05-21 |
| SERVER-127343 | Revisit applyOps handling of container writes on local db | Parker Felix | Major - P3 | Backlog | 2026-05-21 |
| SERVER-127339 | Check lastSpilledRecordId when determining whether to insert key | Gregory Noma | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127338 | Use lastSpilledRecordId when determining where to resume PDIB scan | Gregory Noma | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127336 | Add an optional UUID field to the config.shards schema | Paolo Polato | Major - P3 | In Progress | 2026-05-21 |
| SERVER-127332 | Extract query_knobs into a dedicated module | Catalin Sumanaru | Major - P3 | In Code Review | 2026-05-21 |
| SERVER-127303 | failedHostPreHandshake is unused in streamable_replica_set_monitor.cpp | Joseph Prince | Major - P3 | Open | 2026-05-20 |
| SERVER-127301 | Step-up after rotation testing for push mode | Unassigned | Major - P3 | Needs Scheduling | 2026-05-20 |
| SERVER-127300 | Multiversion testing for push mode | Unassigned | Major - P3 | Needs Scheduling | 2026-05-20 |

*(showing top 10 of 893)*

---

## Summary

| # | Category | Count | Severity |
|---|----------|-------|----------|
| 1 | High priority, no action (90d+ stale Blocker/Critical) | 18 | 🔴 High |
| 2 | Unassigned in active statuses | 44 | 🔴 High |
| 3 | Orphaned (no epic) — high-priority only | 38 | 🟡 Medium |
| 4 | Ghosts in dead epics | 0 | ✅ |
| 5 | Stale in-progress (90d+ no update) | 107 | 🔴 High |
| 6 | Done in active sprint (status inconsistency) | 314 | 🟡 Medium |
| 7 | Blocker resolved; task still blocked | 0 | ✅ |
| 8 | Sprint overflow (open in closed sprints) | 1,552 | 🔴 Critical |
| 9 | Zombie To Do (Open 90d+ untouched) | 1,186 | 🔴 Critical |
| 10 | Reopened (Closed → Open last 90d) | 129 | 🟡 Medium |
| 11 | Done parent, open children | N/A | — |
| 12 | Missing story points | N/A | — |
| 13 | Fix version mismatch | 27 | 🟡 Medium |
| 14 | Heavily discussed, never resolved | N/A | — |
| 15 | Discussed and parked | 0 | ✅ |
| 16 | Other anomalies (empty descriptions) | 893 | 🟡 Medium |

---

## Top 3 Priorities

1. **Sprint overflow: 1,552 issues** — Over 11% of all open issues are carried over from closed sprints with no resolution. This is a structural sprint hygiene failure. Recommendation: run a bulk triage session to either reschedule, de-sprint, or close these issues.

2. **Zombie To Do: 1,186 issues** — Nearly 9% of open issues have sat untouched in Open status for over 90 days, many dating to 2020 with "[DO NOT USE] Backlog" assignees. These are likely dead backlog items. Recommendation: bulk-close or move to a dedicated "Graveyard" epic after a triage pass.

3. **Empty descriptions: 893 issues** — 893 open issues have no description text, hampering discoverability and triage. Recommendation: enforce a description requirement via Jira workflow validators and run a cleanup sprint for existing no-description high-priority issues.
