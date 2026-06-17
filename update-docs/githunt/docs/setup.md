# Setup

## Requirements

- Node.js (any LTS version supported by `react-scripts` 3.x, i.e. Node 10–14 recommended)
- Yarn or npm

## Install

```bash
yarn install
# or
npm install
```

## Run (development)

```bash
yarn start
```

Opens at `http://localhost:3000`. Hot reload enabled.

## Build

**Chrome extension:**
```bash
yarn build-chrome
```
Sets `INLINE_RUNTIME_CHUNK=false` (required for Chrome CSP). Output in `build/`. Load `build/` as an unpacked extension in `chrome://extensions`.

**Web app (GitHub Pages):**
```bash
yarn build-web
```
Sets `PUBLIC_URL=/githunt`. Output in `build/`.

**Deploy to GitHub Pages:**
```bash
yarn gh-pages
```

## External services

| Service | Used by | Auth |
|---|---|---|
| GitHub Search API (`https://api.github.com/search/repositories`) | `src/redux/github/actions.js` | Optional — GitHub personal access token. Without it, unauthenticated rate limit applies (10 req/min). Set via the Options page inside the app. |

## Configuration

No config files or environment variables required to run. The GitHub token is entered by the user inside the app (Options page) and saved to `localStorage` via redux-persist.

## Dependencies (key)

| Package | Purpose |
|---|---|
| `react`, `react-dom` | UI |
| `redux`, `react-redux`, `redux-thunk` | State management |
| `redux-persist`, `redux-persist-expire` | localStorage persistence with 1h TTL on github slice |
| `axios` | GitHub API calls |
| `moment` | Date range computation |
| `react-router`, `react-router-dom` | In-app routing (MemoryRouter) |
| `bootstrap`, `reactstrap` | UI components and grid |
| `github-colors` | Language badge colors |
