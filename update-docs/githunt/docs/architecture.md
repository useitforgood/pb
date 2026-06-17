# Architecture

GitHunt is a React + Redux single-page app that runs both as a web app and a Chrome extension (new-tab replacement).

## Entry point

`src/index.js` mounts `<App/>` into `#root`.

`src/app.js` wraps the entire tree in two providers:
- `<Provider store={store}>` — makes Redux state available everywhere
- `<PersistGate loading={<Launcher/>}>` — holds rendering until persisted state is rehydrated from localStorage; shows a loading spinner in the meantime

## Routing

`src/router/index.js` uses `MemoryRouter` (not `BrowserRouter`) so routing works inside the Chrome extension without a real URL bar.

| Route | Component |
|---|---|
| `/` | `FeedContainer` |
| `/options` | `OptionsContainer` |
| (fallback) | `FeedContainer` |

## Containers

**`src/containers/feed/index.js`**

Main view. On mount, checks if repositories are already loaded in Redux state. If not, calls `fetchTrending`. On filter change (language or dateJump), resets and re-fetches.

Pagination works by appending groups: each call to "Load next week/month/day" computes the next date range starting from the `start` of the last loaded group and going one `dateJump` period further back in time.

Renders either `<RepositoryList>` or `<RepositoryGrid>` depending on `preference.viewType`.

Shows a warning banner if no GitHub token is set (rate limit risk). Shows an error banner on API failure with a special message for invalid tokens.

**`src/containers/options/index.js`**

Single-field form for saving a GitHub personal access token. Delegates to `<OptionsForm>` component; dispatches `updateOptions` on save.

## Component tree (abbreviated)

```
App
└── AppRoutes
    ├── FeedContainer
    │   ├── TopNav
    │   ├── Alert (warning / error)
    │   ├── GroupHeading
    │   ├── Filters
    │   │   ├── LanguageFilter
    │   │   ├── DateJumpFilter
    │   │   └── ViewFilter
    │   ├── RepositoryList / RepositoryGrid
    │   └── Loader
    └── OptionsContainer
        └── OptionsForm
```

## Data flow

1. User opens the app or changes a filter
2. `FeedContainer` calls `fetchTrending(filters)` (thunk)
3. Thunk dispatches `PROCESS_FETCH_TRENDING` → sets `github.processing = true`
4. Axios calls `https://api.github.com/search/repositories` with date range + optional language + optional token
5. On success: dispatches `FETCH_TRENDING_SUCCESS` → appends `{start, end, data[]}` to `github.repositories`
6. On error: dispatches `FETCH_TRENDING_FAILED` → sets `github.error`
7. Redux-persist writes state to localStorage; the github slice expires after 1 hour
