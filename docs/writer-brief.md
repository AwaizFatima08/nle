# Writer brief: Prep Simulator for NLE

You write original single-best-answer MCQs for a HomiLabs Android app that helps foreign medical graduates prepare for the PM&DC National Licensing Examination (NLE, now officially the National Registration Examination, NRE) Step 1 theory paper in Pakistan. The real paper is 200 MCQs testing applied knowledge at the level of a newly qualified general practitioner: 70 % clinical sciences, 30 % applied basic sciences. Accuracy matters more than speed: one wrong key damages a doctor's trust.

## Format
Read `docs/content-schema.md` and `content/blueprint.json` (your topics' prefix, counts and scope). Write `content/bank/<section>/<topic>.jsonl`. For a topic split across writers, use the file name and id range given in your task. Write in chunks of at most 25 questions per tool call, appending with Bash heredocs (`cat >> file <<'EOF'`), and run `python3 tool/validate.py --files <your files>` after each chunk until it reports 0 errors and no WARN.

## Question style
- Clinical subjects: mostly short clinical vignettes (age, sex, presentation, key findings, relevant investigations), then a focused lead-in: most likely diagnosis, most appropriate next step, best initial investigation, first-line treatment, most likely complication, mechanism. Mix lead-ins; do not make most of them "diagnosis".
- Basic sciences: applied, clinically anchored where possible ("A man cannot abduct his arm beyond 15° after a fracture of ... Which nerve...?"). Some direct recall is fine, about a third.
- Setting is Pakistan: names (Ayesha, Bilal, Rukhsana, Imran), places (a BHU in rural Sindh, a THQ hospital, Lahore), local disease burden (TB, typhoid including XDR typhoid, hepatitis B and C, dengue, malaria, thalassaemia, rabies, snake bite, organophosphate poisoning, malnutrition), the Pakistan EPI schedule, and local practice where it is standard. Use SI units with common Pakistani lab units (Hb g/dL, glucose mg/dL, creatinine mg/dL), with normal ranges in brackets where a value is borderline.
- Management follows current mainstream international guidance as taught in Pakistan (WHO, NICE, ATLS, ALS, IMCI, WHO TB guidance). If guidance genuinely differs between bodies, avoid that point.
- Stems under 900 characters; a prepared candidate should answer in about one minute. No hints in the stem, no "Which of the following is NOT" more than rarely, and never negative stems with a single negation trap.
- British English (anaemia, oesophagus, paediatric, haemorrhage).

## Options
- Exactly 4 options, one clearly best. Wrong options must be plausible to a weaker candidate (real differential diagnoses, the common wrong drug, the investigation done too early) and definitely inferior.
- Homogeneous options: all diagnoses, or all drugs, or all investigations. Similar length and form. The correct option must not stand out: it is the longest no more often than the others (the validator warns above 40 %; a file with that WARN is not finished). Spread the key evenly across A-D with no pattern.
- No "all/none of the above", no "both A and B", no "always/never" giveaways.

## Explanations
Teach in 2-4 sentences: the key clue and why it points to the answer, then why the most tempting wrong option is wrong. Do not start with "The answer is". No references or citations.

## Facts
- Only state facts you are sure of and that are stable. If unsure, write a different question.
- No drug doses unless they are standard and unambiguous (e.g. adrenaline 0.5 mg IM 1:1,000 in adult anaphylaxis). No brand names. No current office holders, statistics that change yearly, or "latest" guidelines by year.
- Forensic and medicolegal points: use the Pakistan Penal Code and Qanun-e-Shahadat sections only where you are certain; otherwise ask about the medical finding instead.
- Respectful, clinical language. Sexual offence questions focus on examination findings and procedure, never graphic detail.

## Variety
Vary ages, sexes, settings, lead-ins and scenarios. No near-duplicates within or across files; read what already exists in your topic files first. Cover the topic's scope evenly; levels about 25 % easy, 55 % medium, 20 % hard.

## Originality
Original work only. Never copy or closely reword questions from PM&DC or NLE/NRE recalls, UWorld, AMBOSS, PassMedicine, First Aid, Kaplan, Pakistani recall books, websites or textbooks.

## Boundaries
Only write the files in your task, plus your scratch folder. Do not edit tools, the blueprint or other topics. Do not run git. Final reply at most 6 lines: files, question counts, validator result, any questions you are unsure about (by id).
