# Scope Justification — One Fillable Block Per Scope

**Template:** `scope-justification.md`
**Fills in:** the per-scope justification the verification form asks for, and the corresponding
text you will paste into follow-up emails when a reviewer asks "please explain why your app
requires scope X".
**Why this file exists:** this is where most submissions die. An app description can be fuzzy and
still pass. A scope justification cannot. The reviewer is deciding one thing per scope: *is this
access necessary for the features the app actually delivers?*

> **Read this before you write anything**
> Scope classifications (non-sensitive / sensitive / restricted) are set by Google and have
> changed. Nothing in this template tells you which bucket a given scope is in. Look up every
> scope you use in Google's current published OAuth scope lists and record the result yourself.
> Getting a classification wrong — particularly treating a restricted scope as merely sensitive —
> can cost you weeks and, for restricted scopes, a security assessment. See `docs/SCOPE-STRATEGY.md`.
> This is not an official Google document and is not affiliated with or endorsed by Google.

---

## The three tiers, and why the bar is different

Google's verification load depends on which tier your scopes fall in. The tiers are not a
difficulty slider; they are three different processes.

### Non-sensitive scopes

The lightest touch. Apps using only these (for example basic sign-in related scopes) generally
do not go through the sensitive/restricted scope verification process. **Branding verification is a
separate thing** and may still apply if your app shows its name and logo on the consent screen.
Confirm the current boundary between non-sensitive and sensitive against Google's current scope
list — scopes have moved between tiers.

**What the justification needs:** very little, because you should not be requesting anything here
that you do not obviously need. State what it returns and what you do with it in one or two lines.

### Sensitive scopes

These give access to Google user data that Google considers private — mailbox content and metadata,
calendar data, file storage, and similar. Using a sensitive scope means:

- your app must complete **verification** before it can be published for general use with that
  scope, and users of an unverified app may see a warning screen;
- you must supply the app description, homepage, privacy policy and a demonstration video that
  shows the scope actually being used;
- Google may ask follow-up questions, and you should expect at least one round of them.

**What the justification needs:** a specific, concrete, feature-level reason. Not "we need to read
email". Instead: "when a user forwards a supplier invoice to invoices@ourapp.example, we read that
message's body and attachments to create an expense record. We request read-only access and we do
not modify or send mail."

### Restricted scopes

The heaviest tier. Restricted scopes are the subset Google holds to the highest bar — broad access
to Gmail, Drive, and similar.

Using a restricted scope means, in addition to everything above:

- **A security assessment is part of the requirements.** Third-party assessment of your app's
  handling of restricted-scope data is required for apps using restricted scopes. Google's
  published material points at its own assessment programme for this.
- **The assessment is not free and not instant.** Historically it has involved third-party
  assessors and a fee, and it recurs on an annual basis. **Do not budget from a number in this
  document** — pricing and cadence are set by Google and its assessors and change. Get the current
  figures from Google's published restricted-scope and security-assessment documentation before
  you commit to a restricted scope.
- **A security assessment is not the same thing as a code review by a friendly engineer.** It
  covers things like data flows, storage, retention, encryption, deletion, access controls, and
  vulnerability management. You need to be able to *evidence* these, not just claim them.

**What the justification needs:** all of the sensitive-tier material, plus an honest account of why
the restricted tier specifically is unavoidable — and then the material in the "restricted scope
addendum" below, which is what the security assessment will pick apart.

**The strategic point, stated plainly:** redesigning your integration to use a narrower or
non-restricted scope is very often cheaper in money and time than completing a restricted-scope
security assessment. Go and read `docs/SCOPE-STRATEGY.md` before you spend an afternoon writing the
justification below. The best justification is the one you did not have to write because you
dropped the scope.

---

## Block A — Non-sensitive / narrow scope

One block per scope. Copy the whole block, fill it, keep the heading numbering consistent.

```
A[N]. Scope: [FULL SCOPE STRING]

Classification as published by Google at time of writing this submission:
  [Non-sensitive / Sensitive / Restricted]. Verified on [DATE] against Google's current
  published OAuth scope list at [URL YOU CHECKED].

What the user has to do to trigger this request:
  [e.g. click "Sign in with Google" on /login]

Why it cannot be avoided:
  [e.g. This is our only sign-in method; it is the minimum needed to identify the account.
   The scope returns the user's email address and nothing else.]

What we receive:
  [Exact fields. e.g. email address, email_verified boolean, and the OpenID subject identifier.]

What we store and for how long:
  [e.g. email address and subject identifier for the life of the account; deleted within 30 days
   of account deletion.]

What we do NOT do with it:
  [e.g. We do not send email on the user's behalf. We do not access any other Google service with
   this scope. We do not use it for advertising or profiling.]

Where it appears in the product: [SCREEN / ROUTE]
Shown in the demo video at:      [TIMESTAMP]
Supporting evidence attached:    [e.g. screenshot of /login, screenshot of the consent screen,
                                  link to the code that consumes the scope: [REPO PATH or LINE]]
```

---

## Block B — Sensitive scope

```
B[N]. Scope: [FULL SCOPE STRING]

Classification as published by Google at time of writing this submission:
  [Sensitive]. Verified on [DATE] against Google's current published sensitive scope list at
  [URL YOU CHECKED].

THE FEATURE THIS ENABLES (name it, then describe it in user terms)
  Feature name:  [e.g. "Forward-to-expense"]
  User story:    As a [USER ROLE], I want [OUTCOME] so that [BENEFIT]. The data arrives from
                 [WHERE IN GOOGLE'S SERVICES] because [WHY IT IS ALREADY THERE, e.g. suppliers
                 send invoices to the user's Gmail address, not to us].

WHAT WE READ, IN DETAIL
  Google API methods called:  [e.g. users.messages.list, users.messages.get]
  Fields consumed:            [e.g. message id, internalDate, payload headers Subject and From,
                               and attachments with MIME type application/pdf]
  Fields ignored:             [Be explicit. e.g. We do not read or store message bodies of
                               messages that do not match the label filter [LABEL].]
  Filtering applied:          [e.g. Gmail search query "label:invoices has:attachment filename:pdf"
                               — we only ever fetch matching messages.]

WHAT WE WRITE
  [e.g. Nothing. We request a read-only scope and make no write calls in production. If your app
   writes, say exactly which methods and what they write.]

DATA FLOW, END TO END
  1. User clicks [ACTION] at [ROUTE].
  2. We request scope [SCOPE] via the consent screen shown in the video at [TIMESTAMP].
  3. On grant, we call [METHOD] and receive [FIELDS].
  4. We [TRANSFORM] in memory and store [WHAT] at [WHERE] for [HOW LONG].
  5. We display it at [ROUTE] — shown in the video at [TIMESTAMP].
  6. On [TRIGGER], we delete it by [MECHANISM].

WHY NO NARROWER SCOPE WORKS
  Candidates we evaluated:
    - [CANDIDATE 1] — rejected because [SPECIFIC REASON, e.g. it only returns messages our app
      itself sent, and the invoices are sent by third parties.]
    - [CANDIDATE 2] — rejected because [SPECIFIC REASON, e.g. it returns only metadata headers
      and we need the attachment body to extract the invoice total.]
    - [USER-MEDIATED ALTERNATIVE, e.g. Google Picker / manual upload / share-a-link] — rejected
      because [SPECIFIC REASON, e.g. it requires the user to hand-pick every message, and
      suppliers send 40-200 invoices per customer per month.]
  Chosen: [SCOPE], which is the narrowest scope that returns [THE MINIMUM NEEDED].

MINIMISATION ALREADY IMPLEMENTED
  [e.g. We request only the read-only variant. We apply the label filter above so we never fetch
   non-invoice mail. We fetch only attachment parts, never full message bodies. We store extracted
   fields, not raw content.]

COMPLIANCE WITH LIMITED USE
  [APP NAME]'s use of information received from Google APIs adheres to the Google API Services
  User Data Policy, including the Limited Use requirements. We do not use this data for
  advertising, we do not sell it, we do not transfer it except as necessary to provide or improve
  the feature above, and we do not permit human review except as the policy allows. The full
  commitment appears in our privacy policy at [PRIVACY POLICY URL] and in the app description
  submitted with this application.

Where it appears in the product: [SCREEN / ROUTE]
Shown in the demo video at:      [TIMESTAMP RANGE — must show the grant AND the feature working]
Supporting evidence attached:    [screenshots, code references, a link to the specific class or
                                  handler that consumes the scope]
```

---

## Block C — Restricted scope

Everything in Block B, plus the following. Keep the addendum as a separate, clearly labelled part;
Google's assessors and reviewers read it separately from the consumer-facing justification.

```
C[N]. Scope: [FULL SCOPE STRING]

Classification as published by Google at time of writing this submission:
  [Restricted]. Verified on [DATE] against Google's current published restricted scope list at
  [URL YOU CHECKED]. We understand that the restricted scope list and the security assessment
  requirements are set by Google and may change.

--- PART C1: CONSUMER-FACING JUSTIFICATION ---
  [Complete the whole of Block B here, unchanged. Do not shorten it because the scope is
   restricted; reviewers still need the feature-level story.]

--- PART C2: WHY THE RESTRICTED TIER IS UNAVOIDABLE ---
  We use the restricted variants because:
    [Be brutally specific. e.g. "The reconciliation feature must read invoice PDFs that suppliers
     email directly to the user. We cannot require the user to forward each one, and we cannot
     read attachments with a metadata-only scope. We therefore need [SCOPE]."
     If the honest answer is "we could redesign to use [NARROWER SCOPE] but have not", STOP. Go
     and evaluate the redesign first; it is usually cheaper than the assessment.]

  Redesign options considered and why we did not take them:
    - [OPTION] — cost to implement [X], impact on users [Y]. Rejected because [REASON].
    - [OPTION] — rejected because [REASON].

--- PART C3: DATA HANDLING FOR ASSESSMENT ---
  This is the material a security assessment will examine. Answer it as evidence, not as promises.

  Data categories held:      [e.g. message metadata, attachment content, extracted invoice fields]
  Storage systems:           [e.g. Postgres (extracted fields), S3 (attachments, 90 days)]
  Encryption in transit:     [e.g. TLS 1.2+ everywhere, including to Google APIs; HSTS enabled]
  Encryption at rest:        [e.g. AES-256 at the storage layer; application-level AES-256-GCM for
                              tokens with keys in AWS KMS; key rotation every [PERIOD]]
  Access control:            [e.g. least-privilege IAM; no standing human access to user content;
                              break-glass role with approval, time limit and audit log]
  Logging and monitoring:    [e.g. all API calls to Google logged with request id and user id but
                              no content; alerts on anomalous access volume]
  Vendor / sub-processor list with data touched: [one line per vendor]
  Retention schedule:        [per data category, with the mechanism that enforces it]
  Deletion mechanism:        [what happens on user request, on account deletion, and on
                              termination of the customer contract; how you verify the purge]
  Incident response:         [who is paged, in what window, and how users and Google are notified.
                              Point at a real document or just describe the actual practice honestly.]
  Vulnerability management:  [dependency scanning, patch SLAs, whether you have had a penetration
                              test, when, by whom, and whether the report is shareable]
  Secure development:        [code review requirement, secrets handling, environment separation]
  Sub-processor security:    [what you require contractually of vendors that touch this data]

--- PART C4: SECURITY ASSESSMENT STATUS ---
  Assessment route:      [e.g. the assessment is arranged through Google's published restricted
                          scope / security assessment process]
  Assessor:              [name, if engaged — otherwise "not yet engaged"]
  Current status:        [e.g. not started / questionnaire in progress / report submitted]
  Fee and cadence:       [DO NOT GUESS. State the figure you were actually quoted, with the date
                          and the source. Google and its assessors set these and they change.]
  Annual re-assessment:  [acknowledge that the requirement recurs, and say who owns it internally]

--- PART C5: EVIDENCE INDEX ---
  Reference evidence rather than asserting it. Reviewers and assessors both follow links.
    - Privacy policy showing Limited Use language: [URL]
    - Data retention and deletion documentation: [URL or attachment]
    - Security page / trust page: [URL]
    - Architecture diagram: [attachment name]
    - Sub-processor list: [URL]
    - Penetration test summary: [attachment name, or "available under NDA on request"]
```

---

## The "drop the scope" decision, in the middle of writing

At any point while filling in Block B or C, if one of these is true, stop and reconsider the scope
instead of finishing the block:

- Your "why no narrower scope works" section is getting longer than two concrete bullets.
- Your honest first draft contained the words "future", "might", "plan to", or "will eventually".
- The feature that needs the scope is used by a minority of users, or is behind a flag, or is not
  in your demo video.
- You are requesting the scope at sign-in rather than at the moment the user asks for the feature
  (see incremental authorisation in `docs/SCOPE-STRATEGY.md`).
- You cannot point at the exact code that consumes it.

Dropping a scope before submitting is a normal, respectable engineering decision. It is much
cheaper than a rejection, and much much cheaper than a restricted-scope security assessment.

---

## Per-scope self-check

Run this for every block before submitting.

- [ ] Scope string copied exactly from the Cloud Console, including scheme and host.
- [ ] Classification looked up in Google's current published list **today**, with the date and URL
      written into the block.
- [ ] The scope appears in the consent screen in the video, and the video timestamp is correct.
- [ ] The feature that consumes it is visible in the video using real data.
- [ ] "Why no narrower scope works" names at least one narrower scope or user-mediated alternative
      that you genuinely considered.
- [ ] Nothing in the block says "core functionality", "better user experience", "future
      features", or "required for the app to work".
- [ ] Retention and deletion are stated with numbers.
- [ ] The Limited Use paragraph matches your live privacy policy word for word in substance.
- [ ] For restricted scopes: C2 through C5 are complete, and you have current figures for
      assessment cost and cadence from Google's own documentation rather than from memory.
- [ ] Someone who is not you has read the block and can explain the feature back to you.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Scope
classifications and assessment requirements are set by Google and change; verify against current
official documentation before submitting.*
