# Architecture

BeeFun Pro is a native iOS app written in Swift 5. It is also packaged as a GitHub iOS client. The source lives under `BeeFun/BeeFun/`.

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

- All GitHub API calls go through `Moya` on top of `Alamofire`.
- `GitHubAPI` (a Moya `TargetType`) enumerates all endpoints.
- `Provider.sharedProvider` is the app-wide Moya provider instance.
- Supplementary API files: `EventAPI.swift`, `IssueAPI.swift`, `SearchAPI.swift`, `TrendingManager.swift`.
- `BFNetworkManager.swift` wraps response handling and error mapping.
- `IdentityAndTrust.swift` handles SSL certificate pinning.
- `SVGProcessor.swift` renders SVG images in repository pages.

## State and storage

- `BeeFunDBManager.swift` provides a SQLite-backed store (via `SQLite.swift`) for persisting starred repositories and tags.
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
| `View/Search/` | Search across repos and users |
| `View/Profile/` | Logged-in user profile |
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
| Kanna | HTML/XML parsing |
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

## Fastlane

`BeeFun/fastlane/` contains the deployment pipeline:
- `Fastfile` — lane definitions
- `Deliverfile` — App Store metadata delivery config
- `Gymfile` — build settings
- `Matchfile` — code signing via match
- `metadata/` — App Store text, screenshots, and review credentials
