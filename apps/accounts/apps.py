"""Accounts apps."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AccountsConfig(AppConfig):  # noqa: D101
    verbose_name = _('Konta użytkowników')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
