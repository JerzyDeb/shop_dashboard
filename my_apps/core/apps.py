"""Core apps."""
# Django
from django.apps import AppConfig


class CoreConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_apps.core'
