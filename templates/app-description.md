# App Description — Fillable Template

**Template:** `app-description.md`
**Fills in:** the free-text "App description / How does your app use Google user data" fields in
the Google Cloud Console **OAuth consent screen** configuration and, where the verification form
asks again, the app description field in the verification submission.
**Time to complete:** 30–60 minutes. Do not rush this — reviewers read it before they open your video.

> **Before you start**
> Google's verification requirements and form field names change. This template follows the shape
> Google has consistently asked for, but you must confirm the current wording of the form and the
> current policy at the time you submit. See `docs/PRE-SUBMISSION-CHECKLIST.md`.
> This is not an official Google document and is not affiliated with or endorsed by Google.

---

## How to use this template

1. Copy the **filled example** at the end of this file into your own document and edit it.
2. Replace every `[BRACKETED]` placeholder. Delete any instruction block you have finished with.
3. Keep the section headings. Google's form fields map onto them and reviewers look for the same
   information in the same order. A reviewer who has to hunt for the answer is a reviewer who
   writes "insufficient information".
4. Write in the **same voice as your homepage**. If your homepage says "Acme Analytics" the form
   must say "Acme Analytics" — not "Acme Analytics, Inc.", not "the Acme platform", not "we".
   Google compares these strings; mismatches are a very common reason for a follow-up email.
5. Delete the **Anti-patterns** section from your final submission text. It is guidance for you,
   not content for Google.

---

## Section 1 — App identity block

```
App name (exactly as shown on the OAuth consent screen): [APP NAME]
Application homepage URL:                               [https://example.com]
Privacy policy URL:                                     [https://example.com/privacy]
Terms of service URL (if you have one):                 [https://example.com/terms]
Support email:                                          [SUPPORT EMAIL]
Cloud project ID:                                       [PROJECT ID]
OAuth client ID(s) shown in the demo video:             [CLIENT ID]
```

**Why the client ID line is here:** you will need the same string inside your demo video and inside
the Google Cloud Console. Copy it once, paste it everywhere, never retype it.

---

## Section 2 — What the app does (the one-paragraph answer)

> Write 3–6 sentences. No marketing adjectives. No "revolutionary", "seamless", "AI-powered
> synergy". A reviewer is trying to answer one question: *can I understand what this product does
> well enough to judge whether it needs these scopes?*

**Template:**

```
[APP NAME] is a [CATEGORY, e.g. web application / desktop application / mobile application]
that helps [TARGET USER, e.g. small finance teams] [DO THE CONCRETE JOB, e.g. reconcile
monthly invoices against bank statements]. A user signs in with their Google Account and
[THE ONE THING THAT REQUIRES GOOGLE DATA, e.g. the app reads the invoices already sitting in
their Google Drive folder so they do not have to upload them by hand]. The app then
[WHAT IT PRODUCES, e.g. produces a reconciliation report the user can export as a PDF].
We do not sell, resell, or share Google user data, and we do not use it for advertising.
```

**Good:** "Ledgerly is a web app for small finance teams. Users sign in with Google and the app
reads invoice PDFs from a Drive folder the user selects, so nobody has to upload them manually.
The output is a monthly reconciliation report."

**Bad:** "Ledgerly is a next-generation, AI-driven financial intelligence platform that
seamlessly unlocks the power of your data." — This says nothing, and it makes the scope request
look bigger than it is.

---

## Section 3 — Who the app is for

```
Primary users:      [e.g. bookkeepers and finance managers at companies with 5-50 employees]
Where they are:     [e.g. United Kingdom, Ireland]
How they sign up:   [e.g. self-service, Google Sign-In is the only sign-in method]
Approximate user count today: [NUMBER]
```

**Note on user count:** Give an honest number, including test users. If your number is small, that
is fine and normal for a new app. Inflating it and being contradicted by your Cloud project's own
analytics causes a credibility problem you cannot recover from in the same thread.

---

## Section 4 — How each scope is used

This is the section reviewers actually grade. One block per scope you request. Use one row per
scope; do not group scopes together to save space.

**Template row (repeat for every scope in your request):**

```
Scope:                    [FULL SCOPE STRING, e.g. https://www.googleapis.com/auth/drive.readonly]
Classification:           [Non-sensitive / Sensitive / Restricted — CONFIRM against Google's
                           current published lists before filling this in; see the caveat below]
Where the user sees it:   [e.g. "Connect Drive folder" screen, step 2 of onboarding]
What we read:             [e.g. the file names and contents of PDFs in one user-selected folder]
What we do with it:       [e.g. parse line items into the reconciliation table]
What we write back:       [e.g. nothing, or "an export file into the same folder"]
Why a narrower scope cannot do this: [e.g. drive.file does not cover files the user created
                           outside our app; we need the folder the user already has]
Where in the product this happens: [SCREEN NAME / URL PATH]
Where in the demo video this is shown: [TIMESTAMP, e.g. 01:42]
```

### Filling "why a narrower scope cannot do this" honestly

This line is the single highest-value sentence in the whole submission, and the single easiest
one to get wrong. Two outcomes:

- **You can write a specific, concrete reason.** Good. Say it plainly.
- **You cannot write one.** Then you probably do not need the scope. Go to
  `docs/SCOPE-STRATEGY.md` and consider dropping it before you submit, rather than writing
  filler here. A dropped scope costs you an afternoon. A scope you cannot justify costs you a
  rejection and a re-review cycle.

**Do not** write "for a better user experience" or "to provide core functionality" or "required
for the app to work". Every rejected submission contains at least one of those phrases.

---

## Section 5 — How Google user data is stored, transmitted, and shared

Reviewers ask this in the form and in follow-up emails. Answer it once, properly, here.

```
Storage location:        [e.g. AWS eu-west-1, Postgres RDS, encrypted at rest with AES-256]
Transmission:            [e.g. TLS 1.2+ for all API calls between our servers and Google]
Access tokens:           [e.g. stored encrypted in our database, accessible to the API service only]
Refresh tokens:          [e.g. same, with rotation; revoked on user request]
What we cache:           [e.g. Drive file metadata cached for 24h to avoid repeat API calls;
                          file bodies are streamed and never persisted]
Sub-processors:          [e.g. AWS (hosting), Stripe (payments - does not receive Google data)]
Third parties that receive Google user data: [e.g. none]
Human access to user data: [e.g. no employee can read user content; production DB access is
                          break-glass only and logged]
Retention:               [e.g. cached metadata 24 hours; user content until the user deletes it
                          or deletes their account, then purged within 30 days]
Deletion:                [e.g. in-app "Delete account" wipes all data; also supported by emailing
                          [SUPPORT EMAIL], actioned within 30 days]
```

**Be exact about "none".** If a sub-processor does touch Google user data, name it here. Discovered
omissions are treated far worse than disclosed ones. If you are unsure whether a vendor touches
the data, ask the vendor or assume it does and disclose it.

---

## Section 6 — The Limited Use statement

Paste this verbatim, filling the brackets. It mirrors the commitments Google's API Services User
Data Policy asks for; it belongs in your submission *and* in your privacy policy
(`privacy-policy-template.md` covers the same ground).

```
[APP NAME]'s use of information received from Google APIs will adhere to the Google API Services
User Data Policy, including the Limited Use requirements. Specifically:

- We only request Google user data that is necessary to provide or improve
  [THE USER-FACING FEATURES NAMED IN SECTION 2].
- We do not transfer Google user data to third parties except as necessary to provide or improve
  those features, to comply with applicable law, or as part of a merger, acquisition, or sale of
  assets with prior notice to users.
- We do not use Google user data for advertising, including retargeting, personalised advertising,
  or interest-based advertising.
- We do not sell Google user data.
- We do not allow humans to read Google user data unless we have the user's affirmative agreement
  for specific messages, it is necessary for security purposes such as investigating abuse, it is
  necessary to comply with applicable law, or it is for our internal operations in a way that the
  data has been aggregated and anonymised.
- We do not use Google user data to determine creditworthiness or for lending purposes.
```

**Do not put this in only one place.** It has to be true of your code, stated in the submission, and
stated in the privacy policy. A reviewer reading a privacy policy that contradicts the submission
is a reviewer who sends the follow-up email you are trying to avoid.

---

## Section 7 — Anti-patterns (delete this section from your submission)

| Anti-pattern | Why it costs you a round |
|---|---|
| Describing the company's mission instead of the app's function | The reviewer cannot map mission statements to scope necessity |
| Vague scope reasons ("core functionality", "better UX") | Reads as "we did not think about it" |
| Scope list that does not match the Cloud project exactly | Instant mismatch; verify both lists side by side |
| Different app name in the form, on the homepage, and on the consent screen | This is checked mechanically before a human reads anything |
| Claiming you store nothing when you cache API responses | Caching is storage; disclose the retention window |
| Writing "we will only use it for X" without saying what happened to Y | Reviewers ask about what you collect, not what you promise |
| Copying another company's description | Reviewers read these all day; it reads as evasive and it will not match your video |

---

## Worked example — a filled-in description

Fictional app, shown complete so you can copy the shape. Replace every detail with your own.

```
App name:            Ledgerly
Homepage:            https://ledgerly.example
Privacy policy:      https://ledgerly.example/privacy
Terms of service:    https://ledgerly.example/terms
Support email:       support@ledgerly.example
Project ID:          ledgerly-prod
Client ID:           000000000000-EXAMPLE.apps.googleusercontent.com

WHAT THE APP DOES
Ledgerly is a web application for bookkeepers and finance managers at small companies. A user
signs in with their Google Account and connects one Google Drive folder containing supplier
invoices. Ledgerly reads the PDFs in that folder, extracts invoice number, supplier, date and
total, and presents a monthly reconciliation table the user can export to CSV. Users do not
upload files and do not type invoice data by hand. Ledgerly does not sell, resell or share
Google user data and does not use it for advertising.

WHO IT IS FOR
Bookkeepers and finance managers at companies with 5-50 employees, based in the United Kingdom
and Ireland. Sign-up is self-service; Google Sign-In is one of two sign-in options.
Approximate user count today: 240.

SCOPES

Scope 1
  Scope:                 https://www.googleapis.com/auth/drive.readonly
  Classification:        Restricted. (Confirm against Google's current published restricted scope
                         list before submitting; classifications have changed before.)
  Where the user sees it: The "Connect your invoice folder" screen during onboarding.
  What we read:          Names of the PDF files in the single folder the user picks with the
                         Google folder picker, and the contents of those PDFs.
  What we do with it:    Extract invoice number, supplier, date and total into the
                         reconciliation table.
  What we write back:    Nothing. The app never writes to Drive.
  Why a narrower scope cannot do this: The invoices are created by suppliers and arrive in the
                         user's Drive before Ledgerly is installed, so drive.file (which covers
                         only files our app created or the user opened through our app) does not
                         cover them. We request read-only access and never write.
  Where in the product:  /onboarding/connect-drive and /invoices
  Shown in the video at: 01:42 - 03:10

Scope 2
  Scope:                 https://www.googleapis.com/auth/userinfo.email
  Classification:        Non-sensitive, per Google's published OAuth scope list. Confirm current
                         status before submitting.
  Where the user sees it: Standard Google Sign-In.
  What we read:          The user's email address and whether it is verified.
  What we do with it:    Create the account and identify the user on later visits. The email
                         address is also the address we send the monthly report summary to.
  What we write back:    Nothing.
  Why a narrower scope cannot do this: It is already the narrowest scope that returns an email
                         address. We do not request profile or openid beyond what sign-in needs.
  Where in the product:  /login
  Shown in the video at: 00:35 - 01:20

DATA HANDLING
Storage:      AWS eu-west-1. Postgres with encryption at rest. Invoice content is parsed in
              memory and the extracted fields are stored; the original PDFs are stored in S3
              with SSE-S3 for 90 days so users can re-export, then deleted by a scheduled job.
Transmission: TLS 1.2+ for all traffic, including all calls between our servers and Google APIs.
Tokens:       Access and refresh tokens stored encrypted (AES-256-GCM, key in AWS KMS),
              readable only by the API service. Refresh tokens are revoked on account deletion.
Cache:        Drive file metadata cached for 24 hours to reduce API calls. Cached entries are
              deleted by the same job that expires them.
Sub-processors: AWS (hosting and storage). Stripe (payments only; receives no Google user data).
Third parties receiving Google user data: none.
Human access: No employee can read user content. Production database access requires a
              break-glass role, is time-limited and is logged.
Retention:    Extracted invoice fields until the user deletes the invoice, deletes the folder
              connection, or deletes their account. Original PDFs 90 days. Cache 24 hours.
Deletion:     An in-app "Delete account" control immediately revokes our Google tokens and
              queues all user data for purge, completed within 30 days. Users can also email
              support@ledgerly.example. Both paths are described in the privacy policy.

LIMITED USE
Ledgerly's use of information received from Google APIs will adhere to the Google API Services
User Data Policy, including the Limited Use requirements. [then the six bullets from Section 6]
```

---

## Final self-check before you paste this into the form

- [ ] Every `[BRACKET]` replaced. Search the document for `[`.
- [ ] App name string is identical in: this document, the consent screen config, the homepage
      `<title>`/heading, the privacy policy, and the video.
- [ ] The scope list here matches the scope list in the Cloud project exactly, including
      `https://` and the `www.googleapis.com` host.
- [ ] Every scope has a "shown in the video at" timestamp that is actually true.
- [ ] Section 5 says something concrete about retention and deletion. "We keep it as long as
      needed" is not an answer.
- [ ] Section 7 (anti-patterns) deleted.
- [ ] The Limited Use paragraph is also present in your live privacy policy.
- [ ] You have confirmed your scope classifications and the current form fields against Google's
      current published documentation, not against this template.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Google's
requirements change; verify against current official documentation before submitting.*
