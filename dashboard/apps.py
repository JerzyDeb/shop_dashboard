"""Dashboard apps."""
# Django
from django.apps import AppConfig


class DashboardConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'
