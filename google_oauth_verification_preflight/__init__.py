"""Preflight an OAuth consent screen configuration before verification.

Catches the mechanical reasons a Google OAuth verification submission is
rejected or sent back, and refuses to guess which scopes are sensitive.

Standard library only - there are no runtime dependencies.

`check` is re-exported lazily so that importing the package stays cheap and does
not import the CLI module: `python -m google_oauth_verification_preflight.cli`
would otherwise warn that the module was already in sys.modules.
"""

__version__ = "0.1.0"

__all__ = ["check", "__version__"]


def __getattr__(name):
    if name == "check":
        from google_oauth_verification_preflight.cli import check
        return check
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
