# Common Rejections — Symptom, Cause, Fix

**What this document is:** a catalogue of the recurring failure patterns that cause OAuth verification
submissions to be declined or sent back for more information, organised so you can find your symptom
and go straight to the fix.

**What this document is not:** a source of statistics. **I am not claiming an official rejection
rate, an approval rate, or a ranking based on measured data**, because I do not have any. No
rejection rate and no approval rate is stated or implied anywhere in this file. These are the
recurring patterns that show up again and again in how developers describe their submissions being
declined, and in what Google's own requirement documentation asks for. Treat the ordering as
"check these first", not as a frequency claim.

> Google's requirements change. Each entry below names the requirement in conceptual terms; **confirm
> the current wording and the current requirement in Google's own documentation before you act on
> any of it.** This is not an official Google document and is not affiliated with or endorsed by
> Google.

---

## How to read the entries

Each failure mode has five parts:

- **Symptom** — what the message you received actually says, or what you observe.
- **Cause** — what the reviewer could not confirm, which is almost always something more specific
  than the words in the message.
- **Fix** — what to change. Prefer fixes that change the artefact, not the wording of your reply.
- **Prevention** — what to do before the next submission so it does not recur.
- **Evidence to send** — what to attach when you reply.

---

## 1. Identity mismatch (the app name does not match)

**Symptom.** "The application name on the OAuth consent screen does not match the name of your
application on your homepage" (or the name in the submission, or the name in the video).

**Cause.** Four artefacts carry your app's name and they have drifted apart. The usual culprits:
the legal entity name ("Acme Analytics Ltd") on one artefact and the product name ("Acme
Analytics") on another; a marketing tagline appended in one place; a rename that was applied
everywhere except the consent screen; different capitalisation or punctuation; the visible heading
differing from the `<title>`.

**Fix.**
1. Choose the exact string. Write it down. It is the product name, not the legal entity.
2. Apply it to: the consent screen "Application name" field, the homepage visible heading, the
   homepage `<title>`, the privacy policy heading and body, the submission's app name field, and the
   video (narration and any on-screen text).
3. If a legal entity genuinely operates the product, disclose the relationship explicitly in the
   footer, terms and privacy policy, and say so in your reply. Do not use the legal entity as the
   consent screen name.

**Prevention.** Settle the name *before* submitting. A rename after verification means redoing
identity work and re-recording your video.

**Evidence to send.** A screenshot of the consent screen configuration, a screenshot of the
homepage header, and the privacy policy URL — all showing the identical string — plus a one-line
statement of the relationship if a legal entity is involved.

---

## 2. Homepage not accessible, or its purpose unclear

**Symptom.** "We could not verify your homepage" / "your homepage does not describe your
application" / "the homepage requires a login".

**Cause.** The reviewer visited the URL you gave and could not establish that a real, public product
exists. Causes in rough order of frequency: the root URL redirects a logged-out visitor to `/login`;
the URL is a staging or preview host; the page is a waitlist or "coming soon" placeholder; the page
describes the company's mission rather than what the app does; the domain is geo-blocked; the page
is client-rendered and blanked by a JavaScript error on the reviewer's browser.

**Fix.**
1. Serve a public landing page at the root of the URL you submitted. Move the authenticated app to
   `/app`, `/dashboard` or a subdomain.
2. State in one plain sentence what the app does and who it is for. Then state how it uses Google
   data.
3. Test in a clean browser profile with no cookies, no session, and no extensions.

**Prevention.** Put "does the homepage explain the product to a stranger with no account?" in your
launch checklist, not in your verification checklist.

**Evidence to send.** A screenshot of the page as a logged-out visitor, the exact sentence that
describes the app, and the URL of the changes you made with the date.

---

## 3. Privacy policy missing required disclosures

**Symptom.** "Your privacy policy does not explain how you use Google user data" / "we could not
find a privacy policy" / "the privacy policy does not include the required information".

**Cause.** Two distinct problems, and the message sometimes does not distinguish them:
- **The policy is not findable.** No link on the homepage, the link text is "Legal" or an icon, the
  link resolves to a PDF that will not render, or the link 404s.
- **The policy does not cover Google user data.** It is a generic website policy that mentions
  cookies and analytics and never says what Google user data you access, how you use it, how it is
  stored or shared, how long you keep it, how a user deletes it, or the Limited Use commitments.

**Fix.**
1. Add a link on the homepage whose visible text is "Privacy Policy". Same URL as the one on the
   consent screen.
2. Publish the policy as HTML on your own domain, reachable without a login.
3. Add a section literally headed "Google user data we access", containing: every scope you request,
   what each one gives you, and the feature it supports.
4. Add explicit retention periods per data category, a deletion route (in-product and by email), and
   the revocation steps in the user's Google Account.
5. Add the Limited Use commitments.
6. Make sure every statement matches your app description and your actual implementation.

**Prevention.** Write the policy from your scope list, not from a template site. Use
`privacy-policy-template.md` as the structure and have a lawyer review it.

**Evidence to send.** The URLs, the section headings, and a quotation of the added text. If retention
or deletion claims are new, say what mechanism enforces them.

---

## 4. Video does not show the consent screen, the scopes, or the client ID

**Symptom.** "Your video does not show the OAuth consent screen" / "the video does not demonstrate
the use of the requested scopes" / "we were unable to confirm the client ID".

**Cause.** The video is a demonstration, not a tour of the finished product. The usual specific
omissions: recording started inside the app so the sign-in is never shown; the consent flow was cut
or sped up; the address bar was cropped out or unreadable; the scopes were granted but the features
using them were never exercised, so the reviewer saw empty screens; the client ID appears nowhere;
the video is private or expired.

**Fix.** Re-record from `demo-video-script.md`. Do not argue; a re-record is faster than a
discussion. Ensure the finished video shows, in one continuous unedited take through the consent
flow:
- the homepage loaded publicly, with the privacy policy reachable from it;
- the client ID, visible in the Cloud Console and in the authorization request URL;
- the real consent screen with a legible address bar;
- each requested scope being granted;
- each scope's feature in use, with real non-empty data;
- a live API call (add an item, refresh, show it appear).

**Prevention.** Rehearse the video before you submit. Watch your own export at normal speed on a
laptop, with the acceptance list in front of you.

**Evidence to send.** The new video link, a list of the timestamps for each required element, and a
statement that the consent flow is unedited.

---

## 5. Scope does not appear to be used by the application

**Symptom.** "We could not verify that your application uses [SCOPE]" / "please explain why your
application requires this scope" / "this scope does not appear necessary for the functionality
described".

**Cause.** The reviewer could not connect the scope to a feature. Either the feature exists and was
not demonstrated, or the scope genuinely is not used. Common specific causes: the scope is requested
at sign-in as a "just in case" and the feature is behind a flag or not built; a dependency
transitively added the scope; the feature exists but the video showed an empty state; the
justification describes the product category rather than the specific operation.

**Fix.**
1. **Grep your codebase for the scope.** If the only occurrences are the constant and the config,
   you do not use it. Drop it and say so.
2. **If you do use it,** write the specific justification from `scope-justification.md`: the API
   method, the fields consumed, the fields deliberately not consumed, any server-side filter you
   apply, and the concrete reason a narrower scope or a user-mediated alternative does not work.
3. **Fix the video** so the feature is visibly exercised with live data.
4. **If you drop the scope,** list every artefact you updated: Cloud project configuration, code,
   privacy policy, app description, video. A clean, self-consistent reduction is a strong reply.

**Prevention.** Before submitting, run the decision test in `docs/SCOPE-STRATEGY.md` §8 on every
scope. Anything without a feature and an API call gets dropped before the reviewer ever sees it.

**Evidence to send.** Code references to the call site, the video timestamp where the feature is
used, a screenshot of the populated feature, and either the narrower-alternative reasoning or the
statement that the scope has been removed with the date.

---

## 6. Request for an unnecessary scope

**Symptom.** "Please justify why your application requires [SCOPE]" / "the requested scope appears
to exceed what is necessary for the functionality described" / "consider whether a narrower scope
would meet your needs".

**Cause.** This is the reviewer's version of the narrowing question. It is usually triggered by the
breadth of the request (all files, all mail, read-write where read-only would do), by requesting
everything at sign-in, or by a justification that does not mention the narrower alternatives you
considered.

**Fix — and this is the entry where "the fix" is often to remove the scope.**
1. Ask the five questions in `templates/rebuttal-responses.md` scenario 6 decision box. In
   particular: is there a per-file or picker-based scope that reaches the data? Is a read-only
   variant enough? Could the user hand you the specific object instead?
2. If a narrower option works, **switch to it** and say so. Re-run the classification lookup on the
   new scope: a narrower scope may sit in a lower tier, which may remove the video requirement, the
   security assessment, or both.
3. If no narrower option works, say exactly why, with detail: how the data arrives, who created it,
   why the user cannot select it, and what volume is involved.
4. If the scope is restricted-tier, re-cost the redesign against the assessment before replying. See
   `docs/SCOPE-STRATEGY.md` §7.

**Prevention.** Choose the narrowest scope at design time, and record the alternatives you rejected
while the reasoning is fresh. Retro-fitting a narrowing story after a rejection is much more
expensive than designing narrow from the start.

**Evidence to send.** The alternatives you evaluated and the specific reason each fails; the API
methods and fields you consume; the filter that restricts what you fetch; and, if you narrowed, the
updated scope list plus every artefact you changed.

---

## 7. Scope list inconsistent across artefacts

**Symptom.** "The scopes in your submission do not match the scopes configured for your project" /
"the video does not show all of the requested scopes".

**Cause.** Drift. Usually caused by a code change or dependency change during the review; by copying
an older description into the form; by adding a scope to the console after filming; or by an
artefact that was never updated when a scope was removed.

**Fix.** Produce one authoritative list from the Cloud project configuration and reconcile everything
to it: the consent screen, the justification, the privacy policy's Google section, the homepage if
it names the access, the app description, and the video. If the video no longer matches, re-record
it.

**Prevention.** Freeze the scope list before you film. Any scope change after that point restarts the
artefact updates — which is why scope changes belong in a change process, not in a quick console
tweak during review.

**Evidence to send.** The authoritative list, a screenshot of the consent screen configuration, and
a statement of which artefacts were updated and when.

---

## 8. Restricted-scope security assessment requirement raised

**Symptom.** The reviewer or the process indicates that because your app uses restricted scopes, a
security assessment applies.

**Cause.** You requested a restricted-tier scope. This is a requirement of the tier, not a judgement
on your app.

**Fix.** This is the entry where the cheapest fix is frequently architectural. Before you reply:
1. Re-read `docs/SCOPE-STRATEGY.md` §8 and confirm that no narrower, non-restricted or non-Google
   design achieves the same user outcome. Cost the redesign against the assessment in a spreadsheet.
2. If a redesign works, take it and tell the reviewer you have removed the restricted scope, listing
   every artefact you updated.
3. If the restricted scope is genuinely necessary, commit to the assessment deliberately: engage the
   process, budget the fee and the annual recurrence from **current published figures obtained from
   Google or its assessors**, and start gathering the evidence in Part C3 of
   `templates/scope-justification.md` — you will need the same material for the assessment.
4. If you cannot fund or complete an assessment, say so plainly and pivot to the redesign rather
   than going quiet.

**Prevention.** Decide the restricted-scope question before you write integration code.

**Evidence to send.** If redesigning: the new scope list and the artefacts updated. If proceeding:
your assessment status, the owner, and the evidence pack.

---

## 9. App name, logo or branding mismatch on the consent screen

**Symptom.** The logo does not appear on the consent screen (users see a generic placeholder), or
branding verification is raised separately from scope verification.

**Cause.** Branding verification is a **separate process** from verification of your scopes. If your
branding is not verified, the consent screen may show a generic logo even though the app works. It
has its own requirements, including verifying ownership of the domain used for the homepage and
logo.

**Fix.** Treat branding as its own workstream: verify the domain, supply the logo at the required
size and format, and confirm the app name and homepage match what you submitted for scope
verification.

**Prevention.** Do the domain verification early. It is a prerequisite for other steps and it is
boring in exactly the way that causes projects to stall.

**Evidence to send.** Screenshots of the branding configuration, confirmation of domain
verification, and the assets you supplied.

---

## 10. Silence, stalling and expiry

**Symptom.** A follow-up request arrives and the process goes quiet; or you cannot remember what you
submitted; or the app is still in a pending state weeks later.

**Cause.** Almost never a Google-side mystery. The usual causes: the reply was never sent; the reply
was sent but did not answer the specific points; the app was changed during review so the submitted
material stopped matching the live app; a required page went down or was redeployed mid-review; the
person who owned the thread left; the video link expired; a deadline passed without a response.

**Fix.**
1. Reply, even if the answer is incomplete. State what you have, what you are still working on, and
   when you will send the rest. Silence is read as abandonment.
2. Answer the reviewer's points in their order, with evidence.
3. Re-verify that everything you cited is still live and still matches: homepage, policy, video
   link, scope list, app name.
4. Freeze deployments to the pages and flows under review where you can. A homepage redesign or a
   domain move during review costs you a round.
5. If a deadline was missed, say so plainly, explain the cause in one line, and ask what happens
   next. Do not pretend it did not happen.

**Prevention.** Record the submission date, project ID, client ID, final scope list and video link
in your own notes. Nominate an owner for the verification thread, and put follow-up reminders in
that owner's calendar. Assume at least one round of questions and plan for it.

**Evidence to send.** A short status note with the current state of every item the reviewer raised,
and the dates on which each is next expected to move.

---

## Cross-cutting patterns

If you only remember four things from this file, remember these:

1. **Most declines are evidence problems, not policy problems.** The reviewer could not confirm
   something from the material you sent. Sending better material is the fix; arguing is not.
2. **Consistency is checked before depth.** Four artefacts carry your identity and your scope list.
   They must agree exactly. Depth in the justification does not compensate for a name mismatch.
3. **The cheapest fix is usually to remove something** — a scope, a claim, a feature that is not
   ready. Reductions are cheap and they are read favourably.
4. **Do the review-friendly things early:** publish the homepage and policy, settle the name, film a
   rehearsal, and write the scope reasoning while you still remember it. Verification is mostly a
   paperwork project, and paperwork done late is paperwork done badly.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. No rejection
or approval statistics are claimed or implied anywhere in this file. Google's requirements change;
confirm against current official documentation before acting.*
