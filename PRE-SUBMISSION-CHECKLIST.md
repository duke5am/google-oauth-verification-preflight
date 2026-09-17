# Pre-Submission Checklist

**How this is ordered:** cheapest-to-fix first, highest-cost-to-fix last. Work top to bottom. Do not
skip ahead to item 40; most failed submissions fail in the first fifteen items, and those fifteen
take an afternoon.

Each item states **what to do** and **why it matters** — because a checklist you understand is a
checklist you actually finish.

> Google's requirements change. This checklist reflects the shape of what Google has consistently
> asked for, not a transcription of the current policy. **Before you submit, open Google's current
> OAuth verification documentation and the Cloud Console side by side with this file and confirm
> each item is still the right thing to check.** This is not an official Google document and is not
> affiliated with or endorsed by Google.

**Suggested use:** copy this file, tick items as you go, and paste the completion date and the
evidence URL next to each tick. The evidence column is what saves you when a reviewer asks in three
weeks' time whether something was true at submission.

---

## Tier 1 — The cheap mechanical checks (do these first; they take under an hour)

**1. Pick one app name string and use it everywhere.**
Write it down once: `______________________`. Then search every artefact for variants.
*Why it matters:* app name matching is checked early and mechanically, before a human reads your
justification. A mismatch costs you a full review round in exchange for a typo.

**2. Make the consent screen's "Application name" exactly that string.**
*Why it matters:* the consent screen is the artefact the user sees and the reviewer compares against
everything else. It is the reference value.

**3. Make the homepage show that same string as visible text (not only in an image or a logo).**
*Why it matters:* reviewers compare the consent screen to the public page. A logo image is weaker
evidence than a heading and may not be readable.

**4. Put a link on the homepage whose visible text is exactly "Privacy Policy".**
Not "Legal", not "Privacy", not an icon in a crowded footer.
*Why it matters:* a requirement of OAuth verification for apps accessing Google user data is a
published privacy policy; the reviewer has to *find* it, and recognisable link text is how they do
it.

**5. Make the privacy policy URL on the homepage identical to the one on the consent screen.**
Character for character, including whether you use `www`, and with no tracking parameters.
*Why it matters:* two different URLs look like two different documents, and the reviewer will check
both.

**6. Check the homepage and privacy policy load for a logged-out visitor in a fresh browser
profile.**
*Why it matters:* a login-walled homepage is the most common single cause of a "cannot verify"
response. Google's reviewers do not create accounts.

**7. Check both pages load over HTTPS with a valid certificate and no mixed-content warnings.**
*Why it matters:* a certificate problem at review time looks exactly like a missing page.

**8. Search your live privacy policy for template leftovers.**
Look for `[`, `]`, `TODO`, `Lorem`, `example.com`, `Company Name`, `[YOUR`.
*Why it matters:* the fastest way to look careless is to publish a placeholder. It also reads as
"this policy was not written for this app".

**9. Search your live homepage for the same leftovers and for broken links.**
*Why it matters:* reviewers click things. Dead links on a homepage undermine every other claim.

**10. Verify the demo video link opens while logged out.**
Test it in a private window. Then test it again from a different device.
*Why it matters:* a private, expired or deleted video is not evidence, and it will be discovered at
exactly the wrong moment.

**11. Confirm the video has no cuts inside the consent flow.**
Watch the segment from "click sign in" to "back in the app" at normal speed.
*Why it matters:* an edited consent flow is indistinguishable from a fabricated one.

**12. Confirm the browser address bar is legible in the video.**
Watch it on a laptop screen, not on the phone you recorded it on.
*Why it matters:* the address bar is where the reviewer confirms the request and the client ID. If
it cannot be read, the reviewer cannot verify the flow.

---

## Tier 2 — The scope list (an hour or two; the highest-value work in this file)

**13. Write down your scope list exactly as configured in the Cloud project.**
Every scope, full string, one per line. This becomes the reference list for everything else.
*Why it matters:* four artefacts have to agree — consent screen, justification, privacy policy,
video. Without one authoritative list you will drift.

**14. For each scope, name the user-visible feature that requires it.**
*Why it matters:* if you cannot name a feature, the reviewer cannot either, and "the scope does not
appear to be used" is the single most expensive follow-up question because it usually requires a
re-recorded video and a code change.

**15. For each scope, name the Google API method your code calls with it.**
Grep your codebase. If the only hits are the scope constant and a config file, the scope is unused.
*Why it matters:* unused scopes are rejection risk with no benefit. Removing them is free.

**16. Drop every scope with no feature and every scope with no API call.**
Do this before you do anything else on this list.
*Why it matters:* the cheapest scope to justify is the one you do not request; it also shortens the
video, the policy and every future review.

**17. Look up the tier of every remaining scope in Google's current published documentation, today.**
Record for each: scope string, tier, date checked, URL checked.
*Why it matters:* tiers change, and treating a restricted scope as sensitive can cost you an
unplanned security assessment. **Never rely on a classification from memory, from a blog post, or
from this pack.**

**18. For every sensitive or restricted scope, write a specific reason why a narrower scope or a
user-mediated alternative does not work.**
Name the alternative you considered and reject it with a concrete reason.
*Why it matters:* this sentence is what the reviewer is actually looking for. "Core functionality"
and "better user experience" are treated as non-answers.

**19. For every restricted scope, decide whether you would rather redesign.**
Get current published terms for the security assessment — fee and cadence — and cost the redesign
against it in a spreadsheet.
*Why it matters:* the assessment has a fee, a third-party dependency and a recurring obligation. Many
teams would choose a different design if they saw the comparison before submission rather than
after.

**20. Confirm the scope list matches exactly in all four places:** Cloud project configuration,
scope justification, privacy policy section on Google data, and video consent screen.
*Why it matters:* a scope in one place and not another is a contradiction, and contradictions read
as carelessness at best.

**21. If you request any scope that you do not use at sign-in, consider requesting it incrementally
instead, only when the user asks for the feature.**
*Why it matters:* it reduces per-user consent friction, strengthens the necessity story, and makes
the video clearer — but note it does not reduce your obligation to justify every scope you can
request.

---

## Tier 3 — The homepage and policy content (half a day)

**22. Publish a privacy policy containing, under a findable heading: what Google user data you
access, how you use it, how it is stored and shared, how long you keep it, how a user deletes it,
and the Limited Use commitments.**
Use `privacy-policy-template.md`.
*Why it matters:* these are exactly the disclosures reviewers look for. A generic website policy
that never mentions Google user data will produce a follow-up question.

**23. Confirm the Limited Use paragraph in the policy is true of your code.**
No advertising use, no selling, no transfer except as allowed, no human review except as allowed.
*Why it matters:* making a commitment you do not keep is worse than making none, and it is checked
against your app description and your actual behaviour.

**24. State concrete retention periods per data category, and make sure a mechanism enforces each
one.**
*Why it matters:* an unenforced retention promise is a false statement, and it is the kind of
finding that escalates a routine review.

**25. Provide a real, tested deletion route — in-product and by email — and describe both in the
policy.**
Test it yourself, end to end, and note the date.
*Why it matters:* deletion is a required disclosure and a common follow-up question. A route that
does not work when the reviewer looks is worse than no claim at all.

**26. Describe how a user revokes your access from their Google Account, in plain steps.**
*Why it matters:* it is a standard expectation and reviewers look for it. Google controls those
screens, so point to them rather than describing a flow you do not own.

**27. Publish terms of service and link them from the homepage next to the privacy policy.**
*Why it matters:* Google's OAuth requirements have asked for a terms of service link in some
versions and not others — **confirm the current requirement yourself.** It costs very little and
reviewers generally respond well to it. Do not treat it as a substitute for the privacy policy.

**28. Make the homepage explain, in plain language, what the app does and how it uses Google data.**
One or two sentences, and a features section that names the integration.
*Why it matters:* it gives the reviewer an independent way to see the scope maps to a real feature.
It is also the difference between "unclear purpose" and a clean review.

**29. Add a visible support contact on the homepage.**
*Why it matters:* the consent screen carries a support email; reviewers may check that it is
plausible and that the product has a real operator.

**30. Make sure the homepage, privacy policy, terms, app description and video do not contradict
each other on any factual point.**
Read them side by side. Pay particular attention to storage, sharing, retention, deletion and
sub-processors.
*Why it matters:* contradictions look like concealment rather than carelessness, and they attract
the most scrutiny.

**31. Have a lawyer in your jurisdiction review the published privacy policy.**
*Why it matters:* the template in this pack is not legal advice and does not attempt to satisfy
every statutory regime. Privacy law and Google's requirements are two different obligations, and you
have both.

**32. Attach screenshots of the homepage and privacy policy to your submission where the form
allows.**
*Why it matters:* a screenshot survives a transient outage, a geo-block or a deploy during the
review window.

---

## Tier 4 — The submission content (a day)

**33. Complete the app description with one paragraph on what the app does, one on who it is for,
and one block per scope covering what you read, what you do with it, and why a narrower scope cannot
do it.**
Use `app-description.md`.
*Why it matters:* this is the first thing a reviewer reads, and a vague description makes every
scope look unjustified.

**34. Complete one justification block per scope, weighted to the tier.**
Sensitive scopes need a feature-level story; restricted scopes need that plus the assessment
addendum.
Use `scope-justification.md`.
*Why it matters:* scope justification is where most submissions fail, and it is the one thing you
cannot bluff.

**35. For every claim in the submission, be able to point at a URL, a timestamp, a screenshot or a
code path.**
*Why it matters:* evidence is what converts a claim into a confirmed fact for the reviewer.

**36. Remove every instance of these phrases:** "core functionality", "better user experience",
"required for the app to work", "future features", "might", "we plan to".
*Why it matters:* they signal that the scope was not thought about, and reviewers recognise them
instantly.

**37. State your storage, transmission, sub-processors, retention and deletion in the submission,
matching the privacy policy.**
*Why it matters:* the same facts are asked twice, in the form and in the policy, and they must
agree.

---

## Tier 5 — The video (an afternoon, plus re-recording if you get it wrong)

**38. Film the video from the rehearsed shot list.**
Use `demo-video-script.md`. One continuous take through consent; cuts allowed only between chapters.
*Why it matters:* the video is a hard requirement for sensitive and restricted scopes, and most
video rejections are about missing evidence rather than production quality.

**39. Confirm the video shows:** the homepage loaded publicly; the privacy policy reached from it;
the real consent screen with the address bar visible; every requested scope being granted; the app
using the resulting data with real, non-empty content; the client ID visible and matching the Cloud
project.
*Why it matters:* each of these is a specific thing the reviewer must be able to see. Missing any
one of them can mean a re-record.

**40. Trigger a live API call on camera** — add an item in the Google product, refresh the app, show
it appear.
*Why it matters:* it is the strongest available evidence that the scope is genuinely used, and it
directly pre-empts the most expensive follow-up question.

**41. Remove every empty state, every piece of dummy data and any real personal data from the
recording.**
*Why it matters:* empty screens verify nothing, and real customer content on screen turns a
verification problem into a privacy incident.

**42. Add English narration or English captions, and confirm they are audible/legible.**
*Why it matters:* the reviewer must be able to tell what feature is being demonstrated and which
scope it uses.

**43. Upload to a link that works logged out, name it clearly in English, and keep the link
somewhere outside the verification thread.**
*Why it matters:* verification threads get lost, forms get resubmitted, and you will want that link
again.

---

## Tier 6 — The configuration and the submission itself

**44. Confirm the authorised domains, JavaScript origins and redirect URIs in the OAuth client match
where your app actually runs.**
*Why it matters:* a redirect mismatch is a functional failure that looks like a verification
problem, and it can make the video unrecordable.

**45. Confirm you know whether your app is Internal or External, and its publishing status — and
that this is what you intend.**
*Why it matters:* Internal apps largely skip verification, and Testing apps are capped in users. If
you meant to be Internal and you are not, you have taken on work you did not need.

**46. Confirm you are in Testing status with your own accounts added as test users while you
prepare, rather than publishing early.**
*Why it matters:* publishing before the submission is ready puts a warning screen in front of real
users for no benefit. Note also that refresh tokens behave differently in Testing — check the
current behaviour before you debug a token problem as a code bug.

**47. Confirm the branding requirements separately from the scope requirements — name, logo,
homepage, domain verification.**
*Why it matters:* branding verification is a different process from scope verification, and passing
one does not give you the other. An unverified logo shows as a generic placeholder to users.

**48. Record, in your own notes: the submission date, the client ID, the project ID, the final scope
list, and the video link.**
*Why it matters:* when a follow-up arrives six weeks later, you need to know exactly what you
submitted, not what you believe you submitted.

**49. Decide in advance who will answer follow-up questions, and how fast.**
*Why it matters:* responses to "we need more information" requests are usually the largest
controllable factor in how long the process takes. Silence is read as abandonment.

**50. Keep `rebuttal-responses.md` open and assume at least one round of follow-up questions.**
*Why it matters:* expecting a round and having a response ready turns a weeks-long setback into a
day's work. Being surprised by it does the opposite.

---

## The final gate

Before you click submit, answer these three questions out loud:

1. **Can a reviewer who has never seen my product understand what it does, which Google data it
   touches, and why, using only my homepage, my privacy policy and my video?** If not, fix that
   first; nothing else compensates.
2. **Is every scope in my request tied to a feature that is visible on camera?** If not, drop the
   scope or film the feature.
3. **Have I confirmed Google's current requirements myself, today, rather than trusting this
   checklist?** This pack is a high-quality starting point. It is not Google, and it will age.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Requirements
change; confirm against Google's current published documentation before submitting.*
