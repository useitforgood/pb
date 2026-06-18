# Setup

## Requirements

- macOS with Xcode 15 or later
- iOS 18.0 SDK (deployment target: iOS 12.0)
- [CocoaPods](https://cocoapods.org/) (`gem install cocoapods`)
- Ruby (for CocoaPods and Fastlane)
- [Fastlane](https://fastlane.tools/) — optional, only needed for deployment

## Install

```bash
cd BeeFun
pod install
open BeeFun.xcworkspace   # always use the workspace, not .xcodeproj
```

## Configuration

All third-party SDK keys are declared in `BeeFun/BeeFun/SystemManager/ProConfig/BFThirdLibKey.swift`. The file is currently tracked with empty strings; fill in the values before building a release.

| Constant | Service | Where to get it |
|---|---|---|
| `GithubAppClientId` | GitHub OAuth App | github.com → Settings → Developer settings → OAuth Apps |
| `GithubAppClientSecret` | GitHub OAuth App | Same as above |
| `GithubAppRedirectUrl` | GitHub OAuth callback | Must match the URL registered in the OAuth App (`beefunios://www.beefun.top`) |
| `JPushAppKey` | JPush (push notifications) | console.jiguang.cn |
| `JPushAppSecret` | JPush | Same as above |
| `WeiboSDKAppKey` / `WeiboSDKAppSecret` | Sina Weibo sharing | open.weibo.com |
| `WeiXinSDKAppID` / `WeiXinSDKAppSecret` | WeChat sharing | open.weixin.qq.com |
| `TencentSDKAppID` / `TencentSDKAppKey` | QQ sharing | open.qq.com |
| `ShareSDKAppKey` / `ShareSDKAppSecret` | MobSDK / ShareSDK | mob.com |
| `FackbookSDKAppID` / `FackbookSDKAppSecret` | Facebook sharing | developers.facebook.com |
| `TwitterSDKConsumerKey` / `TwitterSDKConsumerSecret` | Twitter sharing | developer.twitter.com |
| `UMengAppSecret` | UMeng analytics | umeng.com |
| `TencentBuglyAppID` | Bugly crash reporting | bugly.qq.com |
| `DingTalkSDKAppID` / `DingTalkSDKAppSecret` | DingTalk sharing | open.dingtalk.com |
| `LinkedInSDKAppID` / `LinkedInSDKAppSecret` | LinkedIn sharing | developer.linkedin.com |
| `YDNoteSDKConsumerKey` / `YDNoteSDKConsumerSecret` | Youdao Note | note.youdao.com |
| `APNsAuthKeyID` | APNs push auth key | developer.apple.com |
| `AppleAppID` | Apple App ID | developer.apple.com |

Keys for unused social platforms can be left empty — the relevant share targets simply won't initialise.

## Build and run

```bash
# Open workspace after pod install
open BeeFun.xcworkspace
```

Select the `BeeFun` scheme and a simulator or device, then press Run (Cmd+R).

Build configurations:
- `Debug` — development
- `Release` — production

Xcode 16 note: The `post_install` hook in `Podfile` sets `SWIFT_ENABLE_EXPLICIT_MODULES = NO` globally to prevent build failures in Kanna/libxmlKanna.

## External services

| Service | Base URL | Auth | Used by |
|---|---|---|---|
| GitHub REST API v3 | `https://api.github.com` | OAuth2 bearer token (stored in UserDefaults via `AppToken`) | `GitHubAPI.swift`, `EventAPI.swift`, `IssueAPI.swift`, `SearchAPI.swift` |
| GitHub OAuth | `https://github.com/login/oauth/authorize` | Client ID + secret from `BFThirdLibKey.swift` | `OAuthManager.swift` |
| GitHub Trending (scrape) | `https://github.com/trending` | None (HTML scraping via Kanna) | `TrendingManager.swift` |
| BeeFun Backend | `https://www.beefun.top:8082/beefun` | GitHub OAuth token forwarded as `Authorization` header | `BeeFunAPI.swift`, `BeeFunDBManager.swift` |
| JPush | jiguang.cn | App key from `BFThirdLibKey.swift` | `JPushManager.swift` |
| Crashlytics | firebase.google.com | Fabric API key (in `GoogleService-Info.plist` or legacy `Fabric.framework`) | `AppDelegate` via Fabric SDK |
| UMeng Analytics | umeng.com | App key from `BFThirdLibKey.swift` | `BFLanunchManager.swift` via `MobClick` |

## Deployment (Fastlane)

```bash
cd BeeFun
bundle exec fastlane <lane>
```

Available lanes: `test` (run tests), `beta` (TestFlight), `deploy` (App Store).

Review credentials for the App Store review sandbox account are in `BeeFun/fastlane/metadata/review_information/`. These should not contain real developer credentials — use a dedicated Apple ID test account.

```bash
# Build for App Store
bundle exec fastlane gym

# Upload metadata and binary
bundle exec fastlane deliver
```
