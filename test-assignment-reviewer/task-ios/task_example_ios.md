# Test Task: iOS Developer — Air Ticket Price Aggregator

## Overview

You are tasked with building a mobile price aggregator application for plane tickets.
The app fetches live offer data from a REST API and presents it through a clean,
Figma-accurate interface built entirely in SwiftUI. This task is designed to assess
your ability to architect a production-ready iOS application, integrate external
dependencies, and deliver polished UI from a design specification.

---

## Tech Stack

All of the following are mandatory. Submissions using alternative tools will not
be reviewed.

| Area | Required |
|---|---|
| Language | Swift 5.9+ |
| UI Framework | SwiftUI |
| Architecture | MVVM + Coordinator |
| Dependency Manager | Swift Package Manager (SPM) |
| Networking | Alamofire |
| Linting | SwiftLint (with custom `.swiftlint.yml`) |
| CI/CD | Xcode Cloud |
| Version Control | Git-Flow (feature branches, no direct commits to main) |
| Minimum Target | iOS 16.0 |

---

## Application Structure

The app must use a tab bar with 4 tabs. Tab 1 is fully required. Tabs 2–4
are structural stubs prepared for future development.

### Tab 1 — Air Tickets (required)

This is the primary screen of the application and must be fully implemented.

**Search Form**
- Two text input fields: departure city and destination city
- Input validation: fields must not be empty before triggering search
- A swap button to reverse origin and destination
- On submit, transition to the results list

**Country/City Search Sheet**
- Triggered when the user taps either input field
- Presented as a bottom sheet (`.sheet` or custom overlay)
- Contains a search field with real-time filtering
- Displays a scrollable list of matching cities/countries
- Selection fills the corresponding input field and dismisses the sheet

**Ticket Offers List**
- Fetches data from the provided mock API on screen load
- Each list item must display:
  - Airline logo (image from API or local asset fallback)
  - Flight price (formatted with currency symbol)
  - Departure and arrival times
  - Flight duration and number of transfers
  - A visual badge for "direct flight" where applicable
- List must support pull-to-refresh
- Loading state: show a skeleton or activity indicator while fetching
- Empty state: show a message if no results are returned
- Error state: show a retry button if the network request fails

### Tab 2 — Hotels (stub)
- Placeholder screen with tab icon and title
- Architecture wired up and ready for future implementation

### Tab 3 — Shorter (stub)
- Placeholder screen with tab icon and title

### Tab 4 — Profile (stub)
- Placeholder screen with tab icon and title

---

## API

Use the following mock endpoints. Do not hardcode response data — all content
must be fetched at runtime.

Your networking layer must:
- Use Alamofire for all HTTP requests
- Decode responses using `Codable`
- Handle HTTP errors (4xx, 5xx) explicitly
- Handle no-internet scenarios with user-facing feedback

---

## Architecture Requirements

**MVVM**
- Views must contain no business logic
- ViewModels expose state via `@Published` properties
- Data flow must be unidirectional

**Coordinator**
- All navigation must go through Coordinators
- No `NavigationLink` with direct destination instantiation in Views
- Each tab should have its own Coordinator

**Dependency Injection**
- ViewModels must receive their dependencies via initializer injection
- No singletons for testable components

---

## Design

Figma layouts will be provided separately upon task acceptance. Your implementation
must be pixel-accurate: correct fonts, spacing, colors, corner radii, and icon sizes.

- Use SF Symbols where specified in the design
- All colors must be defined in the asset catalog (no hardcoded hex values in code)
- Support both light and dark mode if specified in Figma

---

## Code Quality

- SwiftLint must be integrated and passing with zero warnings on build
- No force unwraps (`!`) anywhere in production code
- No `print()` statements in submitted code
- All public types and functions must have documentation comments

---

## Localization

- The app must support Russian (`ru`) as the primary locale
- All user-facing strings must use `NSLocalizedString` or `.localized` extension
- No hardcoded strings in Views or ViewModels

---

## Version Control

Follow Git-Flow strictly:
- `main` — stable, production-ready code only
- `develop` — integration branch
- `feature/xxx` — one branch per feature
- Commit messages must be descriptive and in English
- No merge commits without a corresponding feature branch

---

## Evaluation Criteria

Your submission will be assessed across the following dimensions:

| Criterion | Weight |
|---|---|
| Feature completeness | High |
| Architecture correctness (MVVM + Coordinator) | High |
| Code quality and SwiftLint compliance | Medium |
| Error and edge case handling | Medium |
| UI accuracy vs Figma | Medium |
| Test coverage | Low (bonus) |
| Git history quality | Low |

---

## Deliverable

- Public GitHub repository
- Clean Git-Flow history
- README with: setup instructions, architecture overview, known limitations
- Estimated completion time: 20–30 hours

Submissions without a README or with a single "initial commit" will not be reviewed.


