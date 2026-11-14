# Release and hosting kit: Prep Simulator for NLE

## Build
- Package `com.homilabs.nle_prep` (locked after the first Play upload). Version 1.0.1 (versionCode 2).
- Build: `jobq run --name nle-release-aab -- flutter build appbundle --release`, then `./gradlew --stop` in `android/`.
- Before every release: `bash scripts/check-release-ad-ids.sh`, `python3 tool/validate.py`, `flutter test`.
- Bundle: `releases/v1.0.1-2/nle-prep-1.0.1-2.aab` (49 MB, local and Drive only). SHA-256 `7971b0fa73436f8b7933e4c58a6448fc7b8746aca407492748650539aa42fa5b` (built 11 Nov 2026). Previous: `releases/v1.0.0-1/nle-prep-1.0.0-1.aab`.
- Upload key SHA-1: `A8:75:DC:DE:C7:45:45:2C:D7:EE:81:B9:EB:25:9F:06:25:5F:B4:07`.
- Signing: `android/key.properties` → `.secrets/nle-upload.keystore` (credentials in `.secrets/nle-upload-keystore-credentials.txt`). `.secrets/` goes to the local and Drive backups, never GitHub. Losing it means a support request to Google.

## Website: https://nle.homilabs.org
- Hostinger: create the subdomain `nle.homilabs.org` in hPanel, then connect Git deployment to `https://github.com/AwaizFatima08/nle`, branch `deploy`, with auto-deployment.
- Change `website/`, commit, then `bash scripts/publish-site.sh`. Flush the CDN cache in hPanel if pages look stale.
- Pages: landing, `/privacy.html`, `/terms.html`, `/app-ads.txt`.
- 14 Nov 2026: "Coming soon" replaced with the "Get it on Google Play" link. Still open: add the app to homilabs.org.

## AdMob (account homilabs.smc@gmail.com)
- Created 4 Nov 2026: app "Prep Simulator for NLE", App ID `ca-app-pub-2087846699268567~9863225682`; units banner `nle_home_banner` and interstitial `nle_results_interstitial` (ids in `config/admob.json`). Debug builds use Google test units.
- "Limited ad serving" until the Play listing is live.
- Store linked 14 Nov 2026: Google Play listing com.homilabs.nle_prep added and verified; AdMob app review typically 2-3 days (ad serving limited until then). `app-ads.txt` is live at https://nle.homilabs.org/app-ads.txt; AdMob crawls it after linking (check Apps → app-ads.txt in a day).
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
NOT A GOVERNMENT APP. Prep Simulator for NLE is independent practice by HomiLabs. It does not represent the Pakistan Medical and Dental Council (PM&DC) or any government entity, and is not affiliated with or endorsed by PM&DC.

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

OFFICIAL SOURCES
The exam information in this app is summarised from PM&DC's official pages. Always check them, your admit card and official PM&DC notices:
• PM&DC website: https://pmdc.pk
• NRE standard and syllabus: https://pmdc.pk/Publication/Syllabus
• NRE registration portal: https://nre.pmdc.pk

All questions are original practice material written by HomiLabs, not real or recalled papers, and scores are for practice only.
```

## Release history
- 4 Nov 2026: 1 (1.0.0) published to **internal testing**, email list "Testers" (homi55@gmail.com, homi55.home@gmail.com).
- 4 Nov 2026: 1 (1.0.0) sent to **production**, full rollout, all 178 countries / regions, together with the store listing and App content, in one Google review. Homi chose to go to production directly; the medical review items below stay open.
- 7 Nov 2026: production rejected under the **Misleading Claims** policy (government information): no link to the official source and no clear "not a government entity" disclaimer.
- 11 Nov 2026: the 1.0.0 submission was removed from review. 1.0.1 (versionCode 2) adds a "Not a government app" notice on the Mocks, Guide and About screens, tappable PM&DC links (pmdc.pk, pmdc.pk/Publication/Syllabus, nre.pmdc.pk) on Guide and About and in the first guide article, and the same on the website. The store description now opens with the disclaimer and ends with an "Official sources" list; the short description starts with "Unofficial". AI asset declaration: don't label (icon and feature graphic drawn in code, screenshots from the app).
- 11 Nov 2026: 2 (1.0.1) sent to **production** as release 2 (1.0.0 not included), full rollout, all 178 countries / regions, with the new listing and App content, in one Google review.
- 14 Nov 2026: approved; **live on Google Play** (https://play.google.com/store/apps/details?id=com.homilabs.nle_prep).

## Before production (open items)
- Homi reviews the medical content, the guide (especially exam-day rules) and `docs/review-flags.md`.
- Trademark: "NLE" is used descriptively, with the PM&DC notice in the About screen, listing and website.
