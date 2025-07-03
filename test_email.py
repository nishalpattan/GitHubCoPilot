import pytest
from email_utils import is_valid_email

def test_valid_emails():
    assert is_valid_email("user@example.com")
    assert is_valid_email("user.name+tag@domain.co")
    assert is_valid_email("user@mail.example.com")  # sub-domain edge case

def test_invalid_emails():
    assert not is_valid_email("userexample.com")  # missing @
    assert not is_valid_email("user@.com")        # missing domain name
    assert not is_valid_email("@example.com")     # missing local part
