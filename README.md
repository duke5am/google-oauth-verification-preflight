# google-oauth-verification-preflight

[![PyPI](https://img.shields.io/pypi/v/google-oauth-verification-preflight)](https://pypi.org/project/google-oauth-verification-preflight/)

Check your OAuth consent screen configuration **before** submitting for
verification, so you are not declined on something mechanical.

Standard library only — no runtime dependencies at all.

```bash
pip install google-oauth-verification-preflight      # from PyPI, Python 3.9+
google-oauth-verification-preflight consent.json

# or straight from a clone, no install:
git clone https://github.com/duke5am/google-oauth-verification-preflight
cd google-oauth-verification-preflight
python3 check_consent.py consent.json
```

The clone and the installed package run the same code: `check_consent.py` is a
thin wrapper around `google_oauth_verification_preflight/cli.py`.

```
  ERROR   homepage_url points at localhost - the reviewer cannot reach it, and
          this is an immediate rejection
  ERROR   authorized_domains contains a placeholder (example.com)
  ERROR   redirect_uri host 'otherapp.com' is not covered by any authorized_domains
          entry ['example.com']
  WARN    2 scope(s) need their classification confirmed against Google's current
          list BEFORE submitting: gmail.readonly, drive. This tool does not guess
          classifications - marking a restricted scope as sensitive (or the reverse)
          can cost weeks.
  WARN    no scope_justification written for gmail.readonly - this is the field most
          submissions are declined on
```

## What it catches

- **localhost or non-https homepage / privacy policy** — the reviewer cannot reach
  it, and it is an immediate rejection
- **placeholder authorized domains** (`example.com`, `yourdomain`)
- **a redirect URI whose host is not covered by an authorized domain**
- an app name too long for the consent screen
- **scopes with no written justification** — the field most submissions are
  declined on
- sensitive/restricted scopes present but no demo video

## What it refuses to do

**It does not guess scope classifications.** Scope sensitivity changes and getting
it wrong cuts both ways, so the tool marks anything non-obvious as needing lookup
against Google's current published list rather than asserting a classification.
Only `openid`, `email` and `profile` are stated as non-sensitive.

Exit codes: `0` clean · `1` warnings only · `2` errors.

## Templates

`templates/` has fillable versions of what the submission actually asks for:

- `app-description.md`
- `scope-justification.md` — **one block per scope**, which is where submissions fail
- `demo-video-script.md` — shot by shot, including what gets a video rejected
- `homepage-requirements.md` — what the reviewer checks on your homepage
- `privacy-policy-template.md` — the disclosures Google requires for OAuth apps
- `rebuttal-responses.md` — replies to "we need more information"

`COMMON-REJECTIONS.md` lists symptom → cause → fix.
`PRE-SUBMISSION-CHECKLIST.md` is ordered cheapest-fix-first.

## Read this first

**Not affiliated with Google** and not an official Google document.

**Requirements change.** Verify against Google's current published documentation,
especially scope classifications — the highest-risk item here.

**Not legal advice.** The privacy policy needs review for your jurisdiction and
your actual data practices; it is a drafting aid, not a substitute for that review.

**Google's Limited Use requirements** govern how you may use data obtained through
Google APIs.

**A restricted-scope security assessment has a cost and is not instant** — do not
budget from any number here; get current published terms.

**No timeline is given, deliberately.** Nobody outside Google can promise a review
duration.

**No approval rate or rejection rate is claimed**, because no reliable public
figure exists. The rejection patterns here are recurring observations, not
statistics.

## The full pack

Adds the scope decision guide (how to avoid verification entirely — often cheaper
than the security assessment), the process walkthrough, and the complete rejection
catalogue.

<!-- RELATED:START -->

## Related tools

- **[spf-dkim-dmarc-audit](https://github.com/duke5am/spf-dkim-dmarc-audit)** — Audit SPF, DKIM and DMARC against live DNS, with recursive SPF lookup counting and the exact record to publish. Tested against 124 real domains.
  *(if you were searching for "spf dkim dmarc check")*

All 28 tools in this set, grouped by what they check: **[dev-tools-index](https://duke5am.github.io/dev-tools-index/)**

If you arrived here searching for one of these, this is the tool: **google oauth verification rejected** · **sensitive scopes verification** · **oauth consent screen requirements** · **casa security assessment**

<!-- RELATED:END -->

→ More developer tooling like this: **[duke5am.gumroad.com](https://duke5am.gumroad.com)** <!-- GUMROAD-LINK -->
