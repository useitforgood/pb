# Issues

_Last checked: 2026-06-18_

## Info
- **[I1] Unresolved @todo in router** — `src/router/index.js:9` contains `@todo use browser router and generate prerendered options.html page for chrome extension`. The current `MemoryRouter` means the extension gets no shareable URLs and no pre-rendered `options.html` page. To fix: replace `MemoryRouter` with `BrowserRouter` for the web build (gate with an env variable), and add a second webpack entry point that pre-renders `options.html` so the Chrome extension can load it directly.
