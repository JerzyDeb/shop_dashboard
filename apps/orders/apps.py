"""Orders apps."""

# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OrdersConfig(AppConfig):  # noqa: D101
    verbose_name = _('Zamówienia')
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
