#!/usr/bin/env python3
"""Preflight check for an OAuth consent screen configuration.

Catches the mechanical reasons a verification submission is rejected or sent back,
before you submit - and refuses to guess which scopes are sensitive.

Usage:
  google-oauth-verification-preflight consent.json
  google-oauth-verification-preflight consent.json --json

From a checkout the same CLI runs as:
  python3 check_consent.py consent.json

Standard library only: no third-party runtime dependencies.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from urllib.parse import urlparse

# Scopes whose classification is genuinely stable enough to state.
CLASS_CONFIDENT = {"openid", "email", "profile",
                   "https://www.googleapis.com/auth/userinfo.email",
                   "https://www.googleapis.com/auth/userinfo.profile"}
# Everything else must be looked up. Marking a scope "sensitive" when it is
# restricted (or the reverse) can cost weeks, so the tool says UNVERIFIED rather
# than guessing.
LOOKUP_REQUIRED = re.compile(
    r"(gmail|drive|calendar|spreadsheets|script|cloud-platform|analytics|"
    r"youtube|contacts|tasks|admin|directory|photos)", re.I)

REQUIRED = [
    ("app_name", "the application name shown on the consent screen"),
    ("support_email", "a monitored support email"),
    ("homepage_url", "the application homepage"),
    ("privacy_policy_url", "a link to your privacy policy"),
    ("authorized_domains", "at least one authorized domain"),
    ("scopes", "the scopes you are requesting"),
    ("redirect_uris", "at least one redirect URI"),
]


def check(cfg: dict) -> tuple:
    """Return (errors, warnings, notes)."""
    errors, warnings, notes = [], [], []

    for field, why in REQUIRED:
        if cfg.get(field) in (None, "", [], {}):
            errors.append(f"missing {field}: needs {why}")

    # homepage must be https and a real host
    for field in ("homepage_url", "privacy_policy_url"):
        url = cfg.get(field)
        if url:
            u = urlparse(str(url))
            if u.scheme != "https":
                errors.append(f"{field} is not https ({url}) - Google requires an "
                              f"SSL-protected page")
            if not u.netloc:
                errors.append(f"{field} is not an absolute URL ({url})")
            if u.netloc.split(":")[0] in ("localhost", "127.0.0.1"):
                errors.append(f"{field} points at localhost - the reviewer cannot "
                              f"reach it, and this is an immediate rejection")

    # app name must match the homepage title/brand, and be stable
    name = cfg.get("app_name")
    if name and len(str(name)) > 40:
        warnings.append(f"app_name is {len(str(name))} characters; a name that "
                        f"does not fit the consent screen is a common mismatch")

    # authorized domains must not be placeholders
    doms = cfg.get("authorized_domains") or []
    for d in doms:
        if any(x in str(d).lower() for x in ("example.com", "yourdomain", "localhost")):
            errors.append(f"authorized_domains contains a placeholder ({d}) - "
                          f"replace it with your real domain")

    # redirect URIs must share a host with an authorized domain
    hosts = {str(d).lstrip(".").lower() for d in doms}
    for uri in cfg.get("redirect_uris") or []:
        h = urlparse(str(uri)).netloc.split(":")[0].lower()
        if hosts and h and not any(h == x or h.endswith("." + x) for x in hosts):
            errors.append(f"redirect_uri host {h!r} is not covered by any "
                          f"authorized_domains entry {sorted(hosts)} - verification "
                          f"requires the redirect host to be an authorized domain")

    # scopes: classify honestly, never guess
    scopes = cfg.get("scopes") or []
    unverified = []
    for s in scopes:
        base = str(s).rstrip("/").split("/")[-1]
        if s in CLASS_CONFIDENT or base in ("openid", "email", "profile"):
            notes.append(f"{s}: non-sensitive, no verification trigger")
        elif LOOKUP_REQUIRED.search(str(s)):
            unverified.append(s)
        else:
            unverified.append(s)
    if unverified:
        warnings.append(
            f"{len(unverified)} scope(s) need their classification confirmed against "
            f"Google's current list BEFORE submitting: {', '.join(unverified)}. "
            f"This tool does not guess classifications - marking a restricted scope "
            f"as sensitive (or the reverse) can cost weeks.")

    # each scope should have a justification written down
    just = cfg.get("scope_justifications") or {}
    for s in scopes:
        if s not in just and str(s) not in just:
            warnings.append(f"no scope_justification written for {s} - this is the "
                            f"field most submissions are declined on")

    # a demo video is required for sensitive/restricted scopes
    if unverified and not cfg.get("demo_video_url"):
        warnings.append("sensitive or restricted scopes usually require a demo "
                        "video; demo_video_url is empty")

    if not cfg.get("terms_url"):
        notes.append("no terms_url given - strongly recommended; confirm the "
                     "current requirement yourself")

    return errors, warnings, notes


def _read_config(path: str):
    """Read the config text. Return (raw_text, None) or (None, error_message).

    Failures are reported as a plain message rather than a traceback: a missing
    file, a directory, an unreadable file and a non-UTF-8 file are all ordinary
    user mistakes, not crashes.
    """
    if path == "-":
        try:
            return sys.stdin.read(), None
        except (OSError, UnicodeDecodeError) as exc:
            return None, f"cannot read stdin: {exc}"
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read(), None
    except IsADirectoryError:
        return None, (f"{path} is a directory, not a JSON file - "
                      f"pass the path to a consent config file")
    except FileNotFoundError:
        return None, f"no such file: {path}"
    except UnicodeDecodeError as exc:
        return None, f"{path} is not valid UTF-8 text: {exc}"
    except OSError as exc:
        return None, f"cannot read {path}: {exc}"


def main(argv=None) -> int:
    # prog is deliberately not pinned: argparse then reports whatever name the
    # user actually invoked, so `python3 check_consent.py --help` from a checkout
    # and the installed console script both show their own name.
    ap = argparse.ArgumentParser(
        description="Preflight an OAuth consent screen config.")
    ap.add_argument("config", help="JSON file, or - for stdin")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    raw, read_error = _read_config(a.config)
    if read_error is not None:
        print(f"error: {read_error}", file=sys.stderr)
        return 2

    try:
        cfg = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"error: not valid JSON: {e}", file=sys.stderr)
        return 2

    if not isinstance(cfg, dict):
        print(f"error: config must be a JSON object mapping field names to values, "
              f"got {type(cfg).__name__}", file=sys.stderr)
        return 2

    errors, warnings, notes = check(cfg)
    if a.json:
        print(json.dumps({"errors": errors, "warnings": warnings, "notes": notes}, indent=2))
    else:
        for e in errors:
            print(f"  ERROR   {e}")
        for w in warnings:
            print(f"  WARN    {w}")
        for n in notes:
            print(f"  note    {n}")
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s), {len(notes)} note(s)")
        print("\nThis is not an official Google document and is not affiliated with "
              "Google.\nRequirements change - verify against Google's current "
              "published documentation.")
    return 2 if errors else (1 if warnings else 0)


if __name__ == "__main__":
    sys.exit(main())
