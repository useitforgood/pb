# Redux State

Persist key: `githunt:root` (localStorage).

## State shape

```js
{
  github: {
    processing: false,        // true while API call is in flight
    repositories: [           // array of fetched groups, one per date range loaded
      {
        start: "2024-01-01T00:00:00+00:00",
        end:   "2024-01-08T00:00:00+00:00",
        data:  { items: [...] }   // raw GitHub Search API response
      }
    ],
    error: null               // string error message, or null
  },
  preference: {
    viewType: 'list',         // 'list' | 'grid'
    dateJump: 'week',         // 'day' | 'week' | 'month'
    language: '',             // GitHub language string, e.g. 'JavaScript'
    options: {
      token: ''               // GitHub personal access token
    }
  }
}
```

## github slice

**Actions** (`src/redux/github/actions.js`):

| Action | Triggered by |
|---|---|
| `PROCESS_FETCH_TRENDING` | Start of `fetchTrending` thunk |
| `FETCH_TRENDING_SUCCESS` | Successful API response |
| `FETCH_TRENDING_FAILED` | API error |

**Reducer** (`src/redux/github/reducer.js`):
- `UPDATE_LANGUAGE` and `UPDATE_DATE_TYPE` (from preference slice) reset the github slice to its initial state, clearing all loaded repositories.

**Persistence transform** (`src/redux/github/transform.js`):
- On write to storage: keeps only the first repository group (to avoid overflowing localStorage). Clears `processing` and `error` so a stale loading state is never restored.
- Cache TTL: **1 hour** (configured in `store.js` via `redux-persist-expire`). After expiry, `github` resets to `initialState` and data is re-fetched on next load.

## preference slice

**Actions** (`src/redux/preference/actions.js`):

| Action creator | Dispatches | Effect |
|---|---|---|
| `updateOptions(options)` | `UPDATE_OPTIONS` | Saves token |
| `updateViewType(viewType)` | `UPDATE_VIEW_TYPE` | Switches list/grid |
| `updateLanguage(language)` | `UPDATE_LANGUAGE` | Changes language filter; also resets github slice |
| `updateDateJump(dateJump)` | `UPDATE_DATE_TYPE` | Changes time period; also resets github slice |

Preference state is persisted indefinitely (no expiry).
