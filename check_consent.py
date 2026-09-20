#!/usr/bin/env python3
"""check_consent: preflight an OAuth consent screen configuration.

This wrapper exists so the documented `python3 check_consent.py consent.json`
workflow keeps working from a clone. The same CLI is installed as the
`google-oauth-verification-preflight` console script; the implementation lives in
`google_oauth_verification_preflight/cli.py` so that the installed package and the
checkout are the same code, not two versions of it.

Usage:
  python3 check_consent.py consent.json
  python3 check_consent.py consent.json --json
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google_oauth_verification_preflight.cli import main  # noqa: E402

if __name__ == "__main__":
    sys.exit(main())
