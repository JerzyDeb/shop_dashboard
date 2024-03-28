"""Countries apps."""

# Django
from django.apps import AppConfig


class CountriesConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.countries'
