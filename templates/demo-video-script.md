# Demo Video Script — Shot-by-Shot

**Template:** `demo-video-script.md`
**What this is:** a shot list you can film in one sitting, plus the rules that decide whether the
video is accepted or sent back.
**Hard requirement:** for sensitive and restricted scopes, a demonstration video is part of
verification. A submission without one is not a complete submission. Most video-related
rejections are not about production quality — they are about the video not *showing* something the
reviewer must see.

> Google's exact video instructions and the form fields that reference them change. Confirm the
> current wording of the video requirement in Google's verification documentation when you film.
> This is not an official Google document and is not affiliated with or endorsed by Google.

---

## Part 1 — The rules that decide acceptance

### Must be visible in the video

| Must show | Why | How to guarantee it |
|---|---|---|
| **The app's homepage, loaded from its real public URL** | Proves the homepage exists and is public. Reviewers use it to check app identity and the privacy policy link | Start the video there. Do not start inside a logged-in dashboard |
| **The OAuth consent screen appearing during a real sign-in** | This is the core artefact being reviewed | Perform a real sign-in. Do not show a mock consent screen |
| **The browser address bar while the consent screen is on screen** | Lets the reviewer confirm the request is going to Google and see the request parameters, including the client ID | Zoom the browser, or use a window size where the URL is legible. Scroll the address bar into frame if you have to |
| **The client ID in the consent URL matching the client ID in the Cloud project** | Ties the video to the project under review. This is the single most-skipped item | Have the Cloud Console credentials page open in another tab and cut to it. Read the ID aloud |
| **Granting each requested scope** | A scope that is never granted is a scope the reviewer cannot see working | If you request several scopes, the consent flow must show all of them being granted |
| **The app actually using the data obtained** | This is what distinguishes a working app from a scope request. Most "scope not used" rejections are really "video did not show it used" | Navigate to the feature and show the real data on screen |
| **Real, non-trivial data** | Empty states prove nothing | Sign in as a test user whose account genuinely contains the data. Populate it beforehand |
| **The privacy policy page, reachable from the homepage** | Reviewer cross-checks the link and the content | Click through to it in the video, or show it earlier in the same unbroken session |

### What gets a video rejected

| Rejection | The reviewer's view of it |
|---|---|
| **Edited, cut, sped up, or jump-cut footage of the consent flow** | Cannot tell whether anything was skipped |
| **A consent screen you mocked in Figma/HTML, or a screen recording of a different app** | Not evidence of anything |
| **Address bar hidden, blurred, cropped, or too small to read** | Client ID and request parameters cannot be verified |
| **Never showing the client ID anywhere in the Cloud Console** | Cannot connect the video to the project being reviewed |
| **Signing in with a demo/sandbox mode that bypasses the real OAuth flow** | The flow under review is precisely what was skipped |
| **Showing only the final screen with the data already loaded** | Does not show the data came from the granted scope |
| **Using an account that has no data, so every screen is empty** | Nothing to see, so nothing is verified |
| **Music over narration with no explanation of what is happening** | Reviewer cannot tell which feature is being demonstrated |
| **A 20-minute video with the relevant 40 seconds buried at minute 14** | Treated as non-responsive |
| **Voice-over or on-screen text in a language the review team does not work in** | Provide English narration or English captions/subtitles |
| **Video on a platform that requires a login to view** | Not viewable, so not evidence. Use an unlisted public link |
| **Video link that 404s, is private, or expired by the time it is reviewed** | Verification cannot proceed. Check the link before and after you submit |
| **App name in the video differing from the consent screen and the Cloud project** | Identity mismatch |
| **Recording the OAuth Playground or a generic API tool instead of your app** | Demonstrates Google's tooling, not your app |
| **Leaving real user personal data, real customer emails, or credential material on screen** | Do not trade a verification problem for a privacy incident |

### Practical filming setup

- **Resolution:** 1080p is plenty. Legibility of the address bar matters more than framerate.
- **Browser:** normal (non-incognito) window so the address bar is at full width; hide bookmarks
  or use a profile with none, so the URL is the only thing in that strip.
- **Zoom:** browser zoom at 125–150% and OS display scaling up. If the address bar is unreadable in
  the final export, the shot has failed regardless of anything else in it.
- **Window size:** record a single window, not the whole desktop, so nothing sensitive and nothing
  distracting is in frame.
- **Length:** aim for 4–7 minutes total. Enough to show every scope used; short enough to watch
  without skipping.
- **Narration:** continuous spoken English, or a clean on-screen caption track in English. Say the
  app name, the scope, and what is now happening on screen.
- **One take per segment, and never cut inside the consent flow.** Cut between chapters if you
  must (homepage → sign-in → feature), but the segment from "click sign in" to "back in the app
  with the scope granted" must be continuous and unedited.
- **Upload:** YouTube unlisted or public, English title and description, no expiry. Paste the URL
  into the submission form and keep a copy of it in your own notes in case the form or thread is
  lost.
- **Before you film:** prepare the data. Seed the test account with several realistic items so no
  screen is empty.

---

## Part 2 — The shot list

Fill in the placeholders before filming. Timestamps below are targets for a ~6 minute video.

### Chapter 0 — Setup before recording (not filmed)

```
App name:             [APP NAME]
Homepage URL:         [https://example.com]
Privacy policy URL:   [https://example.com/privacy]
Sign-in entry route:  [https://example.com/login]
Feature route(s):     [https://example.com/invoices]
Cloud project:        [PROJECT ID]
Client ID:            [CLIENT ID]   <-- copy/paste everywhere, never retype
Scopes requested:     [SCOPE 1] [SCOPE 2] [SCOPE 3]
Test account:         [TEST USER EMAIL]
Data seeded:          [e.g. 12 invoice PDFs in the folder / 8 labelled emails]
```

Checklist before you press record:

- [ ] Test account has real data in it, enough that every screen shows something.
- [ ] Test account has **not** already granted these scopes to this client (or revoke them at
      [myaccount.google.com](https://myaccount.google.com) → Data & privacy → Third-party apps).
      You cannot show a consent screen to an account that already consented.
- [ ] Cloud Console open in a second tab, on the **Credentials** page, scrolled to the OAuth 2.0
      client ID. Also useful: the **OAuth consent screen** page showing the same app name and the
      same scope list.
- [ ] Browser zoom set so the address bar is legible; bookmarks bar hidden.
- [ ] Notifications silenced; no personal tabs, no customer data, no API keys or tokens in frame.
- [ ] Privacy policy page loads while logged out, and is one click from the homepage.

---

### Chapter 1 — The homepage (target 0:00 – 0:40)

**Do:**
1. Start the recording with the browser on the homepage URL. Let the full page render.
2. Scroll slowly, top to bottom, pausing on:
   - the **app name in the site header** — narrate it: *"This is [APP NAME]. The same name appears on our OAuth consent screen."*
   - the **privacy policy link** in the footer, and the terms of service link if you have one;
   - one or two sentences describing what the product does.
3. Click the privacy policy link, let the policy page render, scroll to the section that names
   Google user data and the Limited Use commitment. Narrate: *"Our privacy policy explains what
   Google user data we access and how it is used, stored, retained and deleted."*
4. Navigate back to the homepage.

**Must be visible:** the address bar showing `[HOMEPAGE URL]` the whole time, and the privacy
policy URL when you are on it.

**Narration for this chapter:** *"This is [APP NAME], the app in this verification request. Here is
our homepage, and here is the privacy policy linked from our footer. The app name on this page is
the same name shown on our OAuth consent screen."*

---

### Chapter 2 — The consent flow, unedited (target 0:40 – 2:00)

**Do:**
1. From the homepage, click **Sign in with Google**. Keep it continuous from here.
2. When the Google account picker appears, pause for two seconds and narrate which account you are
   choosing: *"I am signing in with our test account, [TEST USER EMAIL]."*
3. **Before clicking through the consent screen, hold still.** The reviewer needs to read:
   - the address bar (leave enough dwell time that a paused frame is readable);
   - the **app name** shown on the consent screen;
   - the **scopes** listed on the consent screen.
   Narrate each scope as it is presented: *"The app is requesting [SCOPE 1], which lets it
   [PLAIN ENGLISH PURPOSE]."*
4. Grant every requested scope. If the flow shows one screen per permission, let each one sit on
   screen for a moment.
5. Complete the flow and land back in the app.

**Optional but strongly recommended — Chapter 2b, the client ID match (insert anywhere in
chapter 2, but do not cut the consent flow to do it):**

- Before you start the consent flow, open the Cloud Console **Credentials** page in the tab next to
  it, show the client ID and the project name on screen, and read the client ID aloud.
- Then switch to the app tab and perform the sign-in.
- At the end, switch back and show the same client ID again.
- If your consent screen URL is visible and includes the client ID, say so explicitly: *"You can
  see the same client ID in the request URL and in our Cloud project."*

**Do not:** cut, speed up, blur, or skip any part of this chapter. This is the chapter that is
actually being verified.

---

### Chapter 3 — Proof that the app uses the data (target 2:00 – 5:00)

One sub-section per scope. Show the feature, not the settings page.

**For each scope:**

```
SCOPE BEING DEMONSTRATED: [SCOPE]
FEATURE THAT CONSUMES IT: [FEATURE NAME]
ROUTE:                    [https://example.com/path]
WHAT THE VIEWER MUST SEE: [e.g. the invoice list populated with the PDFs that came from Drive]
```

**Pattern to follow for each scope:**

1. Navigate to the feature. Keep the address bar visible.
2. Show the data on screen, and **connect it out loud to the scope**: *"These are the twelve
   invoice PDFs read from the Drive folder I connected. This list is populated by [SCOPE], which
   is why the scope is required."*
3. **Trigger a live action** that calls the API again rather than showing a cached page — e.g.
   refresh the list, add a new item in the Google side (send an email to the test address, drop a
   new file into the Drive folder), then reload and show it appear in the app. This is the
   strongest single piece of evidence in the whole video.
4. If the app writes anything back to Google, show the result appearing in the Google product. If
   it writes nothing, say so: *"The app never writes to Drive; we requested read-only access."*
5. Show where the user can disconnect: *"The user can revoke access here"* — and, if relevant,
   *"and here is where they delete their data."*

**Narration template per scope:** *"This is [FEATURE]. It reads [WHAT] using [SCOPE]. I have just
added [NEW ITEM] in [GOOGLE PRODUCT]; on refresh it appears here, which shows the app is calling
the API with the granted scope. We do not [WHAT YOU DO NOT DO — write, delete, share]. The user can
disconnect or delete this data from [SCREEN]."*

---

### Chapter 4 — Close (target 5:00 – 5:30)

1. Return to the homepage.
2. Narrate a two-sentence summary: the app name, the scopes requested, and what each one is for.
3. State the client ID one last time while it is visible.
4. Stop recording.

---

## Part 3 — Narration script you can read aloud

Replace the brackets and read it in your own words. Speaking naturally is fine; being inaudible or
silent is not.

```
[0:00] This video demonstrates [APP NAME], the application submitted for OAuth verification
       under Google Cloud project [PROJECT ID].

[0:05] This is our homepage at [HOMEPAGE URL]. The application name is [APP NAME], which is the
       same name shown on our OAuth consent screen. The privacy policy is linked in the footer.

[0:20] Our privacy policy describes the Google user data we access, how we use it, how it is
       stored, how long we keep it, and how a user deletes it. [Scroll to the Google data section.]

[0:35] Here is the OAuth client ID in our Google Cloud project: [CLIENT ID]. You will see this
       same client ID in the authorization request.

[0:50] I am now signing in with our test account, [TEST USER EMAIL].

[0:58] This is the Google consent screen. The app requesting access is [APP NAME]. The address
       bar shows the authorization request. The app is requesting:
       [SCOPE 1] — to [PURPOSE IN PLAIN ENGLISH];
       [SCOPE 2] — to [PURPOSE IN PLAIN ENGLISH].

[1:30] I am granting all requested permissions now. [Grant each.]

[1:45] Back in the app. I am now at [FEATURE ROUTE].

[2:00] This is [FEATURE]. The items on this screen were read from [GOOGLE PRODUCT] using
       [SCOPE]. To show that this is live, I am adding a new item in [GOOGLE PRODUCT] now.
       [Do it.] Refreshing the app — the new item appears. That is [SCOPE] being used.

[3:00] [Repeat for each remaining scope.]

[5:00] In summary: [APP NAME], client ID [CLIENT ID], requesting [SCOPE LIST], each used for the
       features demonstrated above. We do not sell or share Google user data, and we do not use it
       for advertising. Users can disconnect the integration and delete their data from
       [SCREEN].
```

---

## Part 4 — Final video self-check

Watch your own export end-to-end, at normal speed, on a laptop screen — not on the phone you
recorded it on.

- [ ] The address bar is readable without pausing and zooming.
- [ ] The homepage and privacy policy URL are both visible in the video.
- [ ] The consent screen is real and shown unedited in one continuous take.
- [ ] Every scope you request in the Cloud project appears on the consent screen in the video.
- [ ] Every scope is shown being *used* in the app, with real data.
- [ ] The client ID is visible at least once, and it matches the Cloud Console.
- [ ] The app name is identical in the video, on the consent screen, on the homepage, and in the
      Cloud project.
- [ ] No empty states and no lorem ipsum.
- [ ] Narration is audible, or English captions are present.
- [ ] No personal data, no customer data, no API keys or tokens visible.
- [ ] Nothing in the flow has been cut, sped up, or blurred.
- [ ] The video is uploaded to a link that works while logged out, and the link is in the form.
- [ ] You have the link saved somewhere outside the Google verification thread.
- [ ] You have re-watched it after any scope change, and re-recorded if the scope list changed.

---

*Part of the Google OAuth Verification Submission Kit. Not an official Google document. Video
requirements are set by Google and change; confirm against current official documentation before
you submit.*
