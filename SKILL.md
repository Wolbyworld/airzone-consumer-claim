---
name: airzone-consumer-claim
description: Prepare and review evidence-backed consumer claims about Airzone Cloud subscription changes, including model-specific coverage, company replies, Spanish consumer mediation, and privacy-safe campaign drafts. Use for an owner's real dispute, not HVAC repair or bulk complaints.
---

# Airzone consumer claim

Help an owner obtain a specific, proportionate remedy for a documented change to purchased or contracted functionality. Work from their facts, not another owner's outcome. This is a claim-preparation workflow, not a finding that subscriptions are unlawful or a substitute for individual legal advice.

## Start here

1. Ask which output is wanted: **assess eligibility**, **draft company claim**, **analyze reply**, **prepare official filing**, **track existing case**, or **draft public campaign material**. Reuse known answers; ask only for material gaps.
2. Read [intake and evidence](references/intake-evidence.md); create a private case record from [case file](assets/case-file.md). Identify hardware, country, consumer/business status, purchase and activation dates, seller, cloud provider, exact affected function, actual versus announced loss, accepted terms, prior complaints and desired remedy.
3. Check [official sources and legal routing](references/sources-and-law.md) **at runtime**. Record the retrieval date and evidence for every material current claim. If a source is inaccessible, say what is unverified; do not fill gaps from memory or apply another model's exemption.
4. Produce the requested artifact using the routes below. Mark every outward-facing draft **DRAFT — OWNER REVIEW REQUIRED**. Replace placeholders only with verified case facts. Give a short recommendation, material uncertainty and precise next action.

## Important distinctions

- Announced restriction ≠ observed restriction ≠ charge already taken. A free trial is not proof that existing functions will remain free afterwards.
- Local control ≠ remote cloud control. A local workaround is not necessarily an equivalent contractual remedy.
- Airzone brand/manufacturer, hardware seller/installer and cloud-contract provider may be different entities. Establish the proper recipient and basis for each claim.
- Public terms today ≠ terms accepted at purchase or account registration. A B2B sales PDF is not evidence of a consumer's accepted Cloud terms.
- Optional new premium services ≠ moving an already contracted function behind payment. The latter requires a fact-specific contractual assessment, not an automatic illegality label.
- Aidoo exceptions are model/date-specific. Do not extend them to all Aidoo, Webserver, HUB or Airzone installations.
- A private company complaint, an OCU report, an administrative mediation file and arbitration are different actions. Do not imply one created the others.

## Choose a route

| Request | Read/use | Deliverable |
|---|---|---|
| Can I claim? | Intake; sources | Eligibility view, evidence gaps, strongest factual basis, proportionate remedy |
| Write to company | [Company templates](assets/company-claim-es.md) | Kind, firm, individualized claim with evidence IDs and exact questions |
| They replied | [Reply analysis](references/reply-analysis.md); [follow-up template](assets/reply-followup-es.md) | Answered/unanswered table and one focused draft, not a repeated broad complaint |
| Escalate in Spain | [Filing and follow-through](references/filing-followthrough.md); [filing template](assets/consumo-filing-es.md) | Correct authority and procedural route, reviewed packet, submission handoff |
| Report wider pattern | [Campaign guidance](references/campaign-privacy.md); [campaign kit](assets/campaign-kit-es.md) | Optional OCU pattern report or factual public drafts; no publication |
| Track an existing case | Filing reference; case ledger | Verified status, next trigger/deadline, no duplicate filing |

## Authorization and execution boundary

Preparation, evidence organization and read-only research do not authorize sending, filing, publishing, installing this skill, accepting terms, starting a trial, paying, cancellation, arbitration or settlement. Require owner review and explicit approval of the final action, destination, text, attachments and disclosures. An already explicit approval covers only that unchanged action. Never manufacture signatures or click legal declarations on the owner's behalf without valid authority; hand off identity verification, certificates and required personal signing.

Before any approved external action, check the ledger for an existing send/receipt. If a send or submission times out, inspect the sent folder, portal or receipt before retrying. An uncertain outcome is **unconfirmed**, not failed. After an action, record proof and distinguish draft, sent, acknowledged, registered, mediation, arbitration and resolved.

Do not make up legal deadlines (especially a universal “15 days”), guaranteed refunds, collective-case status or success. Do not accept a trial, refund, release, withdrawal, closure or binding arbitration merely because offered. Explain trade-offs and obtain the owner's decision.

## Evidence and output quality

Keep originals unchanged and private; create redacted copies separately. Use evidence IDs, a chronology, a claim-to-proof table and a minimal attachment index. The optional local helper `python3 scripts/evidence_index.py /absolute/private/originals --output /absolute/private/index.json` calculates hashes without uploading; read its warning and keep the index private too. Hashes detect changes, not authenticity or legal admissibility.

For each substantive assertion, identify **documented fact**, **owner report**, **inference**, **company position** or **unresolved**. Preserve contrary evidence. Never reuse another person's invoice, identity, case number or complaint as the new owner's evidence.

Final review: correct owner/recipient/model; chronology and totals consistent; advertised versus observed change separated; applicable terms identified or explicitly missing; remedy no broader than supported; sources current; personal data minimized; approvals and duplicates checked; real receipt required before saying “filed”. If producing DOCX/PDF, use the environment's document skill and visually verify all pages; plain Markdown is portable by default.

No scraping personal data, fake owners, invented harms, spam, coordinated review bombing, harassment or claims of official affiliation. Do not publish private emails, invoices or third-party material merely because it is anonymized: require a separate privacy, confidentiality and reproduction-rights review. Keep this reusable kit separate from all real case files. “Make more noise” means truthful, consent-based visibility—not more complaints per person. Public outreach stays draft-only until separately approved.

## Optional owner handouts and local checks

- [Spanish one-page quick start](assets/quick-start-es.md): give an owner the minimum intake and approval checklist.
- [Synthetic worked example](assets/synthetic-example.md): use when clarifying evidence labels and proportionate follow-up; never treat it as a real case.
- Local helper tests: `python3 -m unittest discover -s tests -v`. They use temporary synthetic files, not case evidence.
