# Rebuttal Responses — Copy-Paste Replies to "We Need More Information"

**Template:** `rebuttal-responses.md`
**Who needs this:** anyone whose submission was declined, or who has received a
"we need more information" / "your app does not comply" message and now has to answer it.
**The single most important thing in this file:** a follow-up request is almost never a judgement
on your app. It is a statement that the reviewer could not confirm something from what you sent.
Your reply should make that thing confirmable. It should not argue.

> Google's requirements, its email wording and the review workflow change. The phrasing below is
> written to be robust to rewording, but confirm the current requirements in Google's own
> documentation when you reply. This is not an official Google document and is not affiliated with
> or endorsed by Google.

---

## How to reply well

**Do:**

1. **Answer the question that was asked, first.** Open with a one-line direct answer, then the
   detail. Reviewers are working through a queue.
2. **Reply in the same thread or form field the request came from,** so the context is attached.
3. **Quote the reviewer's wording back** and label your response under it, item by item. If they
   listed four points, reply with four numbered sections in their order.
4. **Send evidence, not reassurance.** A link, a timestamp, a screenshot, a code reference, a
   published page. "We take privacy seriously" is not evidence of anything.
5. **Say what you changed,** with the URL or the timestamp where the change is visible. "We have
   added X at [URL], visible at [timestamp] in the updated video at [LINK]."
6. **Move fast.** A long silence is not interpreted generously. If you cannot answer within a few
   days, send a short holding reply saying when the full answer will come.
7. **Keep one thread, one version of the truth.** If a fact changed (you dropped a scope, you
   changed the retention period), say that it changed and why. Do not quietly alter a previous
   statement.

**Do not:**

- Argue the policy, cite competitors who you believe were approved, or explain that the
  requirement is unreasonable. It does not change the requirement.
- Resubmit the same material unchanged and hope for a different reviewer.
- Send a wall of text with no headings. Structure is a courtesy that pays.
- Invent details to close a gap — a fabricated retention period or an understated data flow is
  found later, and the cost of that is much higher than an extra review round.
- Blame your framework, your template, or an agency. The reviewer needs the fact, not the cause.

**A reply template skeleton.** Reuse this shape for every scenario below.

```
Subject: Re: [exact subject of the request] — [APP NAME], project [PROJECT ID]

Hello,

Thank you for the review. Direct answers to each point below, with links and video timestamps.

1. [Reviewer's point, quoted]
   [One-sentence direct answer.]
   [Evidence: URL, timestamp, screenshot, code reference.]
   [What changed, if anything.]

2. [Reviewer's point, quoted]
   ...

Supporting links:
  Homepage (public, no login):        [URL]
  Privacy policy (public, no login):  [URL]
  Updated demo video:                 [URL] — changed sections at [TIMESTAMPS]
  Cloud project / client ID:          [PROJECT ID] / [CLIENT ID]

We have not changed the scope list since the original submission. [Or: we removed [SCOPE] on
[DATE] because [REASON].]

Regards,
[NAME], [ROLE], [APP NAME]
```

---

## Scenario 1 — "Your homepage is not accessible, or its purpose is unclear"

**Typical wording:** the homepage URL does not load, requires a login, redirects to an unrelated
site, or does not make clear what the application does or how it uses Google user data.

**What the reviewer could not confirm:** that the app is a real, public product; that the app name
on the consent screen refers to this page; and that a privacy policy is published and reachable.

**Root causes, in order of frequency:**
- Root URL redirects to `/login` for logged-out visitors.
- Homepage is a staging or preview URL, or is geo-restricted.
- The page says what the company believes but not what the app does.
- The privacy policy link exists but points elsewhere, is a PDF, or 404s.

**Reply:**

```
1. Homepage accessibility

Our homepage at [URL] is public and requires no login. We have verified it loads for a
logged-out visitor in a clean browser profile; a screenshot of the logged-out view is attached
as [FILENAME].

On [DATE] we changed [WHAT YOU CHANGED — e.g. "the root route, which previously redirected to
/login, now serves a public landing page; the application itself is at /app"]. The change is
live now.

2. Clarity of purpose

The homepage now states in its first paragraph: "[PASTE THE SENTENCE]". This describes what
[APP NAME] does and who it is for. The section headed [SECTION NAME] describes the Google
integration: [PASTE THE RELEVANT SENTENCE].

Our app description submitted with the application says the same thing: [QUOTE IT].

3. Privacy policy

The privacy policy is linked from the homepage footer under the text "Privacy Policy" and is
published at [PRIVACY POLICY URL], which is also the URL recorded on the OAuth consent screen.
It loads without a login. It describes the Google user data we access ([LIST]), how we use it,
how we store and share it, our retention periods, and how a user deletes it. Section
"[GOOGLE USER DATA]" contains our Limited Use commitments.

4. App name

The app name shown on the consent screen is "[APP NAME]". That exact string appears in the site
header at [URL], in the page title, and in the privacy policy. [If a legal entity differs, name
it here and explain the relationship.]
```

---

## Scenario 2 — "Your privacy policy is missing required disclosures"

**Typical wording:** the privacy policy does not explain what Google user data is accessed, how it
is used or shared, how long it is retained, how a user can delete it, or does not include the
Limited Use commitments.

**What the reviewer could not confirm:** that the policy actually covers Google user data, as
opposed to general website privacy boilerplate.

**Root causes:** generic policy copied from a template site; Google data covered by one vague
sentence; no retention periods; no deletion route; Limited Use language absent.

**The fastest reliable fix is to restructure rather than patch.** Add a section literally headed
"Google user data we access", with a table of scope → what it gives → why you ask. Then explicit
retention and deletion. Then the Limited Use paragraph. `privacy-policy-template.md` in this pack
is shaped that way.

**Reply:**

```
1. What we access and why

We have added a section to the privacy policy headed "Google user data we access". It lists every
scope we request, what each one gives us access to, and the specific feature it supports:

  [SCOPE 1] — [WHAT] — [WHY]
  [SCOPE 2] — [WHAT] — [WHY]

Live at [PRIVACY POLICY URL]#google-user-data.

2. How we store and share it

Section "[SECTION]" states where the data is hosted, that it is encrypted in transit and at rest,
what we store and what we deliberately do not store, and who processes it on our behalf
([SUB-PROCESSORS]). We can confirm we do not sell Google user data and do not share it with third
parties for advertising.

3. Retention

Section "[SECTION]" now gives explicit periods per data category:
  [DATA CATEGORY] — [PERIOD]
  [DATA CATEGORY] — [PERIOD]

4. Deletion and revocation

Section "[SECTION]" explains both routes: revoking our access from the user's Google Account
(Data & privacy → Third-party apps & services), and deleting data in the product at
[ROUTE]/by emailing [EMAIL]. Deletion completes within [N] days. We have tested both paths;
screenshots attached.

5. Limited Use

Section "[SECTION]" now contains: "[PASTE THE LIMITED USE PARAGRAPH]". This is the same commitment
made in our app description. It is accurate of our implementation: we do not use Google user data
for advertising, we do not sell it, and we do not transfer it except as necessary to provide the
features described.

The policy URL recorded in the Google Cloud Console OAuth consent screen is
[PRIVACY POLICY URL], identical to the link on our homepage.
```

---

## Scenario 3 — "The video does not show the OAuth consent screen / does not show the scopes being used"

**Typical wording:** the demonstration video does not show the consent screen, does not show the
requested scopes being granted, does not show the app using the data, omits the client ID, or
omits the homepage.

**What the reviewer could not confirm:** that the scopes are granted through the real flow and that
the app genuinely consumes the data.

**Root causes:** video starts inside the app; consent flow edited or sped up; address bar cropped
or unreadable; scopes requested at sign-in but never exercised in the demo; empty-state screens;
video link private or expired.

**This is the most fixable category and the most common reason for a re-review. Re-record rather
than argue.** `demo-video-script.md` in this pack is a shot list built for exactly this.

**Reply:**

```
We have re-recorded the demonstration video: [NEW LINK]. It is unlisted but viewable without a
login, and it is a single continuous take through the consent flow.

The new video explicitly shows:

  0:00  The app homepage at [URL], loaded logged out, including the privacy policy link in the
        footer and the app name "[APP NAME]" in the site header.
  0:35  The OAuth client ID [CLIENT ID] displayed in the Google Cloud project's Credentials page
        for project [PROJECT ID].
  1:00  A full sign-in with the test account [TEST EMAIL]. The address bar is visible throughout
        and shows the authorization request, including the same client ID.
  1:20  The Google consent screen, unedited, showing the app name "[APP NAME]" and each requested
        scope as it is granted.
  2:00  [SCOPE 1] in use: I navigate to [ROUTE], which shows [DATA]. To demonstrate that this is
        read live, I add [NEW ITEM] in [GOOGLE PRODUCT] at 2:40, refresh at 2:55, and the item
        appears.
  3:30  [SCOPE 2] in use: [DESCRIPTION AND ROUTE].
  4:30  Where the user can revoke access and delete their data: [ROUTE].
  5:00  Return to the homepage and a summary of the scopes and their purpose.

Nothing in the consent flow is cut, sped up, blurred or cropped. The address bar is legible at
full resolution. The app name is identical in the video, on the consent screen, on the homepage
and in the Cloud project.
```

**If the video was fine but the link was not:** say so plainly, provide a working link, and note
that the content is unchanged. Do not re-record for a link problem, but do check the link from a
logged-out browser before you send it.

---

## Scenario 4 — "The requested scope does not appear to be used by your application"

**Typical wording:** the scope is not necessary for the functionality described, or the application
does not appear to use it.

**What the reviewer could not confirm:** a feature in the submitted material that requires this
scope. This is the most consequential rejection, because the usual correct answer is either
(a) demonstrate the feature properly, or (b) **remove the scope**.

**Before replying, do this honestly:** search your codebase for every use of the scope. If the
only hits are the request itself, a config constant, and a comment, you do not use the scope. See
the decision box below.

**Reply, when the scope genuinely is used:**

```
[APP NAME] uses [SCOPE] for the feature "[FEATURE NAME]", which is available to all users at
[ROUTE].

Flow: the user [ACTION] at [ROUTE]. The application then calls [GOOGLE API METHOD] and receives
[FIELDS], which are displayed at [ROUTE] as shown in the video at [TIMESTAMP].

In the video at [TIMESTAMP] you can see the feature populated with live data: I add a new
[ITEM] in [GOOGLE PRODUCT] at [TIMESTAMP], refresh the application at [TIMESTAMP], and the new
item appears. This call is made with the granted scope.

Implementation references:
  [FILE PATH / CLASS / FUNCTION] — [WHAT IT DOES]
  [FILE PATH] — where the scope constant is requested

Supporting screenshot attached: [FILENAME], showing [WHAT].

[If applicable:] We do not request any scope beyond what this feature and sign-in require. The
full scope list in our Cloud project is: [LIST].
```

**Reply, when you have decided to remove the scope:**

```
Having reviewed the requirement, we agree that [SCOPE] is not necessary for the functionality of
[APP NAME]. We have removed it.

On [DATE] we removed [SCOPE] from the OAuth consent screen configuration for project
[PROJECT ID], and the consent screen now requests only:
  [REMAINING SCOPE 1] — [PURPOSE]
  [REMAINING SCOPE 2] — [PURPOSE]

Related changes made at the same time:
  - Code paths that used the scope have been removed: [FILES/DESCRIPTION]
  - The privacy policy section "Google user data we access" has been updated to remove
    [SCOPE] and its description: [PRIVACY POLICY URL]
  - The app description submitted with the application now lists only the remaining scopes.
  - The demonstration video has been re-recorded and shows only the remaining scopes being
    granted and used: [NEW VIDEO LINK]

Existing users who previously granted [SCOPE] have [WHAT YOU DO — e.g. "been asked to reconnect
with the reduced scope; existing grants will be revoked at [myaccount.google.com] as part of
cleanup on [DATE]"].

We understand that removing a scope means the consent screen changes, and we have not requested
any replacement.
```

---

## Scenario 5 — "The application name does not match / does not match your homepage or consent screen"

**Typical wording:** the app name on the consent screen differs from the name on the homepage or
in the submission, or the app name is inconsistent across materials.

**What the reviewer could not confirm:** that the consent screen name refers to the reviewed
product.

**Root causes:** legal entity name used on one artefact and product name on another; a rename
during the process; a marketing tagline included in one place; different capitalisation or
punctuation; the homepage title tag differing from the visible heading.

**Reply:**

```
The application name is "[APP NAME]". We have made it identical in all of the following, and can
confirm each is now exactly that string:

  - Google Cloud project OAuth consent screen (Application name): "[APP NAME]"
  - Homepage site header and page title at [URL]: "[APP NAME]"
  - Privacy policy heading and body: "[APP NAME]"
  - Verification submission app name field: "[APP NAME]"
  - Demonstration video narration and on-screen: "[APP NAME]"

Changes made on [DATE]:
  - Homepage header previously read "[OLD STRING]"; it now reads "[APP NAME]". [URL]
  - Page title changed from "[OLD]" to "[APP NAME]".
  - [Any other artefact that changed.]

[If the app was renamed:] The product was previously known as "[OLD NAME]". We renamed it to
"[APP NAME]" on [DATE]. The old name appears nowhere in the submitted materials; [WHERE, IF
ANYWHERE, IT STILL APPEARS — e.g. "our terms of service still reference the registered company
name [LEGAL ENTITY], which is the legal entity operating the product"].

[If a legal entity is involved:] [APP NAME] is a product of [LEGAL ENTITY]. The product name is
used on the consent screen and the homepage; the legal entity name is disclosed in the footer,
terms of service and privacy policy.
```

**Do not** use this reply to explain that the names are "essentially the same". Either make them
identical or explain the relationship explicitly.

---

## Scenario 6 — "Please justify why your app requires this scope" (including "this scope appears unnecessary")

**This is the request to answer with `templates/scope-justification.md`, per scope.** Reply with
the filled block for that scope, in the reviewer's numbering, and nothing else.

```
[APP NAME] requests [SCOPE] for one feature: [FEATURE NAME].

The user story: as a [ROLE], I want [OUTCOME], so that [BENEFIT]. The data exists in
[GOOGLE PRODUCT] because [WHY — e.g. suppliers send the invoices there, not to us].

Google API methods used: [METHODS]
Fields consumed:         [FIELDS]
Fields not consumed:     [BE EXPLICIT — this is what distinguishes a considered request from a
                          blanket request]
Filtering applied:       [e.g. only messages matching [QUERY]; only files in the user-selected
                          folder]
What we write back:      [NOTHING / SPECIFIC METHODS]

Why a narrower scope cannot do this:
  - [NARROWER SCOPE 1] — does not work because [SPECIFIC REASON]
  - [NARROWER SCOPE 2] — does not work because [SPECIFIC REASON]
  - [USER-MEDIATED ALTERNATIVE — manual upload / Google Picker / file-by-file selection] — does
    not work because [SPECIFIC REASON, with a number if you have one, e.g. "customers process
    40-200 invoices a month"]
  We therefore request [SCOPE], the narrowest option that returns [THE MINIMUM NEEDED].

Where it is used in the product: [ROUTE]
Where it is demonstrated in the video: [TIMESTAMP]
Code reference: [FILE/CLASS that consumes it]
```

### Decision box — when the right answer is to drop the scope

Read this before you write the reply above. For each requested scope, ask:

| Question | If the honest answer is… | Then… |
|---|---|---|
| Is there a feature that visibly requires it? | No | Drop it |
| Does the feature exist for all users today, not "soon"? | No | Drop it until the feature ships |
| Can you name the API call and the fields you consume? | No | Investigate; if you cannot, drop it |
| Can you name a narrower scope or user-mediated alternative and say concretely why it fails? | No | Drop it — this is the answer that generates a second rejection |
| Is the scope used at sign-in rather than when the user asks for the feature? | Yes | Consider incremental authorisation instead of a blanket request |
| Is the scope restricted-tier, and would the security assessment cost more than the feature is worth? | Yes | Redesign around a narrower scope — see [SCOPE-STRATEGY.md](../docs/SCOPE-STRATEGY.md) |

**Dropping a scope is a legitimate engineering decision, not a defeat.** It removes a whole class
of rejection risk, shortens the review, and — for restricted scopes — may avoid a security
assessment entirely. If you can ship the same user outcome with a narrower scope, that is the
better product as well as the faster verification.

When you drop a scope, tell the reviewer explicitly and list every artefact you updated, as in the
second reply in Scenario 4. Reviewers respond well to a clear, self-consistent reduction.

---

## Scenario 7 — "The scope list does not match / you have changed scopes"

**Typical wording:** the scopes in the submission, the Cloud project, the video and the privacy
policy do not agree.

**Cause:** this almost always happens after a code change, a dependency update that added a scope,
or a copy-paste of an older description.

**Reply:**

```
The authoritative scope list for project [PROJECT ID] is:

  [SCOPE 1] — [PURPOSE]
  [SCOPE 2] — [PURPOSE]

We have reconciled every artefact to this list on [DATE]:

  - OAuth consent screen configuration: matches, as shown in the screenshot attached.
  - Privacy policy section "Google user data we access": matches. [URL]
  - App description in the submission: matches.
  - Demonstration video: [RE-RECORDED ON [DATE] / UNCHANGED, and previously showed only these
    scopes]. [VIDEO LINK]

[If a scope was added or removed, say when, why, and what happened to existing user grants.]

Nothing outside this list is requested by the application. Our client configuration contains no
additional scopes.
```

---

## Scenario 8 — "The security assessment is required" (restricted scopes)

**Typical wording:** your app uses restricted scopes, so a security assessment is part of the
process.

**What this is not:** a rejection. It is a statement of a requirement attached to the tier of
scope you requested.

**Do not reply with an argument that an assessment should not be needed for your app.** Instead,
before you reply at all, re-open `docs/SCOPE-STRATEGY.md` and confirm that no narrower or
non-restricted scope design delivers the same user outcome. Redesign is frequently the cheaper
route in both money and calendar time. If you conclude the restricted scope really is necessary:

```
We understand that the restricted scopes we request fall under the security assessment
requirement, and we are prepared to complete it.

Current status: [e.g. "we have not yet engaged an assessor" / "we have engaged [ASSESSOR] and
expect to submit on [DATE]"]
Owner for this work: [NAME / ROLE]
[If you have a quote:] We were quoted [FIGURE] on [DATE] by [SOURCE]; the recurring cadence we
understand applies is [CADENCE].

Relevant documentation we can provide for the assessment:
  - Data flow description for restricted scope data: [ATTACHMENT]
  - Storage, encryption and key management: [ATTACHMENT]
  - Retention and deletion, with the mechanism that enforces each: [ATTACHMENT]
  - Access control model and audit logging: [ATTACHMENT]
  - Sub-processor list: [URL]
  - Most recent penetration test summary: [ATTACHMENT / "available under NDA"]

We have also re-examined whether a narrower scope would meet the need. [State the conclusion and
the reasons, briefly and honestly.]
```

**If your honest position is "we cannot fund or complete an assessment":** say so to the reviewer
in one line and pivot to the redesign. Reviewers deal with this constantly. A clear "we are
removing the restricted scope and will resubmit with [NARROWER SCOPE]" is a clean path forward;
silence or a vague promise is not.

---

## Final self-check before you send any reply

- [ ] You answered every numbered point the reviewer raised, in their order.
- [ ] Each answer leads with the direct answer, then the evidence.
- [ ] Every claim is checkable: a URL, a timestamp, a screenshot filename, a code path.
- [ ] Every URL in the reply loads while logged out — you tested them.
- [ ] The video link works and the timestamps you cite are accurate; you re-watched it.
- [ ] The scope list is identical everywhere; you have not left an older list in any artefact.
- [ ] Anything you changed has a date, and the change is live now, not planned.
- [ ] Nothing in the reply contradicts your privacy policy or your app description.
- [ ] You did not argue with the policy, cite other apps, or explain why the requirement is
      unreasonable.
- [ ] You did not invent a retention period, a data flow or a sub-processor to close a gap.
- [ ] You sent it in the same thread or form field the request came from.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Google's
requirements and review process change; verify against current official documentation when you
reply.*
