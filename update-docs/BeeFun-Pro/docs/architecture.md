# Architecture

BeeFun Pro is a native iOS app written in Swift 5. The source lives under `BeeFun/BeeFun/`.

## Layer breakdown

```
BeeFun/BeeFun/
├── AppDelegate.swift       — app entry point; sets up window, tab bar, notifications
├── Model/                  — data models (repos, users, events, issues, gists, trending)
├── View/                   — UIViewControllers and UIViews, grouped by feature
├── SystemManager/          — singletons and helpers (network, OAuth, push, storage, config)
├── ToolKit/                — generic Swift/ObjC utilities not tied to the app domain
├── Resources/              — localisation strings, plists, cert files, images
├── Assets.xcassets/        — all image assets
└── ThirdParty/             — manually bundled SDKs (MobSDK/ShareSDK, UMMobClick)
```

CocoaPods-managed dependencies live in `BeeFun/Pods/` (not tracked).

## App startup

1. `AppDelegate.application(_:didFinishLaunchingWithOptions:)` calls `BFLanunchManager.shared.application(_:didFinishLaunchingWithOptions:)` which registers third-party SDKs (JPush, analytics, etc.)
2. A `UIWindow` is set up with `BFBaseTabBarController` as the root view controller.
3. The tab bar hosts the main feature screens.

## GitHub OAuth flow

- `OAuthManager` + `OAuthGithubWebController` implement the GitHub OAuth2 web flow using `OAuthSwift`.
- The OAuth callback URL is `beefunios://www.beefun.top` (registered in `Info.plist` and `BFThirdLibKey.swift`).
- `AppDelegate.applicationHandle(url:)` passes incoming URLs to `OAuthSwift.handle(url:)`.
- The resulting access token is stored in `UserDefaults` via `AppToken.shared`.

## Networking

Two separate API layers exist:

### GitHub API (`GitHubAPI.swift`)
- All GitHub API calls go through `Moya` on top of `Alamofire`.
- `GitHubAPI` (a Moya `TargetType`) enumerates all endpoints: user info, repos, starring, notifications, watching, forks.
- `Provider.sharedProvider` is the app-wide Moya provider instance.
- Supplementary API files: `EventAPI.swift`, `IssueAPI.swift`, `SearchAPI.swift`.
- Base URL: `https://api.github.com`

### BeeFun Backend API (`BeeFunAPI.swift`)
- A second Moya-based API layer talks to the BeeFun backend server at `https://www.beefun.top:8082/beefun` (currently offline).
- Handles server-side DB sync, tag management, language lists, and trending data.
- `BeeFunProvider.sharedProvider` is the provider instance.
- `BeeFunDBManager` coordinates periodic sync of starred repos to the backend.

### Other networking
- `TrendingManager.swift` scrapes `https://github.com/trending` HTML via Kanna to extract trending repos, developers, and showcases.
- `BFNetworkManager.swift` monitors network reachability (via `ReachabilitySwift`) and provides cookie/cache clearing utilities.
- `IdentityAndTrust.swift` handles SSL certificate pinning via PKCS12 extraction.
- `SVGProcessor.swift` (currently commented out) was intended to render SVG images in repository pages via Kingfisher.

## State and storage

- `SQLManager` provides a SQLite-backed store (via `SQLite.swift`) with a `github.sqlite3` database.
- `SQLStars` and `SQLTags` manage the starred-repos and tags tables respectively.
- `AppToken` reads/writes the GitHub access token in `UserDefaults`.
- `BFLanunchManager` initialises all third-party SDKs once at launch.

## Key feature modules (View/)

| Directory | Feature |
|---|---|
| `View/Trending/`, `View/NewTrending/` | Trending repository discovery |
| `View/Repository/` | Repository detail and file browsing |
| `View/User/` | User profile and followers/following |
| `View/Stars/`, `View/Tag/` | Starred repos and custom tags |
| `View/Notification/` | GitHub notification feed |
| `View/Event/` | Activity event feed |
| `View/Issue/` | Issues browser |
| `View/Gist/` | Gist browser |
| `View/Search/` | Search across repos, users, code, commits, issues, wikis |
| `View/Profile/` | Logged-in user profile, settings, feedback, sync |
| `View/Message/` | In-app push/local notification UI |

## Third-party SDKs (Podfile)

| Pod | Purpose |
|---|---|
| Alamofire | HTTP client |
| Moya | API abstraction layer |
| OAuthSwift | GitHub OAuth2 |
| Kingfisher | Image downloading/caching |
| SnapKit | Auto Layout DSL |
| ObjectMapper | JSON model mapping |
| SwiftyJSON | JSON access |
| Kanna | HTML/XML parsing (trending page scraping) |
| SQLite.swift | Structured local storage |
| MJRefresh | Pull-to-refresh |
| MBProgressHUD | Loading indicators |
| SkeletonView | Skeleton loading UI |
| SwiftMessages | Banner alerts |
| JPush | Push notifications |
| SwiftyStoreKit | In-app purchase |
| Crashlytics / Fabric | Crash reporting |
| SwiftyBeaver | Structured logging |
| SwiftDate | Date utilities |
| YYText | Rich text rendering |
| iCarousel | Carousel UI |
| SwipeCellKit | Swipe cell actions |
| ReachabilitySwift | Network reachability |
| IQKeyboardManagerSwift | Keyboard management |
| HMSegmentedControl | Segmented control UI |
| TOWebViewController | Web view controller |
| SwiftLint | Code style linting |

## Fastlane

`BeeFun/fastlane/` contains the deployment pipeline:
- `Fastfile` — lane definitions (test, beta via TestFlight, deploy to App Store)
- `Deliverfile` — App Store metadata delivery config
- `Gymfile` — build settings
- `Matchfile` — code signing via match
- `metadata/` — App Store text, screenshots, and review credentials
