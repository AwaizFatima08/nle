# Release and hosting kit: Prep Simulator for NLE

## Build
- Package `com.homilabs.nle_prep` (locked after the first Play upload). Version 1.0.0 (versionCode 1).
- Build: `jobq run --name nle-release-aab -- flutter build appbundle --release`, then `./gradlew --stop` in `android/`.
- Before every release: `bash scripts/check-release-ad-ids.sh`, `python3 tool/validate.py`, `flutter test`.
- Bundle: `releases/v1.0.0-1/nle-prep-1.0.0-1.aab` (49 MB, local and Drive only). SHA-256 `59c15ddb4d841e226ef0290ed64397865ac891f239547eefb8f0fe9496477996` (built 4 Nov 2026).
- Upload key SHA-1: `A8:75:DC:DE:C7:45:45:2C:D7:EE:81:B9:EB:25:9F:06:25:5F:B4:07`.
- Signing: `android/key.properties` → `.secrets/nle-upload.keystore` (credentials in `.secrets/nle-upload-keystore-credentials.txt`). `.secrets/` goes to the local and Drive backups, never GitHub. Losing it means a support request to Google.

## Website: https://nle.homilabs.org
- Hostinger: create the subdomain `nle.homilabs.org` in hPanel, then connect Git deployment to `https://github.com/AwaizFatima08/nle`, branch `deploy`, with auto-deployment.
- Change `website/`, commit, then `bash scripts/publish-site.sh`. Flush the CDN cache in hPanel if pages look stale.
- Pages: landing, `/privacy.html`, `/terms.html`, `/app-ads.txt`.
- After Play launch: replace "Coming soon on Google Play" with the Play link, and add the app to homilabs.org.

## AdMob (account homilabs.smc@gmail.com)
- Created 4 Nov 2026: app "Prep Simulator for NLE", App ID `ca-app-pub-2087846699268567~9863225682`; units banner `nle_home_banner` and interstitial `nle_results_interstitial` (ids in `config/admob.json`). Debug builds use Google test units.
- "Limited ad serving" until the Play listing is live.
- After the Play listing is live: AdMob → Apps → this app → Add store (com.homilabs.nle_prep). `app-ads.txt` is already in `website/`.
- Privacy & messaging: European regulations messages are per app, not account-wide. "Prep Simulator for NLE consent" (this app only, privacy URL https://nle.homilabs.org/privacy.html, "Do not consent" on for all countries) published 4 Nov 2026 for the app's Google UMP request.

## Play Console
App "Prep Simulator for NLE", Play app id 4975932169548060068 (Homilabs account 9161588402757830740), created 4 Nov 2026.

| Item | Value |
|---|---|
| App icon 512×512 | `store-assets/icon-512.png` |
| Feature graphic | `store-assets/feature-graphic.png` |
| Phone screenshots | `store-assets/screenshots/01-05` (1080×2160, profile build, no ads shown) |
| Privacy policy URL | https://nle.homilabs.org/privacy.html |
| Website | https://nle.homilabs.org |
| Contact email | homilabs.smc@gmail.com |
| Ads | Yes (AdMob banner on home tabs; one interstitial after results or practice) |
| App access | All functionality available without login |
| Data safety | Collected and shared via the AdMob SDK, required, not ephemeral: approximate location (Advertising), app interactions (Analytics, Advertising), diagnostics (Analytics), device or other IDs (Advertising, Fraud prevention). Encrypted in transit; no accounts. Attempts stay on the device |
| Advertising ID | Yes, purpose Advertising or marketing |
| Health apps | Medical reference and education |
| Government / financial | No / no financial features |
| Content rating | IARC, All Other App Types, primarily educational, No to everything else. Result: ESRB Everyone, PEGI 3, USK all ages, IARC 3+ (submitted 4 Nov 2026) |
| Target audience | 18+ |
| Category | Education (Medical is also possible; Education fits exam prep) |

**App name** (22 characters): `Prep Simulator for NLE`

**Short description** (80 max): `NLE/NRE Step 1 mock papers for foreign medical graduates, all answers explained.`

**Full description**:
```
Prepare for the PM&DC licensing exam for foreign medical graduates in Pakistan (NLE, now called the National Registration Examination, NRE) the way it feels on the day.

10 FULL-LENGTH MOCK PAPERS
• 200 single-best-answer MCQs in each, weighted like the theory paper: 140 clinical sciences and 60 applied basic sciences.
• Timed, with flags and a question map. No negative marking, just like the real paper.
• Your score against the 60% pass mark, clinical and basic science totals, every subject, and the topics to work on next.
• Every question explained after you submit.

SUBJECT PRACTICE
• Question pools for Medicine, Surgery, Obstetrics and Gynaecology, Paediatrics, Ophthalmology, ENT, Pathology, Anatomy, Physiology, Pharmacology, Biochemistry, Community Medicine and Forensic Medicine, by topic.
• Instant answers and explanations. Practice questions never appear in the mocks.

RULES, GUIDELINES AND TIPS
• The paper pattern, eligibility and registration, exam-day rules, passing, validity and attempts.
• A 12-week study plan, how to answer single-best-answer questions, time management and high-yield themes for Pakistan.

PRIVATE AND OFFLINE
• No account. Everything works offline, and your scores stay on your phone.
• Free, with light ads, never during a mock or a practice question.

Prep Simulator for NLE is independent practice material by HomiLabs. It is not affiliated with, endorsed by or connected to the Pakistan Medical and Dental Council (PM&DC). All questions are original practice material, not real or recalled papers, and scores are for practice only. Always follow your admit card and official PM&DC notices.
```

## Release history
- 4 Nov 2026: 1 (1.0.0) published to **internal testing** (no testers yet; add an email list under Internal testing → Testers). Store listing and App content (8 changes) sent for Google review the same day. Production not started.

## Before production (open items)
- Homi reviews the medical content, the guide (especially exam-day rules) and `docs/review-flags.md`.
- Trademark: "NLE" is used descriptively, with the PM&DC notice in the About screen, listing and website.
