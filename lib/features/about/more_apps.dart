/// Related HomiLabs apps on the About screen. Names are store titles, so they are not translated.
const moreApps = [
  (name: 'USMLE Step 1 Prep: QBank Mocks', package: 'com.homilabs.step1prep'),
  (name: 'PLAB 1 Simulator: UK Mocks', package: 'com.homilabs.plab1prep'),
  (name: 'USMLE Step 2 CK Prep: QBank', package: 'com.homilabs.step2ck'),
  (name: 'MedCal: Medical Calculator', package: 'com.homilabs.medicalcalc'),
];

/// A Play link tagged so Play Console reports installs that came from this app.
String playLink(String package) =>
    'https://play.google.com/store/apps/details?id=$package'
    '&referrer=utm_source%3Dnle_prep%26utm_medium%3Dapp%26utm_campaign%3Dcrosspromo';
