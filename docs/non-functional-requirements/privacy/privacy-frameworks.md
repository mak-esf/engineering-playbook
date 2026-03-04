# Privacy Frameworks Reference

## Regulatory Frameworks

| Framework | Scope | Key Obligations |
|-----------|-------|-----------------|
| **GDPR** | EU/EEA personal data | Consent, right to erasure, data minimization, DPAs with processors |
| **CCPA/CPRA** | California residents | Right to opt-out of sale, disclosure of data collected |
| **HIPAA** | US health data | PHI safeguards, Business Associate Agreements, breach notification |
| **PIPEDA** | Canadian personal data | Consent, accountability, limited collection and retention |

**When this applies to ESF projects:** Any project handling data from EU/EEA users falls under GDPR. Projects processing health records require HIPAA controls. When in doubt, apply GDPR-level data minimization and consent practices as a baseline.

## Technical Privacy Controls

Use these tools and techniques when building data-handling systems:

**De-identification / Anonymization**

- [Presidio](https://microsoft.github.io/presidio) — PII detection and anonymization in text and images
- [FHIR Tools for Anonymization](https://github.com/microsoft/FHIR-Tools-for-Anonymization) — for healthcare data

**Synthetic Data**

- [Faker](https://github.com/joke2k/faker) (Python), [Mimesis](https://github.com/lk-geimfari/mimesis) — generate realistic test data without using real PII

**Privacy-Preserving ML**

- [Differential Privacy / SmartNoise](https://github.com/opendifferentialprivacy/smartnoise-samples) — add statistical noise to query results
- [TensorFlow Privacy](https://github.com/tensorflow/privacy) — DP-SGD for model training

**Data Classification (Azure)**

- [Microsoft Purview](https://azure.microsoft.com/en-us/services/purview/) — discover, classify, and govern sensitive data
- [Microsoft Information Protection](https://learn.microsoft.com/en-us/microsoft-365/compliance/information-protection) — sensitivity labels and DLP policies

## Minimum Baseline for Any Project

1. Classify data on intake (Public / Internal / Confidential / Restricted)
2. Apply access controls — least privilege, logged access
3. Encrypt at rest and in transit
4. Document what PII you collect and why (required for GDPR accountability)
5. Have a data retention and deletion policy
