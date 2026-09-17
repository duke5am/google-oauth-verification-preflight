# Privacy Policy — Fillable Template for a Google OAuth App

**Template:** `privacy-policy-template.md`
**What this is:** a complete privacy policy you can publish on your homepage, written so that the
disclosures Google asks of OAuth apps are present and easy for a reviewer to find.
**How to use it:** copy the block in Part 2 into your CMS, replace every `[BRACKET]`, delete the
parts that do not apply (and delete nothing that does apply), then read it aloud once. If a
sentence would embarrass you in front of a customer, rewrite it.

> **This is not legal advice.**
> This template is a starting point written for the Google OAuth verification context. Privacy law
> is jurisdiction-specific, changes frequently, and interacts with your contracts and your data
> practices in ways a template cannot know about. Have a lawyer qualified in your jurisdiction —
> and in the jurisdictions of your users — review the finished policy before you publish it. If
> you handle data about individuals in the UK or EU, GDPR/UK GDPR obligations apply on top of what
> is below. If you handle data about California residents, the CCPA/CPRA may apply. This template
> covers the Google-specific disclosures; it does not attempt to cover every statutory
> requirement in every jurisdiction.
>
> Also note: Google's own requirements change. Confirm the current published requirements for
> privacy policies for OAuth apps before you submit. This is not an official Google document and
> is not affiliated with or endorsed by Google.

---

## Part 1 — What the policy must contain for OAuth verification

Google's requirements for apps that access Google user data include publishing a privacy policy.
Separately, Google's API Services User Data Policy sets out how apps may use that data, including
the Limited Use requirements. For verification purposes, a reviewer needs to find these things in
your policy:

| # | Required content | Where it is in the template below |
|---|---|---|
| 1 | What Google user data you access | Section 3 |
| 2 | How you use it | Section 4 |
| 3 | How it is stored and who it is shared with | Sections 5 and 6 |
| 4 | How long you keep it | Section 7 |
| 5 | How a user can delete it, and how they revoke access | Section 8 |
| 6 | The Limited Use commitment (no ads, no selling, no transfer except as allowed) | Section 4 |
| 7 | How to contact you | Section 11 |
| 8 | That the policy is reachable from the homepage without logging in | `homepage-requirements.md` |

Two structural rules that matter as much as the content:

- **Put the Google-specific section under a heading a reviewer can find quickly.** A reviewer
  scanning for "Google" should hit it without reading your whole policy. A dedicated
  `Google User Data` section, as below, does that.
- **Never claim less access than you have, or more retention than you have.** If you cache API
  responses, that is storage — disclose it. If you email a report to the user's Gmail address,
  you are sending data to Google's servers; that is a disclosure, not a secret.

---

## Part 2 — The policy template

Copy from `PRIVACY POLICY` to the end. Everything in `[BRACKETS]` must be replaced.

---

# PRIVACY POLICY

**Effective date:** [DATE]
**Last updated:** [DATE]

This privacy policy explains how [LEGAL ENTITY NAME] ("[APP NAME]", "we", "us") collects, uses,
stores, shares and deletes information when you use [APP NAME] at [HOMEPAGE URL] (the "Service").
It also explains specifically how we handle information we receive from Google APIs when you sign
in with your Google Account.

## 1. Who we are

[LEGAL ENTITY NAME], [ADDRESS OR COUNTRY].
Contact for privacy questions: [PRIVACY EMAIL].
Data protection officer (if you have one, or if required in your jurisdiction): [NAME / EMAIL].

## 2. Information you give us

- **Account information.** Your name, email address and password or authentication identifiers.
- **Content you provide.** [e.g. invoice details you type, notes, files you upload directly.]
- **Billing information.** Handled by [PAYMENT PROCESSOR]. We receive confirmation of payment and
  a customer identifier; we do not store your full card number.
- **Support communications.** Messages you send us and our replies.

## 3. Google user data we access

> **Instruction to the person filling this in (delete this note from the published policy).**
> The example scope string in the table below is illustrative only. Before you publish, list your own
> scopes here and **confirm each one's current wording and current classification (non-sensitive /
> sensitive / restricted) against Google's current published OAuth scope lists** — tier names and
> tiers themselves change. Do not copy a scope string from this template without checking it, and do
> not assume that a scope you have seen described elsewhere is still in the tier you remember.

When you choose to sign in with Google, or to connect a Google service, we ask Google for
permission to access specific data. **We only request access to the data listed here, and only for
the purposes described in section 4.** You are shown exactly which permissions are being requested
on Google's consent screen before you approve anything, and you can decline and still use
[the parts of the Service that do not require it / nothing, if Google is your only sign-in].

For each permission we request, we set out what it grants and why it is needed. **Confirm every
scope string against Google's current published list before publishing this table.**

| Google permission (scope) | What it gives us access to | Why we ask for it |
|---|---|---|
| [SCOPE 1, e.g. https://www.googleapis.com/auth/drive.readonly] | [e.g. Read-only access to files in the Google Drive folder you select] | [e.g. To read the invoice PDFs in that folder so you do not have to upload them] |
| [SCOPE 2] | [WHAT] | [WHY] |
| [SCOPE 3] | [WHAT] | [WHY] |

**We request only the minimum access needed for the features described here.** We do not request
access to Google services that we do not use.

To stop us accessing your Google data at any time, see section 8.

## 4. How we use Google user data

We use Google user data only to provide and improve the features you have asked for. Replace the
first bullets below with your own real purposes, one bullet per scope, and delete the rest:

- [PURPOSE 1: the specific feature that uses the first scope]
- [PURPOSE 2: the specific feature that uses the second scope]
- To maintain the security and reliability of the Service, for example to detect abuse, and to
  comply with the law.

**We do not use Google user data for advertising.** We do not use it for personalised or
interest-based advertising, retargeting, or to build advertising profiles, and we do not sell it.
We do not use it to determine creditworthiness or for lending purposes.

### Our commitments under Google's Limited Use requirements

[APP NAME]'s use of information received from Google APIs adheres to the
[Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including the Limited Use requirements. In particular:

- We only use Google user data to provide or improve **user-facing features** that are prominent
  in the Service's interface, and we only use it for those features.
- We do not transfer Google user data to third parties except: where necessary to provide or
  improve those features; to comply with applicable law; or as part of a merger, acquisition or
  sale of assets, in which case we will give users notice.
- We do not use Google user data for serving advertisements, including personalised, retargeted or
  interest-based advertising.
- We do not sell Google user data.
- We do not allow humans to read Google user data unless you have given us your affirmative
  agreement for specific items; it is necessary for security purposes such as investigating and
  preventing abuse; it is necessary to comply with applicable law; or it is for our internal
  operations and the data has been aggregated and anonymised so that it is not identifiable to you.
- We do not use Google user data to determine creditworthiness or for lending purposes.

## 5. How we store Google user data

- **Where.** [HOSTING PROVIDER AND REGION]
- **Encryption in transit.** All traffic between your browser, our servers and Google's APIs is
  encrypted using TLS 1.2 or above.
- **Encryption at rest.** [HOW DATA AND TOKENS ARE ENCRYPTED AT REST]
- **What we store.** [BE SPECIFIC: what fields you keep, for how long, and what you cache] For
  example, a compliant answer would name the extracted fields, the retention period for any
  original files, and the cache window for API responses, rather than saying "we keep what we need".
- **What we do not store.** [WHAT YOU DELIBERATELY DO NOT KEEP]
- **Access controls.** [WHO CAN REACH PRODUCTION DATA, AND HOW]
- **Security incidents.** If we become aware of a breach affecting your Google user data, we will
  notify you and the relevant authorities as required by applicable law.

## 6. Who we share Google user data with

**We do not sell Google user data and we do not share it with third parties for their own
marketing purposes.**

We share it only with service providers who process it on our behalf so that we can run the
Service, and only as far as necessary:

| Recipient | What they receive | Why |
|---|---|---|
| [e.g. AMAZON WEB SERVICES] | [e.g. Hosting and storage of the data described in section 5] | [e.g. Infrastructure] |
| [e.g. PAYMENT PROCESSOR] | [e.g. Billing details only — no Google user data] | [e.g. Payments] |
| [e.g. ERROR MONITORING SERVICE] | [e.g. Error reports with user identifiers redacted] | [e.g. Reliability] |

We may also disclose Google user data where we are legally required to do so, where it is
necessary to investigate abuse or security incidents, or as part of a merger, acquisition or sale
of assets (with notice to you).

If you do not share Google user data with anyone at all, replace the table above with this
sentence: "We do not share Google user data with any third party except as required by law."

## 7. How long we keep Google user data

| Data | Retention period | What happens at the end |
|---|---|---|
| [DATA CATEGORY 1] | [PERIOD] | [DELETION MECHANISM] |
| [DATA CATEGORY 2] | [PERIOD] | [DELETION MECHANISM] |
| [Cached API metadata] | [e.g. 24 hours] | [e.g. expired automatically] |
| [OAuth tokens] | [e.g. until the user revokes access] | [Revoked with Google and deleted from our systems] |
| [Support emails] | [e.g. 24 months] | [Deleted] |

Use realistic entries and make sure a mechanism actually enforces each period. Include any cached
or derived data, and say what happens to backups.

We may retain limited records where the law requires it, for example billing records for tax
purposes, and we may retain aggregated or anonymised information that cannot be used to identify
you.

## 8. How to access, revoke, delete or export your data

**Revoke our access to your Google Account.** You can do this yourself at any time:

1. Go to your Google Account at [myaccount.google.com](https://myaccount.google.com).
2. Open **Data & privacy**.
3. Under **Data from apps and services you use**, open **Third-party apps & services** (wording
   may change; Google controls these screens).
4. Select **[APP NAME]** and choose **Delete all connections you have with [APP NAME]** (or
   **Remove access**).

Revoking access stops us making further Google API calls. To have data already in our systems
deleted, use one of the options below.

**Delete your data in the Service.** [THE IN-PRODUCT DELETION PATH AND TIMESCALE]

**Email us.** Write to [PRIVACY EMAIL] from the address associated with your account and ask us to
delete your data. We will confirm within [7] days and complete deletion within [30] days, subject
to any legal retention obligations we tell you about.

**Export your data.** [DESCRIBE THE EXPORT PATH, or delete this paragraph if you do not offer one.]

**Access and correction.** You can ask us what we hold about you and ask us to correct anything
inaccurate, using the same address.

If you are in the UK, EEA or Switzerland, you also have the rights set out in data protection law,
including rights of access, rectification, erasure, restriction, portability and objection, and
the right to complain to your supervisory authority. If you are a California resident, you have
rights under the CCPA/CPRA. [ADJUST THIS FOR YOUR JURISDICTIONS WITH YOUR LAWYER]

## 9. Cookies and similar technologies

[List the cookies you use, and confirm none are used for advertising]

## 10. Children

The Service is not directed at children under [13/16], and we do not knowingly collect their data.
If you believe a child has provided us with personal data, contact [PRIVACY EMAIL] and we will
delete it.

## 11. Changes to this policy

We may update this policy. If we make a material change — in particular to how we use Google user
data — we will notify you by [email / in-product notice] before it takes effect, and update the
"Last updated" date above. Earlier versions are available at [URL] on request.

## 12. Contact us

[LEGAL ENTITY NAME]
[POSTAL ADDRESS]
[PRIVACY EMAIL]

---

## Part 3 — After you publish

1. **Put the URL in three places and keep them identical:** the footer link on your homepage, the
   privacy policy URL field on the OAuth consent screen, and the privacy policy URL in the
   verification form.
2. **Check it loads logged out, over HTTPS, as HTML.** Use a fresh browser profile.
3. **Grep your live page for leftovers:** a bare `[` or `]`, `TODO`, `Lorem`, `example.com`, and
   any unfilled placeholder from the template. Fix anything you find.
4. **Set a reminder to review it annually,** and whenever your data practices change, your
   sub-processors change, or you add a scope. A policy that describes last year's data flows is a
   policy that contradicts today's submission.
5. **Keep it consistent with the other artefacts.** The privacy policy, the app description in the
   Cloud Console, the scope justification and the demo video must tell the same story about what
   you access, store and share. Contradictions between them are the most expensive kind of
   finding, because they look like concealment rather than carelessness.
6. **Have it reviewed by a lawyer for your jurisdiction.** This template is not legal advice and
   does not attempt to be complete for any particular jurisdiction.
7. **Confirm the current Google requirements** for privacy policies for OAuth apps, because they
   change.

---

## Part 4 — Self-check

- [ ] Every `[BRACKET]` replaced; no template leftovers in the published page.
- [ ] Every scope you actually request is in the table in section 3, with a plain-English purpose.
- [ ] No scope is listed that you do not actually request.
- [ ] The Limited Use commitments in section 4 are true of your code, not just of your policy.
- [ ] Storage, sharing, retention and deletion match what you wrote in the app description and
      scope justification.
- [ ] Revocation instructions and a deletion route are both present and actually work — test them.
- [ ] Contact details are real and monitored.
- [ ] The page is linked from the homepage and reachable without logging in.
- [ ] The URL entered in the Cloud Console matches the homepage footer link exactly.
- [ ] A lawyer in your jurisdiction has reviewed the finished policy.
- [ ] You have confirmed the current published Google requirements for privacy policies of OAuth
      apps.

---

*Part of the Google OAuth Verification Submission Kit. Not legal advice. Not an official Google
document. Have a qualified lawyer review your published policy, and confirm Google's current
requirements before submitting.*
