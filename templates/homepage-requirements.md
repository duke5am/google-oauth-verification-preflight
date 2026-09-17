# Homepage Requirements — Checklist and Fixes

**Template:** `homepage-requirements.md`
**Who needs this:** everyone. Even a perfect scope justification fails if the reviewer opens your
homepage and cannot see what Google needs to see there. Homepage problems are also the cheapest
category of problem to fix, which is why they come first in
`docs/PRE-SUBMISSION-CHECKLIST.md`.

> Google's published requirements, and the exact checks its reviewers apply, change over time.
> This file describes the shape of what Google has consistently asked for and links the concepts
> to the language Google uses. Confirm the current requirement text in Google's own OAuth
> verification documentation before you submit. This is not an official Google document and is not
> affiliated with or endorsed by Google.

---

## Part 1 — Why the homepage matters so much

Verification is not only about code. The reviewer has to be able to answer three questions using
public pages:

1. **Does this app really exist as a public product?** A homepage that requires a login, or is a
   `localhost` page, or is a placeholder, cannot establish this.
2. **Is the app name on the consent screen the same product?** Name matching is checked, and it is
   checked mechanically before a human looks at anything.
3. **Is there a public privacy policy that discloses what happens to Google user data?** This is a
   stated requirement for apps that access Google user data, not a nice-to-have.

**Why a login-walled homepage fails.** If `https://example.com` immediately redirects a
logged-out visitor to a sign-in form, the reviewer sees a login box and nothing else. They cannot
confirm the app name, cannot read what the product does, cannot click the privacy policy link
without creating an account, and cannot reconcile your consent screen with a public product. The
most common version of this failure is a single-page app whose root route is the authenticated
dashboard. Google's reviewers will not create accounts to review your app; a page behind a login
is, for review purposes, a page that does not exist.

**Why a "coming soon" or password-protected staging homepage fails.** Same reason: there is
nothing public to review. If your product is not yet public, the usual answer is to publish a real
description page for it, not to submit and hope.

**Why the homepage must be on the same domain pattern you declared.** Reviewers compare the
homepage URL, the privacy policy URL, and the JavaScript origins in the OAuth client
configuration. A homepage on `example.com`, a privacy policy on `notion.site`, and a JS origin on
`app.example.com` invites the follow-up question "which of these is the application?" Keep them
coherent and same-site where you can. If you must use a third-party host for the policy, say so
and make the link prominent and stable.

---

## Part 2 — The checklist

Work top to bottom. Each item states what Google is looking for and the fix if you fail it.

### Identity

1. **The app name appears as text on the homepage.** Not only in an image, not only in the
   `<title>`, not only in a logo that a screen reader cannot read. A visible heading is the
   clearest evidence. **Fix:** add an `<h1>` or header with the exact app name.
2. **The app name on the homepage is the same string as the app name on the consent screen and in
   the Cloud project.** Character for character, including capitalisation and any punctuation.
   **Fix:** pick one spelling and use it in all three places. If your legal entity name differs
   ("Acme Analytics Ltd" vs "Acme Analytics"), use the product name on the consent screen and the
   homepage, and mention the legal entity in the footer or terms — do not use the legal entity on
   the consent screen.
3. **The homepage describes what the product does, in words a reviewer can understand.** One or two
   clear sentences. Not a slogan. Concrete: who it is for and what job it does. **Fix:** rewrite
   the hero copy. If your hero copy is a metaphor, add a plain sentence underneath it.
4. **The homepage is reachable at the exact URL you entered in the form, over HTTPS, without a
   redirect to a different domain.** **Fix:** test in a fresh browser profile with no session. If
   it 302s to a marketing subdomain, either submit that subdomain or change the redirect.
5. **The homepage loads for a logged-out visitor.** No redirect to `/login`, no modal that cannot
   be dismissed, no cookie wall that blocks the page. **Fix:** render a public landing page at the
   root route and move the app behind `/app` or `/dashboard`.

### The privacy policy link

6. **A link to the privacy policy appears on the homepage.** Google's requirements for apps that
   access Google user data include publishing a privacy policy, and the homepage is where
   reviewers look for it. **Fix:** add a visible link. Footer is normal and accepted; header or
   main navigation is even more obvious.
7. **The link text is recognisable.** "Privacy Policy" is ideal. "Legal", "Fine print", or an icon
   in a crowded footer is a needless risk. **Fix:** change the text to "Privacy Policy".
8. **The link resolves to a real page, over HTTPS, without a login, and without a PDF download.**
   A PDF can be missed, fails to render on some reviewers' setups, and looks like an afterthought.
   **Fix:** publish the policy as HTML on your own domain. A stable public document host is
   acceptable if your own site cannot host it, but the same-domain HTML page is the safer choice.
9. **The privacy policy URL you put in the Cloud Console is the same URL as the link on the
   homepage.** Reviewers follow both. **Fix:** make them identical, and do not use a URL with
   tracking parameters or a session id.
10. **The privacy policy itself contains the required Google-related disclosures, not just generic
    GDPR boilerplate.** At minimum: what Google user data you access, how you use it, how it is
    stored and shared, how long you keep it, how a user deletes it, and the Limited Use
    commitments. `privacy-policy-template.md` in this pack is built for exactly this.
11. **The privacy policy is not an empty page or a template placeholder.** Search your live page
    for `[`, `Lorem`, `TODO`, and `Company Name`. **Fix:** obviously, fill it in.

### Terms of service

12. **Publish terms of service, and link them from the homepage.** Google's OAuth verification
    material has asked for a terms of service link in some versions of the requirements and not in
    others, so **treat this as strongly recommended rather than as a fixed universal rule, and
    check the current published requirements yourself.** It costs almost nothing, reviewers
    generally react well to it, and your privacy policy and terms should be consistent with each
    other. **Fix:** publish a short, honest ToS on the same domain and link it next to the privacy
    policy in the footer.
13. **Do not let your terms contradict your privacy policy or your scope justification.** For
    example, a ToS that reserves the right to share data with "partners" while the privacy policy
    promises no sharing is a credibility problem that will produce a follow-up question. **Fix:**
    read both documents side by side before submitting.

### Content that helps, and content that hurts

14. **Include a short "how it works" or features section that mentions the Google integration.**
    It should correspond to the feature you cite in your scope justification, using plain terms.
    This gives a reviewer an independent way to see that the scope maps to a real feature.
15. **Include a support contact.** A visible support email or contact page. The consent screen has
    a support email field; reviewers may check that it is plausible and monitored.
16. **Do not claim things your app does not do.** "We never store your data" on the homepage while
    your submission describes a 90-day retention window is the kind of contradiction that turns a
    routine review into a long one. **Fix:** make the homepage, the privacy policy, the app
    description, and the video agree.
17. **Do not gate the homepage behind a waitlist signup form.** It reads as "no product to
    review".
18. **Do not have broken links, placeholder copy, or lorem ipsum anywhere a reviewer might click.**
    **Fix:** run a link checker over the homepage and the two policy pages.

### Technical

19. **HTTPS everywhere, with a valid certificate.** No mixed content warnings, no expired cert, no
    self-signed cert. **Fix:** renew and test in a fresh profile.
20. **The page renders without JavaScript errors that blank the content.** If your landing page is
    client-rendered and the bundle fails, the reviewer sees an empty page. **Fix:** check the
    browser console in a clean profile, and consider server-rendering at least the identity block.
21. **The homepage is not geo-blocked or region-restricted.** A block for the reviewer's region
    looks identical to a missing homepage. **Fix:** test from a couple of locations, or remove the
    restriction for public marketing pages.
22. **The homepage is not a `localhost`, `*.ngrok.io`, `*.vercel.app` preview URL, or an IP
    address**, unless you genuinely have nothing else and are prepared to explain it. **Fix:**
    point a real domain at it. This is also required for some other Google configuration steps,
    such as domain verification for branding.
23. **The favicon, `<title>`, and Open Graph title all use the app name.** Small, but every
    consistent signal helps identity matching.

---

## Part 3 — Worked example of a compliant homepage structure

Not a design, a structure. A plain page with these blocks passes; a beautiful page missing block 3
does not.

```
[HEADER]
  [APP NAME]                      <- exact consent-screen string, visible as text
  Features | Pricing | Docs | Privacy Policy | Terms     <- Privacy Policy is link text, not "Legal"

[HERO]
  "[ONE PLAIN SENTENCE: what it does, for whom]"
  "[ONE PLAIN SENTENCE: the Google integration, stated plainly — e.g. 'Sign in with Google and
   connect a Drive folder; Ledgerly reads the invoices in it so you do not upload them by hand.']"
  [Sign in with Google button]    <- real button, real flow

[FEATURES]
  - [FEATURE THAT USES SCOPE 1] — [plain description]
  - [FEATURE THAT USES SCOPE 2] — [plain description]

[DATA AND PRIVACY]
  "We access [WHAT], only to [WHY]. We do not sell or share Google user data and we do not use it
   for advertising. See our Privacy Policy for what we store, for how long, and how to delete it."
  Privacy Policy | Terms of Service

[FOOTER]
  [APP NAME] | [COMPANY LEGAL ENTITY, if different] | [SUPPORT EMAIL] | Privacy Policy | Terms
```

The loop to close: **a reviewer should be able to read only your homepage and your privacy policy
and already know what your app does, which Google data it touches, and why.** If they cannot, the
video and the scope justification are working uphill.

---

## Part 4 — Final homepage self-check

Test in a fresh browser profile with no cookies and no account, on a laptop.

- [ ] `[HOMEPAGE URL]` loads with no login and does not redirect off-domain.
- [ ] The exact app name string is visible as text.
- [ ] The app name matches the consent screen and the Cloud project character for character.
- [ ] A link whose text is "Privacy Policy" is visible on the homepage.
- [ ] The privacy policy link goes to the same URL you entered in the Cloud Console.
- [ ] The privacy policy page loads logged out, renders as HTML, and is not a placeholder.
- [ ] The privacy policy contains the Google user data disclosures and the Limited Use language.
- [ ] A terms of service link is present (recommended; confirm the current requirement).
- [ ] The homepage, privacy policy, terms, app description and video do not contradict each other.
- [ ] HTTPS with a valid certificate; no console errors; no lorem ipsum; no broken links.
- [ ] A one-sentence plain description of the app is on the page.
- [ ] Support contact is visible.
- [ ] You have screenshotted the homepage and the privacy policy and attached them where the form
      allows, because a screenshot survives a transient outage at review time.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Homepage
and policy requirements are set by Google and change; verify against current official documentation
before submitting.*
