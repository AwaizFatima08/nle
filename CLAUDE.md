# Prep Simulator for NLE (HomiLabs) — project notes

Flutter Android app for foreign medical graduates preparing for the PM&DC NLE (now officially NRE) Step 1 theory paper:
subject practice pools, 10 full-length mock papers with scoring and explanations, and rules, guidelines and tips. No login.
Package `nle_prep`, app id `com.homilabs.nle_prep` (locked after the first Play upload). Launcher name "NLE Simulator".
Built on the NTS app's engine (`/mnt/storage/projects/nts`).

## Locations
- Code: `/mnt/storage/projects/nle` · GitHub `AwaizFatima08/nle` (PUBLIC repo: no secrets)
- Local backup: `/mnt/storage/project_backups/nle_backup`
- Google Drive backup: Projects/nle, https://drive.google.com/drive/folders/198ZIjqCcK_S8weAAD4vfqYj70276pBhn
- Backups: `bash scripts/backup.sh` (all three layers)
- Site: https://nle.homilabs.org (Hostinger), source in `website/`

## Exam format (PM&DC NRE standard 2024, checked 4 Nov 2026)
200 single-best-answer MCQs: clinical 140 (Medicine 52, Surgery 48, Obs & Gynae 14, Paeds 14, Eye 6, ENT 6) and applied
basic sciences 60. Pass 60 %, no negative marking, theory pass valid 5 years; CSE is a 20-station OSCE.
PM&DC's basic-science table prints 11/11/10/8/6/6/4 (= 56, not 60); we use Pathology 13 and Anatomy 13. PM&DC
publishes no theory duration; mocks use 210 minutes (what prep sources report). `tool/make_blueprint.py` holds these.

## Content
- `content/bank/<section>/<topic>.jsonl` (format in `docs/content-schema.md`); `docs/writer-brief.md` is the quality bar.
- Mock pool 2,000 (10 × 200) and a separate practice pool of 1,200, so practice never spoils a mock.
- `python3 tool/validate.py`, `python3 tool/build_content.py` (fixed seed: papers stay stable), `tool/blind.py`
  (independent answer check), `tool/patch.py` (apply reviewed fixes). `flutter test test/content` checks the built papers.
- Every question is original HomiLabs work. Never copy PM&DC papers, recalls, UWorld, AMBOSS, PassMedicine or books.
- All medical content, the exam-day rules article and items in `docs/review-flags.md` are for Homi's review before release.

## Ads
Ids in `config/admob.json`. Banner on Home tabs only; interstitial when leaving results or a practice set, 5 minutes apart.
Never on mock, practice question or review screens. Debug builds use Google test units.

## Gate before commit
```
dart format --set-exit-if-changed lib test
flutter analyze
flutter test
```
Heavy jobs follow `~/.claude/heavy-jobs.md`: use `jobq`, then `./gradlew --stop`.
