# Issues

_Last checked: 2026-06-18_

## Warnings

- **[W1] Credential config file tracked by git** — `BeeFun/BeeFun/SystemManager/ProConfig/BFThirdLibKey.swift` is the master configuration file for 14+ third-party SDK keys (GitHub OAuth client ID/secret, JPush, Weibo, WeChat, Facebook, Twitter, LinkedIn, etc.). All fields are currently empty strings, but the file is tracked: if real keys are ever filled in and committed, they will be permanently in git history. Fix: add this file to `.gitignore`, provide a `BFThirdLibKey.swift.example` template instead, and inject real values via an `.xcconfig` file or CI/CD secrets at build time.

- **[W2] Infer static-analysis artifacts tracked by git** — `BeeFun/infer-out/` (1,200+ files: `.attr`, `.cfg`, `.cg`, `.tenv`, `.specs`) is the output directory of the [Infer](https://fbinfer.com/) static analyzer and should never be committed. It bloats the repository and re-generates on every analysis run. Fix: add `BeeFun/infer-out/` to `.gitignore` and run `git rm -r --cached BeeFun/infer-out/` to stop tracking it.

- **[W3] Fastlane review_information directory not gitignored** — `BeeFun/fastlane/metadata/review_information/` contains App Store review contact details (`first_name.txt`, `last_name.txt`, `phone_number.txt`, `demo_user.txt`, `demo_password.txt`, `email_address.txt`). None are covered by `.gitignore`. Fix: add `BeeFun/fastlane/metadata/review_information/` to `.gitignore` and use `fastlane deliver` environment variables or a `Deliverfile` that reads from the environment for all reviewer contact fields.

## Info

- **[I1] App Store review credentials tracked by git** — `BeeFun/fastlane/metadata/review_information/demo_password.txt` contains `test1234` and `email_address.txt` contains `wenghengcong@icloud.com`. These are in the `review_information` directory (Apple App Store review demo credentials), not production secrets. The password is an obviously test value. Still, best practice is to supply these via environment variables rather than committing them. See W3 for the fix.

- **[I2] TODO/FIXME comments across 11 files** — 16 unresolved markers remain in the source:
  - `SystemManager/Manager/ThirdParty/ShareManager.swift:11` — `TODO: 分享App 到微信收藏总是失败` (WeChat Favorites share always fails)
  - `SystemManager/Manager/ThirdParty/ShareManager.swift:256,267` — two `TODO: 经纬度` (geolocation stubs, not implemented)
  - `SystemManager/Manager/ThirdParty/ShareManager.swift:262` — `TODO: 微博高级API未通过审核` (Weibo advanced API not approved, falls back to text share)
  - `Model/Event/ObjEvent.swift:123` — `TODO: org is organization`
  - `View/Message/BFMessageController.swift:104` — `FIXME: carouselContent layer ordering`
  - `View/User/UserCell/BFUserTypeOneCell.swift:94,140` — two `HCTODO: checkUserFollowed()` (follow-check logic disabled)
  - `View/Profile/BFProfileController+Data.swift:19` — `TODO: 分享的开关暂时关闭` (share toggle disabled)
  - `View/Profile/Funny/BFFunnyLabViewController.swift:56` — `FIXME: 网络重连` (network reconnect not handled)
  - `View/Profile/StarTag/BFListsManageController.swift:36` — `FIXME:` (empty, no description)
  - `ToolKit/JSToolKit/JSFoundation/NSString+Size.swift:14` — `FIXME: 为什么无效？？？` (size calculation not working)
  - `ToolKit/JSToolKit/JSStyleGuide/JSCommentStyleGudie.swift:141,143,145,149` — 4 markers (style guide examples, not functional code)
