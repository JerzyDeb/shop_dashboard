"""Products apps."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductsConfig(AppConfig):  # noqa: D101
    verbose_name = _('Produkty')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
