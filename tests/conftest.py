import pytest

from app.config import settings


@pytest.fixture(autouse=True)
def test_settings():
    settings.EMAIL_FROM = "test_email_from"
    settings.EMAIL_TO = "test_email_to"
    settings.EMAIL_TO_ALL = "test_email_to_all"
    settings.EMAIL_SUBJECT = "test_email_subject"
    settings.EMAIL_DOMAIN = "test_email_domain"

    settings.TG_HASTAG = "рассылка"
    settings.TG_HASTAG_ALL = "рассылка_всем"

    settings.MAILGUN_API_KEY = "test_mailgun_api_key"
