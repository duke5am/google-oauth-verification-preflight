"""Tests for the google-oauth-verification-preflight CLI.

These tests exercise the packaged tool: every case runs the documented
`python3 check_consent.py ...` entry point as a real subprocess and asserts on
its exit code and captured output, so a traceback or a wrong exit code fails the
suite instead of being hidden.

They import the package from this checkout (the repo root is put on sys.path), so
`python3 -m unittest discover -s tests -v` works from the repo root with no
installation step.

Scratch input files live under /root/ and are removed in tearDown.

Note on the README: the README's sample block abbreviates scope identifiers
("gmail.readonly", "drive") while the tool prints the full scope URL it was given.
These tests assert the documented *problems* and the documented summary counts,
and use substring checks that the full URLs satisfy, rather than pinning the
abridged illustration character for character.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WRAPPER = os.path.join(REPO_ROOT, "check_consent.py")
EXAMPLES = os.path.join(REPO_ROOT, "examples")
GOOD = os.path.join(EXAMPLES, "consent-good.json")
BAD = os.path.join(EXAMPLES, "consent-bad.json")

if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

import google_oauth_verification_preflight  # noqa: E402
from google_oauth_verification_preflight import cli  # noqa: E402


def run_cli(*args):
    """Run the documented CLI entry point; return the CompletedProcess."""
    return subprocess.run(
        [sys.executable, WRAPPER, *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )


class BaseCliTest(unittest.TestCase):
    def setUp(self):
        # Scratch files under /root, never /tmp and never inside the repo.
        self.tmp = tempfile.mkdtemp(prefix="goauth-cli-test-", dir="/root")
        self.missing = os.path.join(self.tmp, "does-not-exist.json")
        self.malformed = os.path.join(self.tmp, "malformed.json")
        self.empty_dir = os.path.join(self.tmp, "empty-dir")
        os.mkdir(self.empty_dir)
        with open(self.malformed, "w", encoding="utf-8") as fh:
            fh.write("{'not': 'json',}\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)
        self.assertFalse(os.path.exists(self.tmp),
                         f"scratch directory {self.tmp} was not cleaned up")

    def assert_clean_failure(self, proc, what):
        """Non-zero exit, a clear message, and no Python traceback."""
        combined = proc.stdout + proc.stderr
        self.assertNotEqual(proc.returncode, 0, f"{what}: expected non-zero exit")
        self.assertNotIn("Traceback (most recent call last)", combined,
                         f"{what}: leaked a Python traceback:\n{combined}")
        self.assertTrue(proc.stderr.strip(),
                        f"{what}: expected a message on stderr, got nothing")
        self.assertIn("error:", proc.stderr,
                      f"{what}: stderr message is not a clear 'error: ...' line:\n"
                      f"{proc.stderr}")
        return combined


class TestPackagingShape(BaseCliTest):
    """The packaging itself: one implementation, wrapped not duplicated."""

    def test_package_is_importable(self):
        self.assertTrue(callable(google_oauth_verification_preflight.check))
        self.assertEqual(google_oauth_verification_preflight.__version__, "0.1.0")

    def test_console_script_target_exists(self):
        # [project.scripts] points at google_oauth_verification_preflight.cli:main
        self.assertTrue(callable(cli.main))

    def test_wrapper_is_thin(self):
        with open(WRAPPER, "r", encoding="utf-8") as fh:
            source = fh.read()
        self.assertIn("from google_oauth_verification_preflight.cli import main", source)
        self.assertIn("sys.exit(main())", source)
        # The wrapper must not contain a second copy of the checking logic.
        self.assertNotIn("def check(", source)
        self.assertNotIn("LOOKUP_REQUIRED", source)

    def test_check_returns_three_lists(self):
        with open(GOOD, "r", encoding="utf-8") as fh:
            cfg = json.load(fh)
        errors, warnings, notes = cli.check(cfg)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        # openid/email/profile are the only scopes the tool classifies, and it
        # reports them as notes; notes never affect the exit code.
        self.assertEqual(len(notes), 3)
        for scope in ("openid", "email", "profile"):
            with self.subTest(scope=scope):
                self.assertIn(f"{scope}: non-sensitive, no verification trigger", notes)


class TestDocumentedExamples(BaseCliTest):
    """examples/*.json must behave the way README.md documents."""

    def test_good_example_is_clean_and_exits_zero(self):
        proc = run_cli(GOOD)
        self.assertEqual(proc.returncode, 0,
                         f"good example should be clean (0), got {proc.returncode}:\n"
                         f"{proc.stdout}{proc.stderr}")
        self.assertIn("0 error(s), 0 warning(s)", proc.stdout)

    def test_good_example_notes_openid_email_profile_are_non_sensitive(self):
        proc = run_cli(GOOD)
        self.assertEqual(proc.returncode, 0)
        self.assertIn("non-sensitive, no verification trigger", proc.stdout)
        # The tool only states a classification for these three.
        self.assertEqual(proc.stdout.count("non-sensitive, no verification trigger"), 3)

    def test_bad_example_reports_every_problem_the_readme_lists(self):
        proc = run_cli(BAD)
        out = proc.stdout
        self.assertEqual(proc.returncode, 2,
                         f"bad example has errors, so exit 2 is documented; got "
                         f"{proc.returncode}:\n{out}{proc.stderr}")
        documented = [
            # README "What it catches": localhost / non-https homepage
            "homepage_url points at localhost - the reviewer cannot reach it",
            # README "What it catches": placeholder authorized domains
            "authorized_domains contains a placeholder (example.com)",
            # README "What it catches": redirect host not covered by a domain
            "redirect_uri host 'otherapp.com' is not covered by any authorized_domains",
            # README "What it catches": app name too long for the consent screen
            "does not fit the consent screen is a common mismatch",
            # README WARN block: scopes needing classification confirmed
            "2 scope(s) need their classification confirmed against Google's current",
            # README "What it refuses to do": never guess a classification
            "This tool does not guess classifications",
            # README WARN block: the field most submissions are declined on
            "no scope_justification written for",
            "this is the field most submissions are declined on",
            # README "What it catches": sensitive scopes but no demo video
            "demo video; demo_video_url is empty",
        ]
        for phrase in documented:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, out, f"missing from output:\n{out}")
        # The two unverified scopes the README names must both be called out.
        for scope in ("gmail.readonly", "drive"):
            with self.subTest(scope=scope):
                self.assertIn(scope, out)
        # Scope URLs that are non-sensitive are still stated as such.
        self.assertIn("openid: non-sensitive, no verification trigger", out)
        # 5 errors: homepage non-https, homepage localhost, privacy non-https,
        # placeholder domain, redirect host not covered.
        self.assertIn("5 error(s)", out)
        self.assertNotIn("Traceback (most recent call last)", out + proc.stderr)

    def test_bad_example_json_flag_exits_non_zero_with_structured_output(self):
        proc = run_cli(BAD, "--json")
        self.assertEqual(proc.returncode, 2)
        payload = json.loads(proc.stdout)
        self.assertEqual(set(payload), {"errors", "warnings", "notes"})
        self.assertTrue(any("localhost" in e for e in payload["errors"]))
        self.assertTrue(any("placeholder" in e for e in payload["errors"]))
        self.assertTrue(any("otherapp.com" in e for e in payload["errors"]))

    def test_warnings_only_config_exits_one(self):
        """README: exit codes 0 clean, 1 warnings only, 2 errors."""
        cfg = {
            "app_name": "Acme Invoicing",
            "support_email": "support@acme.example",
            "homepage_url": "https://acme.example",
            "privacy_policy_url": "https://acme.example/privacy",
            "terms_url": "https://acme.example/terms",
            "authorized_domains": ["acme.example"],
            "scopes": ["openid"],
            "redirect_uris": ["https://acme.example/oauth/callback"],
            # scope_justifications deliberately absent -> warning, not error
        }
        path = os.path.join(self.tmp, "warnings-only.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(cfg, fh)
        proc = run_cli(path)
        self.assertEqual(proc.returncode, 1,
                         f"warnings only must exit 1, got {proc.returncode}:\n{proc.stdout}")
        self.assertIn("no scope_justification written for openid", proc.stdout)
        self.assertIn("0 error(s)", proc.stdout)


class TestBadInputIsHandledCleanly(BaseCliTest):
    """Bad input must exit non-zero with a clear message and no traceback."""

    def test_missing_file(self):
        proc = run_cli(self.missing)
        combined = self.assert_clean_failure(proc, "missing file")
        self.assertIn("no such file", proc.stderr)
        self.assertIn(self.missing, proc.stderr)
        self.assertEqual(proc.returncode, 2)

    def test_malformed_json(self):
        proc = run_cli(self.malformed)
        combined = self.assert_clean_failure(proc, "malformed JSON")
        self.assertIn("not valid JSON", proc.stderr)
        self.assertEqual(proc.returncode, 2)

    def test_empty_directory(self):
        proc = run_cli(self.empty_dir)
        combined = self.assert_clean_failure(proc, "empty directory")
        self.assertIn("is a directory", proc.stderr)
        self.assertEqual(proc.returncode, 2)

    def test_truncated_json(self):
        path = os.path.join(self.tmp, "truncated.json")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write('{"app_name": "Acme"')
        proc = run_cli(path)
        self.assert_clean_failure(proc, "truncated JSON")
        self.assertIn("not valid JSON", proc.stderr)

    def test_empty_file(self):
        path = os.path.join(self.tmp, "empty.json")
        open(path, "w", encoding="utf-8").close()
        proc = run_cli(path)
        self.assert_clean_failure(proc, "empty file")

    def test_json_array_instead_of_object(self):
        path = os.path.join(self.tmp, "array.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(["openid", "email"], fh)
        proc = run_cli(path)
        combined = self.assert_clean_failure(proc, "JSON array")
        self.assertIn("must be a JSON object", proc.stderr)

    def test_json_scalar_instead_of_object(self):
        path = os.path.join(self.tmp, "scalar.json")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("42\n")
        proc = run_cli(path)
        self.assert_clean_failure(proc, "JSON scalar")

    def test_non_utf8_file(self):
        path = os.path.join(self.tmp, "binary.json")
        with open(path, "wb") as fh:
            fh.write(b"\xff\xfe\x00\x01not text")
        proc = run_cli(path)
        combined = self.assert_clean_failure(proc, "non-UTF-8 file")

    def test_no_arguments_is_a_usage_error_not_a_traceback(self):
        proc = run_cli()
        combined = proc.stdout + proc.stderr
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback (most recent call last)", combined)

    def test_stdin_dash_still_works(self):
        """`-` for stdin is documented in the CLI help and must keep working."""
        with open(GOOD, "r", encoding="utf-8") as fh:
            raw = fh.read()
        proc = subprocess.run(
            [sys.executable, WRAPPER, "-"],
            cwd=REPO_ROOT, input=raw, capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
        self.assertIn("0 error(s), 0 warning(s)", proc.stdout)


if __name__ == "__main__":
    unittest.main()
