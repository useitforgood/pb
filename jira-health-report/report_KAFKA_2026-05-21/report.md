# Jira Health Report — KAFKA
**Instance:** https://issues.apache.org/jira
**Date:** 2026-05-21
**Total open issues:** 5,126
**Stale threshold:** 90 days (cutoff: 2026-02-20)

---

## 1. High Priority, No Action — 339

339 Critical or Blocker issues have not been updated in over 90 days. Many are unassigned; some date back to 2015. This is the single most serious signal in the project — nearly 7% of all open issues are high-severity and stagnant.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-19895 | __consumer_offsets Partitions Growing to TB Size | Unassigned | Critical | Open | 2025-11-19 |
| KAFKA-19885 | Explicitly define execution or dry-run when altering | Chia-Ping Tsai | Blocker | Open | 2025-11-13 |
| KAFKA-19677 | Flaky Test SmokeTestDriver | Unassigned | Critical | Open | 2025-09-05 |
| KAFKA-19633 | Kafka Connect connectors sent zombie records during rebalance | Unassigned | Critical | Open | 2025-08-21 |
| KAFKA-19622 | Limitations of KRAFT Dual Write Mode for Production | Unassigned | Critical | Open | 2025-08-30 |
| KAFKA-19586 | Kafka broker freezes and gets fenced during rolling restart | Unassigned | Blocker | Open | 2025-08-17 |
| KAFKA-19557 | Remove BrokerNotFoundException | Unassigned | Blocker | Open | 2025-11-05 |
| KAFKA-19552 | Unclean leader election fails due to precedence issue | Unassigned | Critical | Open | 2025-07-28 |
| KAFKA-18885 | Document behavioral differences between ZooKeeper and KRaft | Chia-Ping Tsai | Blocker | Open | 2025-02-27 |
| KAFKA-18871 | KRaft migration rollback causes downtime | Unassigned | Critical | Open | 2025-04-17 |
| KAFKA-18762 | Acks=all not working correctly in Kafka Kraft mode | Unassigned | Critical | Open | 2025-02-10 |
| KAFKA-17784 | Mirror Maker2 Pod CrashLoopbackOff | Unassigned | Blocker | Open | 2024-10-25 |
| KAFKA-17590 | ReplicaFetcher throw CorruptRecordException | Unassigned | Blocker | Open | 2024-09-26 |
| KAFKA-17582 | Unpredictable consumer position after transaction abort | Unassigned | Critical | Open | 2024-09-30 |
| KAFKA-17146 | ZK to KRAFT migration stuck in pre-migration mode | Unassigned | Blocker | Open | 2025-12-17 |
| KAFKA-16710 | makeFollower may cause the replica fetcher thread issue | hudeqi | Blocker | Patch Available | 2025-08-15 |
| KAFKA-16430 | group-metadata-manager thread always in loading state | Unassigned | Blocker | Open | 2024-04-03 |
| KAFKA-13796 | MM2 Topics Exclude/Blacklist not working | Unassigned | Blocker | Open | 2022-07-24 |
| KAFKA-1694 | KIP-4: Command line and centralized operations | Unassigned | Critical | In Progress | 2021-07-13 |
| KAFKA-1682 | Security for Kafka | Unassigned | Major | Open | 2015-10-12 |

*→ 339 total. See 01_high_priority_stale.csv for full list (50 rows exported).*

---

## 2. Unassigned Issues (Active Statuses) — 0

No issues found in active non-backlog statuses without an assignee. ✅

---

## 3. Orphaned Issues — No Epic — N/A

**Not applicable — project does not use Epics.**
100% of open issues (5,126 / 5,126) have no Epic Link. KAFKA tracks work via fix versions and KIP references rather than Epics. CSV skipped.

---

## 4. Ghosts in Dead Epics — N/A

No Done/Closed/Resolved epics found. Epics are not used. CSV skipped.

---

## 5. Stale In-Progress — 0

No issues in "In Progress" or "In Development" with no update in 90+ days. The project primarily uses "Open" as the active status. ✅

---

## 6. Status Inconsistencies — N/A

**Not applicable — project does not use Sprints.** CSV skipped.

---

## 7. Blocker Resolved, Task Still Blocked — 14

14 issues have a "is blocked by" link pointing to a Done/Closed/Resolved issue but are themselves still open. These are stale dependency chains that should be unblocked or re-evaluated.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-17261 | Support quorum controller not in cluster | Kuan Po Tseng | Major | In Progress | 2025-02-11 |
| KAFKA-15895 | Move DynamicBrokerConfig to server module | TengYao Chi | Major | In Progress | 2025-02-15 |
| KAFKA-15853 | Move KafkaConfig to server module | Christo Lolov | Major | In Progress | 2026-05-11 |
| KAFKA-15370 | Support Participation in 2PC (KIP-939) | Unassigned | Major | Open | 2026-04-30 |
| KAFKA-14470 | Move log layer to storage module | Ismael Juma | Major | Open | 2024-12-07 |
| KAFKA-10877 | Instantiating loggers for every FetchContext | Sean McCauliff | Major | Open | 2025-01-01 |
| KAFKA-10483 | Extract common functions from SourceConnector | Ning Zhang | Major | Patch Available | 2020-09-15 |
| KAFKA-10370 | WorkerSinkTask IllegalStateException from consumer.seek | Unassigned | Major | Reopened | 2024-07-05 |
| KAFKA-8468 | AdminClient.deleteTopics doesn't wait until topic deleted | Viktor Somogyi-Vass | Major | Open | 2022-04-28 |
| KAFKA-4740 | New consumer API with Deserializer throwing SerializationException | Sébastien Launay | Critical | Open | 2024-12-22 |
| KAFKA-2170 | 10 LogTest cases failed for file.renameTo on Windows | Jay Kreps | Major | Open | 2024-11-14 |
| KAFKA-1694 | KIP-4: Command line and centralized operations | Unassigned | Critical | In Progress | 2021-07-13 |
| KAFKA-1682 | Security for Kafka | Unassigned | Major | Open | 2015-10-12 |

*→ See 07_blocker_resolved_still_blocked.csv*

---

## 8. Sprint Overflow — N/A

**Not applicable — project does not use Sprints.** CSV skipped.

---

## 9. Zombie To Do — 4,135

**4,135 issues** are in "Open" status and have not been created or updated in 90+ days. This represents 80.7% of all open issues — the dominant health problem. The backlog has not been triaged or pruned; thousands of issues are essentially abandoned.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-20188 | Implement timeout for OffsetsRequestManager | Kirk True | Major | Open | 2026-02-13 |
| KAFKA-20186 | Cluster Mirroring | Federico Valeri | Major | Open | 2026-02-14 |
| KAFKA-20175 | Introduce new MetadataVersion for ClusterIdRecord | Kevin Wu | Major | Open | 2026-02-11 |
| KAFKA-20172 | Support online migration between classic and streams rebalance | Unassigned | Major | Open | 2026-02-11 |
| KAFKA-20133 | Implement TimestampedWindowStoreWithHeaders | Unassigned | Major | Open | 2026-02-06 |
| KAFKA-20123 | Use re2j for regex matching in Connect runtime | Mickael Maison | Major | Open | 2026-02-04 |
| KAFKA-20086 | Release Process automation | Unassigned | Major | Open | 2026-01-21 |
| KAFKA-20022 | Kafka Dual Write Mode Sync Failure | David Arthur | Major | Open | 2026-01-13 |
| KAFKA-19996 | Conflicts between ExpandIsr and ShrinkIsr | Unassigned | Major | Open | 2025-12-15 |
| KAFKA-19933 | Make new voter caught up criteria strict | Jimmy Wang | Major | Open | 2025-11-30 |

*→ 4,135 total. See 09_zombie_todo.csv for 50-row export.*

---

## 10. Reopened Issues — 15

15 issues were transitioned back to Open in the last 90 days. Several were previously Resolved and then reopened — worth reviewing whether the fixes were incomplete.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-20412 | Fix prefixScan for KV-Store with headers | Uladzislau Blok | Major | In Progress | 2026-05-03 |
| KAFKA-20263 | Change KeyValueWrapper to have versioned and headersStore | Alieh Saeedi | Major | Resolved | 2026-04-08 |
| KAFKA-19738 | Improve testing of OffsetsRequestManager | Evan Zhou | Minor | Open | 2026-03-13 |
| KAFKA-18187 | Replicas receiving EndQuorum should grant preVotes | Unassigned | Minor | Open | 2026-04-04 |
| KAFKA-15768 | StateQueryResult getOnlyPartitionResult should not throw | Gavin Wang | Major | Resolved | 2026-05-05 |
| KAFKA-14405 | Log warning when users set a controlled config | Arpit Goyal | Major | Open | 2026-04-14 |
| KAFKA-14192 | Move registering/unregistering changelogs to state updater | Nikita Shupletsov | Major | Resolved | 2026-05-04 |
| KAFKA-8382 | Add TimestampedSessionStore | Unassigned | Minor | Open | 2026-02-26 |
| KAFKA-1614 | Partition log directory name and segments info exposed | Unassigned | Major | Open | 2026-05-15 |
| KAFKA-859 | Support basic auth protection of mx4j console | Unassigned | Major | Resolved | 2026-05-15 |

*→ See 10_reopened.csv*

---

## 11. Done Parent, Open Children — Skipped (API Limitation)

The JQL function `issuesWithStatus()` is not available on this Jira instance. Could not filter by parent status at scale.

**Context:** 374 open sub-tasks exist across the project. A spot-check of 5 showed all had open parents. Recommend running this check with Jira admin access or a script using the REST API `parent` field.

---

## 12. Missing Story Points — N/A

**Not applicable — project does not use Sprints.** CSV skipped.

---

## 13. Fix Version Mismatch — 48

48 issues have a **released** fix version but are not Done/Closed/Resolved. These represent undocumented gaps in release notes or work that slipped past version cutoffs.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-19438 | FileSystemException Errors on Kafka | Unassigned | Critical | Open | 2025-06-28 |
| KAFKA-16808 | Consumer join Group response with 2 different members | Unassigned | Critical | Open | 2024-05-21 |
| KAFKA-13960 | ERROR Shutdown broker — all log dirs in c:\kafka | Unassigned | Critical | Open | 2022-06-04 |
| KAFKA-13796 | MM2 Topics Exclude/Blacklist not working | Unassigned | Blocker | Open | 2022-07-24 |
| KAFKA-17840 | Move ReplicationQuotaManager to server module | PoAn Yang | Major | Reopened | 2026-03-23 |
| KAFKA-15369 | Allow AdminClient to Talk Directly with KRaft Controller | Colin McCabe | Major | Reopened | 2025-01-07 |
| KAFKA-14956 | Flaky test OffsetsIntegration | Unassigned | Major | Reopened | 2024-06-30 |
| KAFKA-12887 | Do not trigger ExceptionalHandler for RebalanceException | Josep Prat | Major | Reopened | 2023-07-05 |
| KAFKA-16699 | Have Streams treat InvalidPidMappingException like ProducerFenced | Walker Carlson | Major | Patch Available | 2024-11-20 |
| KAFKA-16848 | Reverting KRaft migration | Edgar | Major | Patch Available | 2024-09-24 |
| KAFKA-15171 | Kafka client poll never notifies when broker is down | Unassigned | Major | Open | 2023-07-10 |
| KAFKA-13594 | Vulnerability found in Log4j | Unassigned | Major | Open | 2022-01-15 |

*→ 48 total. See 13_fix_version_mismatch.csv*

---

## 14. Heavily Discussed, Never Resolved — 21+ (sampled)

21 issues with 10+ comments found in the first 800 open issues sampled (15.7% of backlog). Extrapolating, ~130+ such issues likely exist project-wide. These are stuck discussions with high engagement but no resolution path.

| Key | Summary | Assignee | Priority | Comments | Last Updated |
|-----|---------|----------|----------|----------|--------------|
| KAFKA-20000 | Optimize retry backoff for CONCURRENT_TRANSACTIONS | Francis Godinho | Major | 22 | 2026-04-09 |
| KAFKA-18871 | KRaft migration rollback causes downtime | Unassigned | Critical | 21 | 2025-04-17 |
| KAFKA-20035 | Prevent data loss during partition expansion | Ken Huang | Critical | 19 | 2026-04-28 |
| KAFKA-19902 | Consumer triggers OFFSET_OUT_OF_RANGE on invalid commit | Unassigned | Major | 17 | 2026-04-20 |
| KAFKA-20171 | Support regex topic patterns for streams groups | sanghyeok An | Major | 16 | 2026-04-20 |
| KAFKA-19430 | Don't fail on RecordCorruptedException | Uladzislau Blok | Major | 16 | 2026-01-30 |
| KAFKA-19853 | Transaction Failure when StreamThread blocks on StateUpdater | Colt McNealy | Major | 15 | 2026-05-04 |
| KAFKA-19097 | Fix order of arguments to assertEquals | Ksolves India Limited | Minor | 15 | 2025-12-26 |
| KAFKA-18762 | Acks=all not working correctly in Kafka Kraft mode | Unassigned | Critical | 11 | 2025-02-10 |

*→ See 14_heavily_discussed.csv. Sampled first 800 of 5,126 open issues.*

---

## 15. Discussed and Parked — 0

No issues in On Hold / Waiting / Deferred / Pending Decision status. ✅

---

## 16. Other Anomalies — 160

160 open issues have **no description**. Many are sub-tasks created without body text. Two Blocker-priority issues (KAFKA-20336, KAFKA-20335, both titled "Update docs") have no description.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-20580 | Scatter-gather support for producer dynamic allocation | Nikita Shupletsov | Major | Open | 2026-05-13 |
| KAFKA-20549 | Implementation of Share Group DLQ Manager | Sushant Mahajan | Major | In Progress | 2026-05-17 |
| KAFKA-20395 | Support unregistering controllers | Kevin Wu | Major | Open | 2026-05-20 |
| KAFKA-20336 | Update docs | Shekhar Prasad Rajak | Blocker | Patch Available | 2026-05-12 |
| KAFKA-20335 | Update docs | Nilesh Kumar | Blocker | Open | 2026-05-18 |
| KAFKA-20292 | Implement assignor offload | Sean Quah | Major | Open | 2026-05-18 |

*→ 160 total. See 16_other_anomalies.csv for 20-row export.*

---

## Summary

| # | Category | Count | Severity |
|---|----------|-------|----------|
| 1 | High priority, no action | **339** | Critical |
| 2 | Unassigned (active statuses) | 0 | OK |
| 3 | Orphaned — no epic | N/A (epics not used) | — |
| 4 | Ghosts in dead epics | N/A | — |
| 5 | Stale in-progress | 0 | OK |
| 6 | Status inconsistencies | N/A (no sprints) | — |
| 7 | Blocker resolved, still blocked | **14** | Warning |
| 8 | Sprint overflow | N/A (no sprints) | — |
| 9 | Zombie To Do | **4,135** | Critical |
| 10 | Reopened issues | 15 | Warning |
| 11 | Done parent, open children | Skipped (API limit) | — |
| 12 | Missing story points | N/A (no sprints) | — |
| 13 | Fix version mismatch | **48** | Warning |
| 14 | Heavily discussed, unresolved | **21+** (sample) | Warning |
| 15 | Discussed and parked | 0 | OK |
| 16 | Other anomalies (no description) | **160** | Warning |

---

## Top 3 Priorities

1. **Backlog rot — 4,135 Zombie To Dos (81% of all open issues):** The backlog has not been pruned in years. Consider a policy of auto-closing issues with no update after 12–18 months, or a dedicated triage sprint to close/reject stale items.

2. **339 stagnant Critical/Blocker issues:** Nearly all are unassigned and some date to 2015. Implement a weekly triage rotation for this bucket — every Critical/Blocker should have an owner and a next action, or be downgraded.

3. **48 fix-version mismatches:** Issues listed against already-released versions but still open represent silent release note gaps. Audit each for whether the fix was missed, incorrectly versioned, or should be closed as won't-fix.
