#!/usr/bin/env python3
"""Writes content/blueprint.json: the subject list, per-topic targets and the NLE (NRE Step 1) paper pattern.

PM&DC NRE standard 2024 (checked 4 Nov 2026): 200 single-best-answer MCQs, 70 % clinical (140) and 30 % applied
basic sciences (60), pass 60 %, no negative marking. The 2024 basic-science table prints 11/11/10/8/6/6/4, which
adds up to 56, not the stated 60; we give the missing 4 to Pathology and Anatomy (13 each), which the 2023 table
also weighted most. PM&DC does not publish the theory duration; prep sources report 3 hours 30 minutes.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# section key, title, group, [(topic key, id prefix, title, items per mock paper, practice items, scope note)]
SECTIONS = [
    ("medicine", "Medicine and Allied", "clinical", [
        ("cardiology", "mc", "Cardiology", 6, 15, "IHD, ACS, heart failure, arrhythmias and ECG, hypertension, valvular disease, rheumatic fever, endocarditis, pericardial disease."),
        ("pulmonology", "mp", "Pulmonology", 5, 15, "Asthma, COPD, pneumonia, TB (clinical), ILD, PE, pleural effusion, pneumothorax, lung cancer, ABGs."),
        ("gastro", "mg", "Gastroenterology and Hepatology", 5, 15, "Dyspepsia, PUD, GI bleeding, IBD, malabsorption, hepatitis B/C, cirrhosis, ascites, encephalopathy, pancreatitis."),
        ("nephrology", "mn", "Nephrology", 4, 12, "AKI, CKD, nephrotic/nephritic syndromes, electrolytes, acid-base, dialysis indications, UTI."),
        ("endocrinology", "me", "Endocrinology and Diabetes", 5, 15, "Diabetes and its emergencies, thyroid, adrenal, pituitary, calcium disorders."),
        ("neurology", "mu", "Neurology", 5, 15, "Stroke, epilepsy, headache, meningitis/encephalitis, GBS, myasthenia, Parkinson's, MS, coma."),
        ("haematology", "mh", "Haematology and Oncology", 5, 15, "Anaemias, thalassaemia, bleeding and clotting disorders, leukaemia, lymphoma, transfusion."),
        ("infectious", "mi", "Infectious Diseases", 6, 15, "Typhoid, malaria, dengue, TB treatment, HIV, hepatitis, rabies, tetanus, sepsis; Pakistan-relevant infections."),
        ("rheumatology", "mr", "Rheumatology", 3, 10, "RA, SLE, gout, spondyloarthritis, vasculitis, osteoarthritis."),
        ("psychiatry", "my", "Psychiatry", 4, 12, "Depression, anxiety, psychosis, bipolar, substance use, delirium vs dementia, suicide risk, psychotropic side effects."),
        ("dermatology", "md", "Dermatology", 2, 6, "Eczema, psoriasis, scabies, fungal infections, leishmaniasis, acne, drug eruptions."),
        ("emergency", "mx", "Emergency and Critical Care", 2, 5, "Shock, poisoning, anaphylaxis, resuscitation, organophosphate and snake bite."),
    ]),
    ("surgery", "Surgery and Allied", "clinical", [
        ("principles", "sp", "Principles of Surgery and Anaesthesia", 6, 18, "Fluids, nutrition, wound healing, surgical infection, perioperative care, anaesthesia, shock, blood transfusion."),
        ("trauma", "st", "Trauma and Emergency Surgery", 6, 18, "ATLS, head injury, chest and abdominal trauma, burns, acute abdomen."),
        ("gi", "sg", "GI and Hepatobiliary Surgery", 8, 25, "Oesophagus, stomach, small and large bowel, appendix, anorectal, gallbladder, liver, pancreas, intestinal obstruction."),
        ("breast-endocrine", "sb", "Breast and Endocrine Surgery", 4, 12, "Breast lumps and cancer, thyroid nodules and surgery, parathyroid, adrenal surgery."),
        ("urology", "su", "Urology", 5, 15, "Stones, BPH, urinary retention, testicular torsion, scrotal swellings, renal and bladder tumours."),
        ("orthopaedics", "so", "Orthopaedics", 6, 18, "Fractures and dislocations, compartment syndrome, osteomyelitis, bone tumours, spine, nerve injuries."),
        ("vascular", "sv", "Vascular and Cardiothoracic Surgery", 4, 12, "Limb ischaemia, aneurysm, varicose veins, DVT, chest drains, empyema."),
        ("neuro-headneck", "sn", "Neurosurgery and Head and Neck", 4, 12, "Raised ICP, extradural/subdural haematoma, neck lumps, salivary glands, oral lesions."),
        ("skin-hernia", "sk", "Skin, Soft Tissue, Hernia and Paediatric Surgery", 5, 20, "Hernias, lumps and ulcers, skin cancers, abscesses, pyloric stenosis, intussusception, undescended testis."),
    ]),
    ("obgyn", "Obstetrics and Gynaecology", "clinical", [
        ("obstetrics", "ob", "Obstetrics", 9, 65, "Antenatal care, bleeding in pregnancy, hypertension and diabetes in pregnancy, labour, PPH, puerperium, anaemia in pregnancy."),
        ("gynaecology", "gy", "Gynaecology", 5, 35, "Menstrual disorders, infertility, contraception, PCOS, fibroids, prolapse, gynaecological cancers, infections."),
    ]),
    ("paeds", "Paediatrics", "clinical", [
        ("neonatology", "pn", "Neonatology", 4, 30, "Neonatal resuscitation, jaundice, sepsis, prematurity, birth asphyxia, feeding."),
        ("growth", "pg", "Growth, Nutrition and Immunisation", 4, 30, "Milestones, malnutrition, rickets, Pakistan EPI schedule, breastfeeding."),
        ("illness", "pi", "Childhood Illness", 6, 40, "Diarrhoea and dehydration, pneumonia, IMCI, congenital heart disease, nephrotic syndrome, convulsions, measles, thalassaemia."),
    ]),
    ("eye", "Ophthalmology", "clinical", [
        ("eye", "ey", "Ophthalmology", 6, 60, "Red eye, cataract, glaucoma, diabetic and hypertensive retinopathy, trauma, squint, refractive errors, trachoma."),
    ]),
    ("ent", "Otorhinolaryngology (ENT)", "clinical", [
        ("ent", "en", "ENT", 6, 60, "Otitis media, hearing loss, vertigo, epistaxis, sinusitis, tonsillitis, airway, foreign bodies, head and neck cancer."),
    ]),
    ("pathology", "Applied Pathology", "basic", [
        ("general", "pa", "General Pathology", 6, 45, "Cell injury, inflammation, healing, haemodynamics, immunity, neoplasia, genetics."),
        ("systemic", "ps", "Systemic Pathology and Haematology", 7, 55, "Systemic disease, blood cells, bleeding disorders, chemical pathology, microbiology basics."),
    ]),
    ("anatomy", "Applied Anatomy", "basic", [
        ("limbs", "al", "Limbs and Back", 4, 30, "Brachial and lumbosacral plexus, nerve injuries, joints, vessels, clinical anatomy of the limbs."),
        ("trunk", "at", "Thorax, Abdomen and Pelvis", 5, 40, "Heart, lungs, abdominal viscera, inguinal canal, pelvis, perineum; embryology and histology where clinical."),
        ("head-neuro", "ah", "Head, Neck and Neuroanatomy", 4, 30, "Cranial nerves, neck triangles, brain blood supply, spinal cord tracts, lesions."),
    ]),
    ("physiology", "Applied Physiology", "basic", [
        ("physiology", "ph", "Applied Physiology", 10, 100, "Cell, blood, cardiovascular, respiratory, renal, GI, endocrine, reproductive and neurophysiology applied to cases."),
    ]),
    ("pharmacology", "Clinical Pharmacology", "basic", [
        ("pharmacology", "pc", "Clinical Pharmacology", 8, 100, "Pharmacokinetics, ANS, CNS, CVS, diuretics, GIT, endocrine drugs, antimicrobials, chemotherapy, side effects and interactions."),
    ]),
    ("biochemistry", "Applied Biochemistry", "basic", [
        ("biochemistry", "bc", "Applied Biochemistry", 6, 60, "Enzymes, metabolism and its disorders, vitamins, nutrition, molecular biology, lab tests."),
    ]),
    ("community", "Community Medicine", "basic", [
        ("community", "cm", "Community Medicine", 6, 60, "Epidemiology, biostatistics, screening, communicable disease control, MCH, nutrition, occupational and environmental health, Pakistan health system, ethics."),
    ]),
    ("forensic", "Forensic Medicine and Toxicology", "basic", [
        ("forensic", "fm", "Forensic Medicine and Toxicology", 4, 60, "Injuries, death and post-mortem changes, identification, sexual offences, poisoning, medical law and ethics in Pakistan."),
    ]),
]

PAPERS = 10
MODES = {
    "nle": {
        "title": "NLE Step 1", "subtitle": "NRE theory: 200 MCQs", "minutes": 210, "questions": 200,
        "streams": {"step1": {"title": "NLE Mock", "sections": [(k, {t[0]: t[3] for t in topics}) for k, _, _, topics in SECTIONS]}},
    },
}

doc = {
    "sections": [
        {"key": k, "title": t, "group": g, "topics": [
            {"key": tk, "prefix": p, "title": tt, "test": n * PAPERS, "practice": b, "scope": s} for tk, p, tt, n, b, s in topics
        ]} for k, t, g, topics in SECTIONS
    ],
    "modes": {m: {**v, "streams": {s: {"title": d["title"], "sections": [{"section": k, "quota": q} for k, q in d["sections"]]} for s, d in v["streams"].items()}} for m, v in MODES.items()},
    "papers": PAPERS,
}
clinical = sum(t[3] for _, _, g, ts in SECTIONS if g == "clinical" for t in ts)
basic = sum(t[3] for _, _, g, ts in SECTIONS if g == "basic" for t in ts)
assert (clinical, basic) == (140, 60), (clinical, basic)
prefixes = [t[1] for *_, ts in SECTIONS for t in ts]
assert len(prefixes) == len(set(prefixes)), "duplicate prefix"
(ROOT / "content/blueprint.json").write_text(json.dumps(doc, indent=1) + "\n")
print("test", sum(t[3] for *_, ts in SECTIONS for t in ts) * PAPERS, "practice", sum(t[4] for *_, ts in SECTIONS for t in ts))
