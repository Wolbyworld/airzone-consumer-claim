# Intake and evidence

## Minimum viable intake

Ask for facts, not a full identity dossier. Use unknown rather than inventing.

- Country of purchase; habitual residence; installation country and region. Spain/Madrid routing is not universal.
- Individual household use or business/professional use? Who bought and whose name is on the contract? A gift, second-hand purchase, landlord/tenant or new-build installation needs ownership/contract-chain clarification.
- Exact controller/gateway model and generation (not just “Airzone”); relevant firmware/app version if known; invoice description; installation and Cloud registration dates. Keep full serial/MAC/site IDs private and only collect when necessary.
- Seller/installer legal name, invoice date, price attributable to the device/service, and the Cloud provider identified in the relevant terms.
- What was promised at sale, by whom and where? Was remote access a material reason for purchase? What did the owner use, for how long, and without which recurring charge?
- Which function is at issue: outside-home on/off or temperature control, remote scheduling, voice/cloud integration, history, or a new advanced service?
- Notice received, effective date stated, current behavior, trial activated or not, charge made or not. Capture the owner's chosen remedy before offering alternatives.
- Terms supplied/accepted at purchase and Cloud signup; later versions/notices; evidence of acceptance. No terms found is an evidentiary gap, not proof no terms existed.
- Prior contact, exact response, any OCU/OMIC/Consumo/arbitration/court file, current deadlines and receipt. Check for existing work before starting again.

## Evidence hierarchy and capture

Prefer contemporaneous invoice/contract and seller advertising, device-specific manuals, original notices and full company replies. Current official pages show the current policy, not necessarily the old bargain. Owner recollection is useful but label it. A forum report is a lead, not proof of the owner's loss or a representative prevalence estimate.

Assign IDs: E01 proof of purchase; E02 product promise; E03 accepted terms; E04 change notice; E05 observed behavior; E06 initial complaint/send proof; E07 full response; E08 official filing receipt. Missing items stay “missing”; never insert fabricated documents.

For each item record filename, source URL/channel, date issued, date captured (timezone), relevant page/section, what it supports, limitations, private/public status and redacted-copy path. Save full context, not a misleading cropped fragment. If web content changes, retain the earlier lawful capture and date; do not silently replace it.

With the owner's consent, a non-disruptive test may compare local Wi-Fi with mobile data for the same function and account. Do not change heating/cooling in a way that could affect people, pets, equipment or occupancy safety. Capture exact error/offer wording and time. Do not activate a trial, buy, cancel, reset hardware, change firmware or remove an account to create evidence.

## Redaction and storage

Maintain separate `originals/`, `redacted/`, `drafts/`, `receipts/` and a private case ledger. Do not ship these folders with this reusable skill. Collect only what the current action needs. Never put credentials, certificate private keys, OTPs or full payment-card data in a claim.

For public material remove owner name, DNI/NIE, address, phone/email, signatures, invoice/order/case IDs, serial/MAC/site IDs, QR/barcodes, account links and location metadata. Keep substantive dates/model/price only if necessary and not identifying in combination. Redact underlying PDF text/OCR, annotations, hidden layers and metadata—not merely a black shape. Verify with text extraction and visual inspection. Don't alter originals. Official submissions may legitimately require unredacted identity/purchase evidence; transmit only to the verified authority and only with approval.

## Claim-to-proof table

| Proposition | Evidence IDs | Status | Limitation / next question |
|---|---|---|---|
| Owner bought [model] on [date] | E01 | Documented / missing | Invoice names [seller], not necessarily Cloud provider |
| Remote control formed part of the bargain | E02, E03 | Documented / inferred / disputed | Separate marketing language from duration promise |
| Company announced [specific change] | E04 | Documented | Does not establish actual cutoff |
| Function failed without subscription on [date] | E05 | Observed / owner report / untested | Rule out outage/account/network fault without destructive tests |
| Company did not identify contractual basis | E06, E07 | Reply analysis | Cite the exact unanswered question, not “they said nothing” |

## Remedy selection

Start with preservation/restoration of the specific purchased function without a new recurring charge, if supported. Ask for written model/account-specific confirmation. Alternatives may include an actually equivalent solution or a proportionate monetary remedy, but assess feasibility, consent, valuation and legal basis first. A full installation refund, damages or lifetime service is not automatic. Explain whether cancelling the Cloud contract could remove the service the owner wants preserved.

## Public repository boundary

A reusable public skill may contain neutral templates and explicitly synthetic examples, not real case evidence. Raw private emails, invoices, third-party documents and receipts remain private. Even anonymized excerpts require a separate privacy, confidentiality and reproduction-rights review before any approved publication; apparent anonymity is not sufficient. See the public-release gate in `campaign-privacy.md`.
