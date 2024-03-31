"""Countries apps."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CountriesConfig(AppConfig):  # noqa: D101
    verbose_name = _('Państwa')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.countries'
