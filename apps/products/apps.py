"""Products apps."""

# Django
from django.apps import AppConfig


class ProductsConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
