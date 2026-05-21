# Jira Health Report — KAFKA
**Instance:** https://issues.apache.org/jira
**Date:** 2026-05-21
**Total open issues:** 5,126
**Stale threshold:** 90 days

---

## Summary

| # | Category | Count | Severity |
|---|----------|-------|----------|
| 1 | High priority (Blocker/Critical), no action for 90+ days | 339 | 🔴 Critical |
| 2 | Unassigned in-flight issues | 0 | ✅ OK |
| 3 | Orphaned issues — no epic | N/A | ⚪ Not applicable (100% of open issues have no epic — project does not use Epics) |
| 4 | Ghosts in dead epics | N/A | ⚪ Not applicable (no epics used) |
| 5 | Stale In Progress / Patch Available (90+ days) | 416 | 🔴 Critical |
| 6 | Status inconsistencies (Resolved with open blockers) | 36 | 🟡 Warning |
| 7 | Blocker resolved, task still blocked | — | ⚪ Could not verify (no issueFunction support on public API) |
| 8 | Sprint overflow | 0 | ✅ OK (no sprints configured) |
| 9 | Zombie To Do (Open, untouched 90+ days) | 4,135 | 🔴 Critical |
| 10 | Reopened issues | 71 | 🟡 Warning |
| 11 | Done parent, open children | 0 | ✅ OK |
| 12 | Missing story points in active sprints | N/A | ⚪ Not applicable (no story points field / sprints) |
| 13 | Fix version mismatch (released version, not Done) | 48 | 🟡 Warning |
| 14 | Heavily discussed, never resolved (≥10 comments, open) | 15 (sample) | 🟡 Warning |
| 15 | Discussed and parked (Patch Available, stale 90+ days) | 224 | 🔴 Critical |
| 16 | Other anomalies (no description, no comments) | 60 | 🟡 Warning |

**Total flagged issues:** ~5,344 (across overlapping checks)

---

## Top 3 Priorities

1. **Zombie To Do backlog (4,135 issues)** — The vast majority of open issues are in "Open" status and have not been updated in 90+ days. This signals massive backlog rot. A triage campaign is urgently needed to close, defer, or reassign stale tickets.
2. **High-priority Blockers/Criticals with no action (339 issues)** — 339 issues marked Critical or Blocker have been sitting untouched for over 90 days. Several involve production data-loss risks (e.g. KAFKA-19633 zombie records, KAFKA-18762 acks=all broken in KRaft mode). These need immediate owner assignment.
3. **Stale Patch Available backlog (224+ issues)** — Patches have been submitted but not reviewed or merged for 90+ days. This blocks contributors and signals a review bandwidth bottleneck.

---

## 1. High Priority, No Action — 339 issues

Open Blocker/Critical issues not updated for 90+ days. Many involve production-level bugs with no assignee.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-19895 | __consumer_offsets Partitions Growing to TB Size | Unassigned | Critical | Open | 2025-11-19 |
| KAFKA-19885 | Explicitly define execution or dry-run when altering | Chia-Ping Tsai | Blocker | Open | 2025-11-13 |
| KAFKA-19677 | Flaky Test SmokeTestDriver | Unassigned | Critical | Open | 2025-09-05 |
| KAFKA-19633 | Connect connectors sent zombie records during rebalance | Unassigned | Critical | Open | 2025-08-21 |
| KAFKA-19622 | Limitations of KRAFT Dual Write Mode for Production | Unassigned | Critical | Open | 2025-08-30 |
| KAFKA-19586 | Kafka broker freezes and gets fenced during rolling restart | Unassigned | Blocker | Open | 2025-08-17 |
| KAFKA-19557 | Remove BrokerNotFoundException | Unassigned | Blocker | Open | 2025-11-05 |
| KAFKA-19552 | Unclean leader election fails due to precedence issue | Unassigned | Critical | Open | 2025-07-28 |
| KAFKA-19438 | FileSystemException Errors on Kafka Broker | Unassigned | Critical | Open | 2025-06-28 |
| KAFKA-18871 | KRaft migration rollback causes downtime | Unassigned | Critical | Open | 2025-04-17 |
| KAFKA-18762 | 'Acks=all' not working correctly in Kafka KRaft mode | Unassigned | Critical | Open | 2026-01-20 |
| KAFKA-18726 | Support root cause exception as nested exception to Timeout | Vineet Kumar | Blocker | Open | 2025-02-04 |
| KAFKA-18602 | Incorrect FinalizedVersionLevel reported for dynamic KRaft | PoAn Yang | Critical | In Progress | 2025-04-10 |
| KAFKA-18495 | Remove Invalid 'numberOfOpenFiles' Metric from RocksDB | Unassigned | Blocker | Open | 2025-06-15 |
| KAFKA-18898 | 4.0 Upgrade docs rendering below other versions | Unassigned | Critical | Open | 2025-02-28 |
| KAFKA-18885 | Document behavioral differences ZooKeeper vs KRaft | Chia-Ping Tsai | Blocker | Open | 2025-02-27 |
| KAFKA-19059 | Client 3.5.0 connecting to ancient broker | Unassigned | Critical | Open | 2025-03-31 |
| KAFKA-19142 | TestKitNodes doesn't bootstrap KIP-853 correctly | PoAn Yang | Critical | Open | 2025-04-14 |
| KAFKA-19329 | Dynamic Connect Worker Configuration | Kunal Sevkani | Critical | Open | 2025-05-25 |
| KAFKA-18744 | sasl.login.callback.handler.class used for wrong purpose | Unassigned | Critical | Open | 2026-01-20 |

*339 total — see `01_high_priority_stale.csv` for full list.*

---

## 2. Unassigned In-Flight Issues — 0 issues

No issues found in active (non-Open/Backlog/Done) statuses without an assignee. ✅

---

## 3. Orphaned Issues — No Epic — N/A

**Not applicable.** 100% of open issues (5,126/5,126) have no Epic Link. Apache Kafka does not use the Epic hierarchy in this Jira instance. Issues are organized via KIPs and fix versions instead.

---

## 4. Ghosts in Dead Epics — N/A

Not applicable — no Epics are used in this project.

---

## 5. Stale In Progress / Patch Available — 416 issues

Issues in active states (In Progress or Patch Available) with no update for 90+ days. Indicates abandoned work or stalled reviews.

| Key | Summary | Assignee | Priority | Status | Last Updated |
|-----|---------|----------|----------|--------|--------------|
| KAFKA-20195 | Better offset reset for new consumer group | Levani Kokhreidze | Major | In Progress | 2026-02-18 |
| KAFKA-20088 | CIDR-based Host Patterns for ACLs | Maros Orsak | Major | In Progress | 2026-01-25 |
| KAFKA-20029 | Disallow partition count increase for __transaction_state | sanghyeok An | Minor | In Progress | 2026-01-07 |
| KAFKA-19989 | Fix order of arguments in assertEquals | Ksolves India Limited | Minor | In Progress | 2025-12-12 |
| KAFKA-19936 | ReplicaManager counts duplicated records to BytesInPerSec | PoAn Yang | Major | In Progress | 2026-01-03 |
| KAFKA-19910 | Support rack awareness in UniformHeterogeneousAssignmentBuilder | PoAn Yang | Major | In Progress | 2025-11-23 |
| KAFKA-19889 | max.connections.per.ip.overrides does not apply to named | Vadym Zhytkevych | Minor | Patch Available | 2026-02-15 |
| KAFKA-19850 | KRaft voter auto join will add removed voter immediately | TaiJuWu | Major | Patch Available | 2025-12-03 |
| KAFKA-19806 | Hook to enable/disable multi-partition remote fetch feature | Kamal Chandraprakash | Major | Patch Available | 2025-10-21 |
| KAFKA-19670 | Unify the command-line parser | HongYi Chen | Major | In Progress | 2025-09-10 |
| KAFKA-19613 | Expose consumer CorruptRecordException | Uladzislau Blok | Minor | In Progress | 2026-01-15 |
| KAFKA-19472 | BufferOverflowException thrown by RemoteLogManager | dyingjiecai | Major | Patch Available | 2025-11-06 |
| KAFKA-19430 | Don't fail on RecordCorruptedException | Uladzislau Blok | Major | In Progress | 2026-01-30 |
| KAFKA-19399 | version and source link in NOTICE-binary file | Palak Kapoor | Minor | In Progress | 2025-07-21 |
| KAFKA-19387 | Support rack awareness in Range and Uniform assignors | PoAn Yang | Major | In Progress | 2026-01-22 |
| KAFKA-19276 | Compare assignment configuration only when relevant | Uladzislau Blok | Minor | Patch Available | 2026-02-08 |
| KAFKA-19272 | Handling scenarios for initPid(keepPrepared=true) | Ritika Reddy | Major | In Progress | 2025-07-22 |
| KAFKA-19200 | Indexes sanity checked on startup | Gaurav Narula | Major | In Progress | 2025-05-01 |
| KAFKA-18994 | Wrong configuration in docker-compose.yml example | Unassigned | Minor | Patch Available | 2025-03-15 |
| KAFKA-18873 | Incorrect error message for max.in.flight.requests | Eslam Mohamed | Minor | Patch Available | 2025-08-17 |

*416 total — see `05_stale_inprogress.csv` for full list.*

---

## 6. Status Inconsistencies — 36 issues

Issues marked Resolved that still have open blocking dependencies. These may block downstream work without being visible in active queues.

| Key | Summary | Status | Last Updated |
|-----|---------|--------|--------------|
| KAFKA-20216 | Jetty 12 requires slf4j 2 | Resolved | — |
| KAFKA-19939 | ProductionExceptionHandler not supported on global thread | Resolved | — |
| KAFKA-19144 | Move DelayedProduce to server module | Resolved | — |
| KAFKA-18888 | Add support for Authorizer | Resolved | — |
| KAFKA-18839 | Drop support for eager rebalancing in Streams | Resolved | — |
| KAFKA-18486 | Remove ReplicaManager#becomeLeaderOrFollower | Resolved | — |
| KAFKA-16343 | Improve tests of streams foreignkeyjoin package | Resolved | — |
| KAFKA-16287 | Implement example test for rebalance callback scenarios | Resolved | — |
| KAFKA-16074 | Fix thread leaks in ReplicaManagerTest | Resolved | — |
| KAFKA-16059 | Fix leak of ExpirationReaper threads | Resolved | — |

*36 total — see `06_status_inconsistencies.csv` for full list.*

---

## 7. Blocker Resolved, Task Still Blocked — N/A

Could not execute `issueFunction in linkedIssuesOf()` via the public unauthenticated Jira REST API (requires ScriptRunner plugin access). Check skipped — flag for manual review.

---

## 8. Sprint Overflow — 0 issues

No sprint-based workflow is configured for this project. ✅

---

## 9. Zombie To Do — 4,135 issues

Issues in Open status that were created more than 90 days ago and have not been updated in 90+ days. This represents **80.7% of all open issues** and is the single largest health problem in this project.

| Key | Summary | Assignee | Priority | Last Updated |
|-----|---------|----------|----------|--------------|
| KAFKA-20188 | Implement timeout for OffsetsRequestManager | Kirk True | Major | 2026-02-13 |
| KAFKA-20186 | Cluster Mirroring | Federico Valeri | Major | 2026-02-14 |
| KAFKA-20180 | Add last-applied-record-latency metric for brokers | Kevin Wu | Major | 2026-02-17 |
| KAFKA-20175 | Introduce new MetadataVersion for ClusterIdRecord | Kevin Wu | Major | 2026-02-11 |
| KAFKA-20174 | Auto-formatting for KRaft observers | Kevin Wu | Major | 2026-02-11 |
| KAFKA-20172 | Support online migration between classic and streams rebalancing | Unassigned | Major | 2026-02-11 |
| KAFKA-20154 | Migrate Kafka modules to Java 21 | Sujay Hegde | Major | 2026-02-12 |
| KAFKA-20151 | C4 Diagram architecture execution strategy | Sujay Hegde | Major | 2026-02-08 |
| KAFKA-20149 | C4 Architecture Diagram for Kafka Ecosystem | Sujay Hegde | Major | 2026-02-07 |
| KAFKA-20143 | Add javadoc to org.apache.kafka.tools.api module | Ken Huang | Major | 2026-02-08 |
| KAFKA-20142 | Add javadoc to org.apache.kafka.streams module | Ken Huang | Minor | 2026-02-09 |
| KAFKA-20141 | Add javadoc to org.apache.kafka.server module | Ken Huang | Minor | 2026-02-08 |
| KAFKA-20140 | Add javadoc to coordinator.group.api module | Ken Huang | Minor | 2026-02-06 |
| KAFKA-20139 | Add javadoc to org.apache.kafka.connect module | Ken Huang | Minor | 2026-02-08 |
| KAFKA-20138 | Add javadoc to org.apache.kafka.common module | Ken Huang | Minor | 2026-02-08 |

*4,135 total (200 sampled in CSV) — see `09_zombie_todo.csv` for sample.*

---

## 10. Reopened Issues — 71 issues

Issues that were previously resolved/closed but have been reopened, suggesting incomplete fixes or regressions.

| Key | Summary | Assignee | Priority | Last Updated |
|-----|---------|----------|----------|--------------|
| KAFKA-19230 | Fail build for FunctionalInterfaceMethodChanged warning | Duc Tri Nguyen | Major | 2025-08-14 |
| KAFKA-17840 | Move ReplicationQuotaManager and ClientRequestQuotaManager | PoAn Yang | Major | 2026-03-23 |
| KAFKA-17755 | AbstractPartitionAssignor cannot enable RackAwareAssignment | Jerry Cai | Major | 2025-03-17 |
| KAFKA-16983 | Generate Docker Official Images PR | Krish Vora | Major | 2024-06-18 |
| KAFKA-16444 | Run KIP-848 unit tests under code coverage | Unassigned | Minor | 2024-10-16 |
| KAFKA-16130 | Write junit test for ZK migration rollback | Unassigned | Major | 2024-08-28 |
| KAFKA-15863 | Handle push telemetry throttling with quota manager | Sanskar Jhajharia | Major | 2024-08-12 |
| KAFKA-15862 | Remove SecurityManager Support | Greg Harris | Major | 2024-09-30 |
| KAFKA-15411 | DelegationTokenEndToEndAuthorizationWithOwnerTest is Flaky | Proven Provenzano | Major | 2024-06-20 |
| KAFKA-15397 | Deserializing produce requests may cause memory leaks | hudeqi | Blocker | 2023-09-11 |
| KAFKA-15376 | Explore options for removing data earlier to current leader | Unassigned | Major | 2025-01-09 |
| KAFKA-15369 | Allow AdminClient to Talk Directly with KRaft Controller | Colin McCabe | Major | 2025-01-07 |
| KAFKA-14956 | Flaky test OffsetsApiIntegrationTest | Unassigned | Major | 2024-06-30 |
| KAFKA-14945 | Add Serializer#serializeToByteBuffer() | LinShunkang | Major | 2025-09-17 |
| KAFKA-14908 | Sporadic "Address already in use" when starting cluster | Unassigned | Major | 2025-10-15 |

*71 total — see `10_reopened.csv` for full list.*

---

## 11. Done Parent, Open Children — 0 issues

No closed/resolved parent issues with open subtasks found. ✅

---

## 12. Missing Story Points — N/A

The `story_points` field is not accessible via the public unauthenticated API and no active sprints are configured. Skipped.

---

## 13. Fix Version Mismatch — 48 issues

Issues assigned to an already-released fix version but still not in a Done/Resolved/Closed status. These represent shipped versions with unfinished work still tracked against them.

| Key | Summary | Assignee | Status | Fix Version | Last Updated |
|-----|---------|----------|--------|-------------|--------------|
| KAFKA-19438 | FileSystemException Errors on Kafka Broker | Unassigned | Open | 3.3.0 | 2025-06-28 |
| KAFKA-18233 | MirrorMaker 2 All Checkpoint Connector CPC tasks | Unassigned | Open | 3.5.1 | 2024-12-13 |
| KAFKA-17840 | Move ReplicationQuotaManager | PoAn Yang | Reopened | 4.0.0 | 2026-03-23 |
| KAFKA-17504 | EKU error in Kafka SSL | Unassigned | Open | 3.3.1 | 2024-09-09 |
| KAFKA-17490 | UpdateMetadataRequest failed (ClusterAuthorizationFailed) | jirar | Patch Available | 2.8.2 | 2024-09-06 |
| KAFKA-17107 | Backport of PR-15327 | Kartik Goyal | Open | 3.6.2 | 2024-07-10 |
| KAFKA-16848 | Reverting KRaft migration for migrating brokers | Edgar | Patch Available | 3.7.0 | 2024-09-24 |
| KAFKA-16808 | Consumer join Group response contains 2 different members | Unassigned | Open | 2.8.0 | 2024-05-21 |
| KAFKA-16699 | Streams treat InvalidPidMappingException like ProducerFenced | Walker Carlson | Patch Available | 3.8.0 | 2024-11-20 |
| KAFKA-16145 | Windows Kafka Shutdown | Unassigned | Open | 3.6.0 | 2024-02-14 |
| KAFKA-15369 | Allow AdminClient to Talk Directly with KRaft Controller | Colin McCabe | Reopened | 3.7.0 | 2025-01-07 |
| KAFKA-15171 | Kafka client poll never notifies when broker is down | Unassigned | Open | 3.2.1 | 2023-07-10 |
| KAFKA-14956 | Flaky test OffsetsApiIntegrationTest | Unassigned | Reopened | 3.5.0 | 2024-06-30 |
| KAFKA-13960 | ERROR Shutdown broker because all log dirs in c:\kafka | Unassigned | Open | 3.1.1 | 2022-06-04 |
| KAFKA-13796 | MM2 - Topics Exclude/Blacklist not working | Unassigned | Open | 3.0.0 | 2022-07-24 |

*48 total — see `13_fix_version_mismatch.csv` for full list.*

---

## 14. Heavily Discussed, Never Resolved — 15 issues (500-issue sample)

Open issues with 10+ comments that remain unresolved, indicating ongoing debate without consensus or decision.

| Key | Summary | Comments | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| KAFKA-20000 | Optimize retry backoff for CONCURRENT_TRANSACTIONS | 22 | In Progress | 2026-04-09 |
| KAFKA-20035 | Prevent data loss during partition expansion | 19 | Open | 2026-04-28 |
| KAFKA-19902 | Consumer triggers OFFSET_OUT_OF_RANGE on committed offset | 17 | Open | 2026-04-20 |
| KAFKA-20171 | Support regex topic patterns for streams groups | 16 | In Progress | 2026-04-20 |
| KAFKA-19430 | Don't fail on RecordCorruptedException | 16 | In Progress | 2026-01-30 |
| KAFKA-19853 | Transaction Failure when StreamThread blocks on StateUpdater | 15 | Patch Available | 2026-05-04 |
| KAFKA-20427 | Controllers can't form quorum on restart when hostnames change | 14 | Open | 2026-04-23 |
| KAFKA-19613 | Expose consumer CorruptRecordException | 14 | In Progress | 2026-01-15 |
| KAFKA-20049 | kafka-site build depends on hvishwanath/hugo | 12 | Open | 2026-04-13 |
| KAFKA-19753 | Metrics from FetchMetricsManager with topic tag are wrong | 12 | Open | 2026-05-15 |
| KAFKA-19704 | Kafka Broker Fails to Start After Upgrade to 4.1.0 | 11 | Open | 2025-09-17 |
| KAFKA-20463 | Merging a PR in kafka-site does not update the website | 10 | Open | 2026-04-28 |
| KAFKA-19804 | Improve heartbeat request manager initial HB interval | 10 | Open | 2026-04-09 |
| KAFKA-19785 | Two Kafka brokers were not active in 3 node cluster setup | 10 | Open | 2026-05-20 |
| KAFKA-19469 | Dead-letter queues for share groups | 10 | Open | 2026-03-28 |

*Note: based on a 500-issue sample — see `14_heavily_discussed.csv`.*

---

## 15. Discussed and Parked — 224 issues

Issues in "Patch Available" status not updated for 90+ days. Patches are waiting but receiving no review attention.

| Key | Summary | Assignee | Last Updated |
|-----|---------|----------|--------------|
| KAFKA-19889 | max.connections.per.ip.overrides does not apply | Vadym Zhytkevych | 2026-02-15 |
| KAFKA-19850 | KRaft voter auto join adds removed voter | TaiJuWu | 2025-12-03 |
| KAFKA-19806 | Hook to enable/disable multi-partition remote fetch | Kamal Chandraprakash | 2025-10-21 |
| KAFKA-19472 | BufferOverflowException in RemoteLogManager | dyingjiecai | 2025-11-06 |
| KAFKA-19276 | Compare assignment config when relevant | Uladzislau Blok | 2026-02-08 |
| KAFKA-19039 | refresh_collaborators.py messes .asf.yaml | Siyang He | 2025-11-13 |
| KAFKA-18994 | Wrong config in docker-compose.yml example | Unassigned | 2025-03-15 |
| KAFKA-18982 | Allow ClusterTests to ignore specific thread leaks | Edoardo Comar | 2025-07-31 |
| KAFKA-18873 | Incorrect error message for max.in.flight.requests | Eslam Mohamed | 2025-08-17 |
| KAFKA-18852 | ApiVersions should use Concurrent Collections | Unassigned | 2025-02-24 |

*224 total — see `15_discussed_and_parked.csv` for full list.*

---

## 16. Other Anomalies — 60 issues

Open issues with no description AND no comments — essentially empty placeholder tickets with no context.

| Key | Summary | Assignee | Status | Last Updated |
|-----|---------|----------|--------|--------------|
| KAFKA-20580 | Scatter-gather support for producer dynamic allocation | Nikita Shupletsov | Open | 2026-05-13 |
| KAFKA-20579 | Implement dynamic allocation for compressed data | Lianet Magrans | Open | 2026-05-13 |
| KAFKA-20578 | Implement dynamic allocation for uncompressed data | Lianet Magrans | Open | 2026-05-13 |
| KAFKA-20549 | Implementation of Share Group DLQ Manager | Sushant Mahajan | In Progress | 2026-05-17 |
| KAFKA-20451 | Move RequestChannel Responses to server module | Mickael Maison | Open | 2026-04-14 |
| KAFKA-20422 | Add DSL integration tests for header stores | Alieh Saeedi | Patch Available | 2026-04-23 |
| KAFKA-20395 | Support unregistering controllers | Kevin Wu | Open | 2026-05-20 |
| KAFKA-20356 | Make cluster id in-memory threadsafe | Kevin Wu | Open | 2026-03-25 |
| KAFKA-20329 | Test headers dsl.store.format further | Alieh Saeedi | In Progress | 2026-05-01 |
| KAFKA-20324 | Update docs to reflect relaxed formatting requirements | Kevin Wu | Open | 2026-03-17 |

*60 total — see `16_other_anomalies.csv` for full list.*
