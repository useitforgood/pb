# Test Assignment Review — iOS Developer
**Candidate repo:** https://github.com/roman-sundurov/TicketSearcher  
**Task:** Air Ticket Price Aggregator — iOS SwiftUI App  
**Date:** 2026-05-21  
**Reviewer:** Claude Code (automated structured review)

---

## VERDICT

**MAYBE — INTERVIEW REQUIRED**

> The submission shows real structural maturity — proper Git-Flow history, Alamofire via SPM, a well-configured custom SwiftLint ruleset, active Xcode Cloud CI, and a working app with screenshots. The Coordinator pattern and MVVM scaffolding are in place. However, three explicit task rules are violated in ways that suggest shallow familiarity rather than deep competence: `AirTicketsVM.shared` and `NetworkService.shared` are singletons (the task says "No singletons for testable components"), `print()` statements litter production code (explicitly forbidden), and localization is entirely absent — every user-facing string is a hardcoded Russian literal, with no `NSLocalizedString` usage anywhere. The tests are also non-functional: the async network callbacks never execute during the XCTest run because `XCTestExpectation` is not used. An interview should determine whether these are time-pressure shortcuts the candidate recognizes and can fix, or genuine knowledge gaps.

**Overall Score: 25 / 60**

| Signal | Status |
|--------|--------|
| Task completion | ⚠️ Partial |
| Stack compliance | ⚠️ Partial |
| Architecture | ⚠️ Partial |
| Code quality | ⚠️ Acceptable |
| Error handling | ❌ Absent |
| Tests | ⚠️ Minimal |

---

## DETAILED SCORES

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Task Completion | 5/10 | Tab 1 (Air Tickets) is the most complete: the search form works, the bottom sheet opens on tap, swap button is present, the ticket offers list fetches live data and renders items. However: input validation before search is absent (empty fields don't block navigation), the search sheet shows hardcoded popular destinations (Istanbul/Sochi/Phuket) rather than a real-time API-filtered city list, pull-to-refresh is missing, and loading/empty/error states are absent from all list views. Tabs 2–4 are correctly stubbed. |
| Stack & Tool Compliance | 7/10 | Swift (5.x), SwiftUI, SPM, Alamofire 5.9.1, SwiftLint with a substantial custom config, Xcode Cloud CI (schemes present, README confirms), iOS 16.0 target, Git-Flow — all present. Deductions: the per-tab Coordinator requirement is violated (one global `AppCoordinator` handles all tabs), and the singleton pattern for `AirTicketsVM` and `NetworkService` directly contradicts the "No singletons for testable components" rule. |
| Architecture & Structure | 4/10 | MVVM scaffolding exists: ViewModels expose `@Published` properties, views consume them via `@EnvironmentObject`. However, views contain business logic — input filtering, print-based debug flags, and conditional navigation logic inline. The Coordinator pattern is genuinely implemented (no bare `NavigationLink`, navigation through coordinator methods) but is centralized in a single `AppCoordinator` rather than per-tab as required. `AirTicketsVM.shared` singleton is injected as an environment object, which makes the ViewModel non-injectable and non-testable in isolation. |
| Code Quality & Readability | 4/10 | Models use proper `CodingKeys` for snake_case mapping, colors are defined in the asset catalog, and the SwiftLint config is thorough. However: `print()` statements appear in at least 8 places across production files (explicitly forbidden); documentation comments are sparse — only a few one-liners on NetworkService methods; `@Environment(\.presentationMode)` is declared but unused in `AirTicketsCountryView`; commented-out `TextField` code remains in `AirTicketsStartView`. No `NSLocalizedString` usage anywhere despite the Russian localization requirement. |
| Error & Edge Case Handling | 3/10 | `NetworkService` methods propagate `AFError` via completion callbacks, and ViewModels set `errorMessage: String?` on failure. However, no view reads or displays `errorMessage` — error state is silently swallowed. There is no retry button, no empty-state view, no offline/no-internet user-facing feedback, and no loading indicator while requests are in-flight. |
| Tests & Quality Assurance | 2/10 | Three unit tests exist for network calls — which is more than nothing. But all three are broken: they use synchronous `throws` functions with async `AF.request` completions. Because `XCTestExpectation` is never used, the test function returns before the network callback fires, and `XCTAssert` never executes. All three tests pass trivially and verify nothing. A `testPerformanceExample` stub is also left in. |
| **Total** | **25/60** | |

---

## TASK vs IMPLEMENTATION — LINE BY LINE

| Requirement | Required | Implemented | Gap |
|-------------|----------|-------------|-----|
| Language | Swift 5.9+ | Swift 5.x (Xcode 2024 project) | ✅ |
| UI Framework | SwiftUI | SwiftUI | ✅ |
| Architecture | MVVM + Coordinator | MVVM + single AppCoordinator | ⚠️ |
| Dependency Manager | SPM | SPM (Package.resolved present) | ✅ |
| Networking | Alamofire | Alamofire 5.9.1 via SPM | ✅ |
| Linting | SwiftLint + custom `.swiftlint.yml` | SwiftLint configured, 40+ rules + custom rule | ✅ |
| CI/CD | Xcode Cloud | Xcode Cloud schemes present, confirmed in README | ✅ |
| Version Control | Git-Flow | feature→develop→release→main flow followed | ✅ |
| Minimum Target | iOS 16.0 | iOS 16.0 (lowered from 17.0 in a feature branch) | ✅ |
| Tab bar with 4 tabs | Air Tickets + 3 stubs | 5 tabs (added Notifications not in task) | ⚠️ |
| Tab 2–4 stubs | Placeholder + wired architecture | Present as StubView / dedicated views | ✅ |
| Search form: 2 input fields | Departure + destination | Present, persisted via `@AppStorage` | ✅ |
| Input validation | Fields non-empty before search | Absent — empty fields don't block navigation | ❌ |
| Swap button | Reverse origin ↔ destination | Present in `AirTicketsCountryView`, absent from `AirTicketsStartView` | ⚠️ |
| Transition to results on submit | Navigate to offers list | Navigation happens from sheet selection | ⚠️ |
| Search sheet: triggered on tap | Open on tap of destination field | ✅ — `appCoordinator.activeSheet = .airTicketsSearch` | ✅ |
| Search sheet: bottom sheet | `.sheet` or custom overlay | Custom sheet presented via AppCoordinator | ✅ |
| Search sheet: real-time city filtering | Filter from `/AvailableCountries` | Static popular destinations (Istanbul/Sochi/Phuket) in assets, no API filtering | ❌ |
| Search sheet: scrollable matching list | Live-filtered scrollable list | Hard-coded list in `PopularDestinationsView` | ❌ |
| Search sheet: selection fills field + dismisses | Fill field, dismiss sheet | Selection fills toCity ✓, sheet closes ✓ | ✅ |
| Ticket list: fetches from API on load | Live data, on screen appear | `getDetailedFlightData()` in `onAppear` | ✅ |
| Ticket list: airline logo | Image from API or local fallback | `company`/`providerName` fields decoded; model present | ⚠️ |
| Ticket list: price with currency symbol | Formatted with currency | Added in feature branch ("Added currency symbol") | ✅ |
| Ticket list: departure + arrival times | Both times shown | `FlightDetail.date` decoded, displayed | ✅ |
| Ticket list: duration + transfers | Duration and transfer count | `hasTransfer` field present; duration calculated from dates | ⚠️ |
| Ticket list: direct flight badge | Visual badge | `badge: String?` field in model, `AirTicketDetailView` present | ✅ |
| Ticket list: pull-to-refresh | `.refreshable` modifier | Absent | ❌ |
| Ticket list: loading state | Skeleton or activity indicator | Absent | ❌ |
| Ticket list: empty state | Message if no results | Absent | ❌ |
| Ticket list: error state + retry | Retry button on failure | `errorMessage` set in VM but not shown in UI; no retry button | ❌ |
| MVVM: no business logic in views | Views only render | Filtering logic and conditional state in views | ⚠️ |
| MVVM: @Published state | State via @Published | ✅ in all ViewModels | ✅ |
| MVVM: unidirectional data flow | One direction | `@AppStorage` in ViewModel is shared mutable state, not strictly unidirectional | ⚠️ |
| Coordinator: all navigation via Coordinator | No direct NavigationLink destinations | Navigation through AppCoordinator methods | ✅ |
| Coordinator: per-tab Coordinator | One per tab | Single global AppCoordinator | ❌ |
| DI: initializer injection | Dependencies via init | ViewModels use `.environmentObject` injection ✅, but defaults to `.shared` singleton | ⚠️ |
| DI: no singletons for testable components | No singletons | `AirTicketsVM.shared`, `NetworkService.shared` both singletons | ❌ |
| SwiftLint: zero warnings | 0 warnings on build | Config is solid; `print()` statements may trigger warnings if linting runs | ⚠️ |
| No force unwraps | No `!` in production code | `force_unwrapping` in SwiftLint opt-in; not observed in read files | ✅ |
| No `print()` statements | None in production | Multiple `print()` in NetworkService, AirTicketsStartView, CountrySearchSheet, AirTicketsOptionsView | ❌ |
| Documentation comments | All public types + functions | Sparse — only a few one-liners | ❌ |
| Localization: Russian primary | NSLocalizedString / .localized | Hardcoded Russian strings everywhere; no `.lproj` files, no NSLocalizedString | ❌ |
| No hardcoded strings in views | Use localization | All strings hardcoded | ❌ |
| README: setup instructions | Build/run instructions | TestFlight link provided; no Xcode build instructions | ⚠️ |
| README: architecture overview | Documented | Brief tech stack list | ⚠️ |
| README: known limitations | Documented | Present (notes about clickability, English locale) | ✅ |
| Git-Flow: feature branches | feature/xxx per feature | Followed — visible in merge commit messages | ✅ |
| Git-Flow: no direct commits to main | All via release branches | Followed | ✅ |
| Commit messages: descriptive English | English, descriptive | Mostly good (feat/fix/refactor prefixes) | ✅ |
| Multiple commits | More than one | ~30 commits | ✅ |

---

## STRENGTHS

- **Git-Flow executed correctly** (`Merge branch 'feature/swipe-navigation-in-tabs-screens' into develop`, etc.): The candidate followed the branching model strictly across ~30 commits — feature branches, versioned releases (v0.1.0 → v0.1.2), and proper merges. This is rare discipline in a solo test task and signals production team experience.
- **Thorough SwiftLint configuration** (`.swiftlint.yml`): 40+ opt-in rules enabled, a custom regex rule for array/dictionary initialization, and sensible relaxations (`line_length`, `indentation_width` disabled). This is not a default config — it reflects genuine familiarity with the tool.
- **Model layer is well-structured** (`AirTicketsModel.swift`): All `Codable` types use proper `CodingKeys` for snake_case mapping, `Hashable` conformance is implemented manually, and the model hierarchy matches the API shape cleanly. No `AnyCodable` hacks.
- **Coordinator + NavigationStack integration** (`AppCoordinator.swift`): The `airTicketsTabPath: [NavigationStackScreen]` array driving `NavigationStack` is correct modern SwiftUI navigation — avoids legacy `NavigationView` and `NavigationLink` destination coupling. `getSwipeView` dispatching from `navigationDestination` is the right pattern.
- **Responsive Xcode schemes** (`xcschemes/`): Debug and Release schemes for Russian language are set up, and Xcode Cloud integration is confirmed — showing awareness of the full build/distribute pipeline, not just writing code.

---

## RED FLAGS

- **`AirTicketsVM.shared` and `NetworkService.shared` singletons** (`AirTicketsVM.swift:12`, `NetworkService.swift:11`): The task says explicitly "No singletons for testable components." Both core components are singletons. Worse, the AppCoordinator factories (`airTickesView()`, etc.) all use `AirTicketsVM.shared` directly, bypassing any injection path. This means ViewModel state is globally shared across screens and tests cannot isolate it. **Coachable gap, but a clear violation of a stated requirement.**
- **`print()` statements in production code** (`NetworkService.swift:20,27`, `AirTicketsStartView.swift`, `CountrySearchSheet.swift`, `AirTicketsOptionsView.swift`): The task says "No `print()` statements in submitted code." There are at least 8 `print()` calls across production files, including debug labels like `print("Tap From fromTextField")`. This suggests the code was not cleaned up before submission. **Coachable, but signals incomplete submission hygiene.**
- **Localization entirely absent**: The task mandates `NSLocalizedString` or `.localized` extension, Russian as the primary locale, and no hardcoded strings in Views or ViewModels. There are no `.lproj` files, no `Localizable.strings`, and every user-visible string is a raw Russian literal. The README acknowledges this only for *English* localization, not for the required `NSLocalizedString` architecture. **Dealbreaker if localization is core to the role; coachable gap otherwise.**
- **Network tests are broken** (`TicketSearcherTests.swift`): All three test methods use synchronous `throws` signatures with async `AF.request` callbacks. Without `XCTestExpectation`, the test body exits before the callback fires — `XCTAssert` never runs, and all tests trivially pass. This demonstrates a fundamental misunderstanding of async testing in XCTest. **Coachable, but signals limited testing experience.**
- **No loading / empty / error states in any list view**: The ViewModel has `errorMessage: String?` and the data arrays start empty, but none of the views handle these states — no spinner while fetching, no "no results" message, no retry button. On a slow or failing network the app shows a blank screen with no feedback. **Coachable gap, but a visible UX regression.**

---

## DEVIATIONS & ALTERNATIVE APPROACHES

**What the TD asked for: Per-tab Coordinator**  
The candidate implemented a single `AppCoordinator` that manages all tabs, sheets, and NavigationStack screens. The stated requirement is "Each tab should have its own Coordinator." The single-coordinator approach is actually common in smaller SwiftUI apps and avoids coordinator-to-coordinator communication complexity. However, it centralizes all navigation logic into one 130-line class, which would become unmaintainable at scale. For this task it works, but it directly contradicts the architecture requirement and signals that the candidate may not have built larger multi-module apps where per-feature coordinators are necessary. **Worse than required for this role's architecture signal.**

**What the TD asked for: Initializer injection / no singletons**  
`AirTicketsVM.shared` is passed as an `.environmentObject()`, which is a legitimate SwiftUI DI mechanism. The issue is that the *source* is always `.shared`, making the singleton hard to swap in tests. A candidate who knows the distinction would have used `init(viewModel: AirTicketsVM = AirTicketsVM())` on views and created VMs in the coordinator. The approach chosen works for the app but breaks testability. **Equivalent UX, worse testability.**

**What the TD asked for: Alamofire with explicit 4xx/5xx handling**  
`AF.request(url).validate().responseDecodable(...)` with `.validate()` is the correct Alamofire pattern — `.validate()` promotes 4xx/5xx HTTP codes into `AFError.responseValidationFailed`, which is then caught in the `.failure` branch. This is actually the idiomatic Alamofire approach and satisfies the spirit of the requirement. **Equivalent or better than rolling manual status code checks.**

**What the TD asked for: Russian primary locale via NSLocalizedString**  
The candidate hardcoded Russian strings inline. A better approach would be to create a `Localizable.strings` with a `.localized` String extension. The candidate acknowledges in the README they plan to "add English localization later" — but this misreads the requirement, which is about the *architecture* for localization, not about supporting English. **Worse than required.**

---

## INTERVIEW QUESTIONS

1. **Singleton + DI**: `AirTicketsVM` and `NetworkService` are both singletons. The task explicitly required no singletons for testable components. Was this a time-pressure shortcut or a conscious choice? Walk me through how you'd refactor these to be injectable — specifically, how would the Coordinator create and own ViewModels and inject them via initializer?

2. **Broken async tests**: Your three unit tests use synchronous `throws` functions with `AF.request` completion handlers. Can you explain why these tests always pass regardless of the network response, and what would you use instead to test asynchronous code in XCTest? How would you mock `NetworkService` to avoid hitting a live endpoint?

3. **Localization architecture**: You hardcoded Russian strings throughout all views. The task required `NSLocalizedString`. How would you add localization to a SwiftUI project — where would the strings file live, what extension would you add to `String`, and how would you handle format strings with dynamic values?

4. **Per-tab coordinators**: You implemented a single `AppCoordinator`. The task asked for one Coordinator per tab. When does a per-feature Coordinator architecture become necessary over a centralized one? Can you sketch how you'd split the Air Tickets navigation into its own `AirTicketsCoordinator`?

5. **Missing UI states**: None of the list views show a loading indicator, empty state, or error view with retry. Walk me through how you'd implement these three states in SwiftUI for the `AirTicketsOptionsView`, given that the ViewModel already has `errorMessage: String?`.

6. **`print()` in production**: There are 8+ `print()` calls in production code — explicitly forbidden by the task. How do you handle debug logging in a production iOS app? What would you use instead of `print()`, and how do you enforce no raw `print()` statements at build time (hint: SwiftLint can help here)?

7. **City search sheet**: The `CountrySearchSheet` shows hardcoded popular destinations (Istanbul, Sochi, Phuket from local assets) instead of a live-filtered list from an API. Was this intentional? How would you implement real-time filtering of a country list, and what debounce strategy would you use to avoid excessive API calls while the user types?
