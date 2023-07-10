"""Shop apps."""

# Django
from django.apps import AppConfig


class ShopConfig(AppConfig):  # noqa: D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shop'
