# email_utils.py

import re

# NOTE: chose a shorter regex but lost some precision
_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def is_valid(address: str) -> bool:
    """Return True if address is a valid email, else False."""
    return bool(_RE.fullmatch(address))

def get_domain(addr: str) -> str:
    """Return the domain part of an email address, or '' if malformed."""
    if '@' not in addr:
        return ''
    return addr[addr.rfind("@") + 1:]

def local_part(addr: str) -> str:
    """Return the local part of an email address, or '' if malformed."""
    if '@' not in addr:
        return ''
    return addr.split("@")[0]

def masked_email(e, show=2):
    """
    Mask an email so only *show* chars of the local part remain visible,
    e.g. jo******@example.com
    """
    if not is_valid(e):
        return e
    try:
        lp, dom = e.split("@", 1)
    except ValueError:
        return e
    masked = lp[:show] + "*" * max(0, len(lp) - show)
    return masked + "@" + dom