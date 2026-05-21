# Test Assignment Review — Frontend Angular Developer
**Candidate repo:** https://github.com/sharcty/CelebrateIt  
**Task:** Public Holidays Explorer — Angular SPA  
**Date:** 2026-05-21  
**Reviewer:** Claude Code (automated structured review)

---

## VERDICT

**NO HIRE**

> This submission is an automatic disqualification under the task's own rules: *"Submissions that do not include NgRx or use a different state management approach will not be reviewed."* The candidate replaced NgRx with plain RxJS observables injected directly into components — there is no Store, no Effects, no Selectors, and no Actions anywhere in the codebase. Beyond the NgRx violation, the implementation is missing an entire major feature (Favourites), uses Angular Material instead of the required PrimeNG/NGX-Bootstrap, runs tests with Karma/Jasmine instead of Jest, has no lazy loading, no HTTP interceptors, no CSV export, no skeleton loaders, no country flags, no timeline view, and no breadcrumb navigation. Meaningful feature completion sits at roughly 30%.

**Overall Score: 13 / 60**

| Signal | Status |
|--------|--------|
| Task completion | ❌ Missing |
| Stack compliance | ❌ Missing |
| Architecture | ❌ Missing |
| Code quality | ⚠️ Acceptable |
| Error handling | ❌ Absent |
| Tests | ❌ Absent |

---

## DETAILED SCORES

| Criterion | Score | Justification |
|-----------|-------|---------------|
| Task Completion | 2/10 | Of 4 major feature areas, only fragments of 3 are present. Home shows 3 *random* holidays (not the required 10 upcoming sorted by date). Search navigates to a country page but has no holiday browser inline, no type filter, no CSV export. Country detail shows a list of holidays but has no country name, no flag, no total count, no timeline, no next-holiday highlight, and no breadcrumb. The Favourites screen is completely absent — no bookmark icons, no localStorage logic, no dedicated tab. |
| Stack & Tool Compliance | 2/10 | Angular 19 ✓ (satisfies 17+ requirement). TypeScript 5.7 ✓. SCSS ✓. ESLint + Prettier ✓. Every other mandatory tool is violated: Angular Material is used instead of PrimeNG or NGX-Bootstrap; NgRx is fully absent; the test runner is Karma/Jasmine, not Jest (despite `@types/jest` appearing as a stray devDependency); HTTP interceptors are absent. The task stated these substitutions are not permitted. |
| Architecture & Structure | 2/10 | No NgRx Store, Effects, Selectors, or Actions. HTTP calls are made inside components via direct observable subscriptions (`ngOnInit` calling service methods and assigning to `$` properties). No lazy-loaded feature modules — `HomeComponent` and `CountryPageComponent` are directly imported in `app.routes.ts`. No SharedModule. The single `CelebratingService` covers all HTTP concerns but is not named `HolidayService` and has no interceptor layer. The router only defines 2 routes (Home and Country), with Search not having its own route at all. |
| Code Quality & Readability | 4/10 | The code is readable and modestly structured. Component files are concise. However: all HTTP calls use `get<any>` (explicit `any` violation against the "No any types" rule); `CountryPageComponent` imports `ɵInternalFormsSharedModule`, a private Angular API marked with the `ɵ` prefix that is not part of the public API surface; mobile detection uses a one-time `window.innerWidth` check with no resize listener; the `CelebratingService.getRandomHolidays` shuffles data randomly on each call, which is incorrect for a "next upcoming holidays" requirement. |
| Error & Edge Case Handling | 2/10 | `getHolidays` and `getAllCountries` have `catchError` that returns `of([])` and logs to `console.error`. `getRandomHolidays` (the home screen's primary call) has no error handling at all. There are no HTTP interceptors for global error dispatching, no user-facing error messages, no retry logic, and no empty-state handling in templates. |
| Tests & Quality Assurance | 1/10 | All four spec files contain only the auto-generated scaffold test (`should create`). No behavioral assertions exist. The test framework is Karma/Jasmine, not Jest as required. There are no tests for reducers or selectors (because they don't exist), no service tests, and no coverage measurement. The `@types/jest` devDependency is present but unused. Meaningful test coverage is effectively 0%. |
| **Total** | **13/60** | |

---

## TASK vs IMPLEMENTATION — LINE BY LINE

| Requirement | Required | Implemented | Gap |
|-------------|----------|-------------|-----|
| Framework | Angular 17+ | Angular 19 | ✅ |
| UI Library | PrimeNG or NGX-Bootstrap | Angular Material | ❌ |
| Language | TypeScript 5.x strict, no `any` | TypeScript 5.7, `any` used in all HTTP calls | ⚠️ |
| Styling | SCSS | SCSS | ✅ |
| State management | NgRx Store + Effects | None — plain RxJS in components | ❌ |
| Routing | Lazy-loaded feature modules | Eager-loaded standalone components | ❌ |
| Forms | Angular Reactive Forms | ReactiveFormsModule used in Search and Country | ✅ |
| HTTP | HttpClient + interceptors | HttpClient only, no interceptors | ⚠️ |
| Linting | ESLint + Prettier, zero warnings | ESLint + Prettier configured | ✅ |
| Testing | Jest, 60%+ coverage | Karma/Jasmine, scaffold tests only | ❌ |
| Home: 10 upcoming holidays | `NextPublicHolidaysWorldwide`, 10 items sorted by date | 3 *randomly shuffled* items from same endpoint | ❌ |
| Home: country flag per card | Flag on each card | No flag | ❌ |
| Home: holiday name, local name, date, country name | All four fields | Name, date, country name only (no `localName`) | ⚠️ |
| Home: refresh button | Manual re-fetch button | Absent | ❌ |
| Home: skeleton loading | Skeleton cards while loading | Absent | ❌ |
| Search: autocomplete country field | From `/AvailableCountries` | Present — Material Autocomplete | ✅ |
| Search: year selector ±5 | Segmented control or stepper | Present — toggle group (desktop) / select (mobile) | ✅ |
| Search: holiday list inline | Display after country + year | Navigates to country detail page instead | ⚠️ |
| Search: type badge per holiday | Public / Bank / Optional badge | Types shown as plain text on country page | ⚠️ |
| Search: filter bar by type | Checkbox or toggle filter | Absent | ❌ |
| Search: CSV export | Download current list as `.csv` | Absent | ❌ |
| Country Detail: country name + flag + code | All three | Code only, no name, no flag | ❌ |
| Country Detail: total holiday count | Count for selected year | Absent | ❌ |
| Country Detail: timeline view | Months-based timeline | Absent — plain `<mat-list>` | ❌ |
| Country Detail: next upcoming holiday highlighted | Highlighted at top | Absent | ❌ |
| Country Detail: breadcrumb navigation | Breadcrumb back to search | Absent | ❌ |
| Favourites: bookmark icon | On each card/row | Absent | ❌ |
| Favourites: localStorage | Persist bookmarks | Absent | ❌ |
| Favourites: dedicated tab | Separate favourites screen | Absent | ❌ |
| Favourites: remove / clear all | Individual + bulk remove | Absent | ❌ |
| NgRx global store | countries, holidays, favourites, loading/error | Absent | ❌ |
| NgRx Effects | All HTTP via Effects | Absent | ❌ |
| NgRx Selectors | All template data access via selectors | Absent | ❌ |
| Action naming | `[Source] Event` convention | Absent | ❌ |
| HTTP interceptor: loading spinner | Global show/hide | Absent | ❌ |
| HTTP interceptor: error → store dispatch | Error actions | Absent | ❌ |
| HolidayService | Dedicated service for HTTP | Present as `CelebratingService` | ⚠️ |
| Model files | Interfaces in `.model.ts` | Interfaces in `core/models/*.ts` (not `.model.ts` suffix) | ⚠️ |
| README: setup instructions | `npm install && ng serve` flow | Present, though clone URL is a placeholder | ⚠️ |
| README: architecture decisions | Documented | Absent | ❌ |
| README: known limitations | Documented | Absent | ❌ |
| Git: multiple commits | More than one commit | 14 commits | ✅ |
| No console errors | Clean browser console | `catchError` silently swallows errors to console | ⚠️ |

---

## STRENGTHS

- **Responsive year selector** (`country-page.component.ts:35-53`): Detects screen width and switches between a `MatButtonToggleGroup` (desktop) and a `MatSelect` (mobile) — a practical UX detail not explicitly required by the task.
- **Proper RxJS lifecycle management** (`country-page.component.ts`): Uses `Subject`/`takeUntil` pattern correctly to unsubscribe on destroy, avoiding memory leaks.
- **Typed model interfaces exist** (`src/app/core/models/country.ts`, `holiday.ts`): Even though they are not placed in `.model.ts`-suffixed files, having them in a `core/models/` directory shows structural awareness.
- **Autocomplete is functional** (`search.component.ts`): The `valueChanges → switchMap → filter` RxJS chain for autocomplete filtering is correctly implemented and avoids redundant HTTP calls.
- **ESLint + Prettier are wired up**: Config files are present and the project follows consistent formatting throughout.

---

## RED FLAGS

- **NgRx completely absent** — The task explicitly disqualifies submissions without it. There is no `@ngrx` package anywhere in `package.json`. This is a **dealbreaker**, not a coachable gap for this role and this task.
- **`ɵInternalFormsSharedModule` imported in `country-page.component.ts:16`** — This is a private Angular internal API (prefixed `ɵ`). Using it is fragile, undocumented, and could break on any patch version update. This is a **red flag about Angular knowledge depth** — likely a StackOverflow copy-paste fix rather than understanding the root issue. Coachable but concerning.
- **Home screen shows random data instead of required data** (`celebrating.service.ts:20-30`): `getRandomHolidays` Fisher-Yates shuffles the worldwide holidays and returns a random 3. The requirement is the next 10 upcoming holidays sorted by date ascending. This is not a simplification — it's a fundamentally wrong implementation of the core home screen. **Dealbreaker at this level of seniority.**
- **Zero meaningful tests**: All spec files contain only the auto-generated `should create` test. The task requires Jest, NgRx reducer/selector tests, and 60% coverage minimum. Using Karma/Jasmine and writing nothing is not a gap — it's a skip. **Dealbreaker for this task's requirements.**
- **Entire Favourites feature absent**: No bookmark icons, no localStorage, no dedicated screen. This is a complete feature omission, not a partial one. Given the estimated 16-24h scope, this suggests either time management failure or deprioritization without disclosure. **Coachable but significant.**

---

## DEVIATIONS & ALTERNATIVE APPROACHES

**What the TD asked for: PrimeNG or NGX-Bootstrap**  
The candidate chose Angular Material instead. Material is a mature, well-supported UI library and in many ways a reasonable default for Angular projects. However, the task explicitly said "Do not substitute any of these tools" and listed PrimeNG and NGX-Bootstrap as the two permitted choices. This is not a superior deviation — it is a direct instruction violation. It signals either that the candidate did not read the requirements carefully or chose comfort over compliance.

**What the TD asked for: Lazy-loaded feature modules**  
The candidate used standalone components with eager loading (direct imports in `app.routes.ts`). Standalone components are the modern Angular 17+ pattern, and lazy loading with standalone components is slightly different than with NgModules (`loadComponent` vs `loadChildren`). A case could be made that standalone + `loadComponent` is the more current approach. However, the candidate did not use `loadComponent` either — components are eagerly imported, so this is not a reasonable trade-off, just missing the feature entirely.

**What the TD asked for: Year selector as segmented control or stepper**  
The candidate implemented a `MatButtonToggleGroup` (desktop) with a dropdown fallback (mobile). The toggle group is visually equivalent to a segmented control and the responsive fallback is a positive UX decision. This is a **better-or-equivalent implementation** of the stated requirement.

---

## INTERVIEW QUESTIONS

1. **NgRx gap**: The task required NgRx Store and Effects as mandatory. Your implementation uses plain RxJS observables in components instead. Walk me through what NgRx adds over plain RxJS, and describe a time you've used it — including how you structured actions, effects, and selectors for an async API call.

2. **Private API usage**: `CountryPageComponent` imports `ɵInternalFormsSharedModule`. Why did you import a private Angular API, and what problem were you trying to solve? What is the correct public API to use instead?

3. **Home screen behavior**: The task specifies the home screen should show the *next 10 upcoming holidays worldwide, sorted by date ascending*. Your implementation shows 3 random holidays from a shuffled array. Was this intentional? How would you implement the correct behavior?

4. **Testing**: Your spec files contain only auto-generated `should create` tests. Can you describe how you would write a unit test for an NgRx reducer? What about testing a component that depends on a store selector?

5. **Favourites and time management**: The Favourites feature (localStorage, dedicated tab, bookmark icons) is completely absent. Given the 16-24h estimated time, why was it skipped? How do you approach feature prioritization when you're running short on time?

6. **Error handling strategy**: Your `getRandomHolidays` method (the primary home screen call) has no error handling. What would a production-grade error handling strategy look like for this app, and how would NgRx Effects factor into it?

7. **HTTP interceptors**: The task requires two interceptors — one for global loading state, one for dispatching error actions to the store. Can you describe how you'd implement them and why the task specifically puts these in the interceptor layer rather than inside components or services?

---

## IF NO HIRE — FULL RATIONALE

This submission fails on the two criteria the task explicitly marked as automatic disqualifiers. First, NgRx is entirely absent — `package.json` has no `@ngrx` dependency of any kind. The task states plainly: *"Submissions that do not include NgRx or use a different state management approach will not be reviewed."* This is not a partial or weak NgRx implementation; it is a complete absence, suggesting either the candidate is unfamiliar with NgRx or chose not to invest the time to learn it for this task. For a frontend Angular role where NgRx architecture correctness is listed as a high-weight criterion, this is a fundamental gap, not a coachable one in the hiring context.

Second, the test suite is essentially non-existent. The task requires Jest (the candidate uses Karma/Jasmine), unit tests for all reducers, selectors, and the service, and a 60% minimum coverage floor. The four spec files contain only scaffold `should create` assertions and test nothing about behavior. This is not "minimal testing" — it is no testing. A candidate who cannot or does not write meaningful tests for Angular services and state management layers is not ready for a position where "Unit test coverage: Medium weight" is an explicit criterion.

Beyond the two disqualifiers, approximately 60-65% of specified features are missing: the entire Favourites module, CSV export, skeleton loaders, type filtering, country flags, timeline view, breadcrumb navigation, refresh button, and the home screen's core behavior (sorted upcoming holidays) is implemented incorrectly. The correct submission for this role would be a senior Angular developer. This submission reads closer to a junior-to-mid developer who is comfortable with Angular basics (routing, reactive forms, Material, simple RxJS), has used Angular for production work, but has not worked with state management at scale and is not yet test-driven in their workflow.
