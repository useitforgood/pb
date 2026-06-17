# GitHunt

React app and Chrome extension to browse the most-starred GitHub repositories by time period and language.

## What it does

- Fetches trending repos from the GitHub Search API grouped by day / week / month
- Infinite scroll backwards in time via "Load next" button
- Filter by programming language (selection persisted across sessions)
- List and grid view modes
- Optional GitHub token to avoid rate limits
- State cached in localStorage for 1 hour

## Setup

See [docs/setup.md](docs/setup.md) for install, build, and deploy instructions.

```bash
yarn install
yarn start          # dev server at localhost:3000
yarn build-chrome   # production build for Chrome extension
yarn build-web      # production build for GitHub Pages
```

## Architecture

See [docs/architecture.md](docs/architecture.md) for component tree and data flow.

See [docs/state.md](docs/state.md) for Redux state shape, actions, and persistence behavior.

## Links

- [Chrome Web Store](https://bit.ly/githunt-chrome)
- [Web version](https://kamranahmed.info/githunt)
- [GitHub API — Search Repositories](https://docs.github.com/en/rest/search)

## License

MIT © Kamran Ahmed
