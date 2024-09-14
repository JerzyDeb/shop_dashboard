"""Core models."""
# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Settings(models.Model):  # noqa: D101
    shop_name = models.CharField(
        _('Nazwa sklepu'),
        max_length=255,
        null=True,
        blank=True,
    )
    show_current_month_orders_chart = models.BooleanField(
        _('Pokaż wykres zamówień z aktualnego miesiąca'),
        default=True,
    )
    show_last_12_months_orders_chart = models.BooleanField(
        _('Pokaż wykres zamówień z ostatnich 12 miesięcy'),
        default=True,
    )
    show_countries_orders_chart = models.BooleanField(
        _('Pokaż wykres zamówień z konkretnych krajów'),
        default=True,
    )
    show_categories_products_chart = models.BooleanField(
        _('Pokaż wykres produktów z konkretnych kategorii'),
        default=True,
    )
    show_best_sells_products_chart = models.BooleanField(
        _('Pokaż wykres najlepiej sprzedających się produktów'),
        default=True,
    )
    enable_test_mode = models.BooleanField(
        _('Włącz tryb testowy'),
        help_text=_('Tryb testowy pozwala na wymianę WSZYSTKICH danych w bazie danych (w celach pokazowych'),  # noqa: E501
        default=False,
    )

    def __str__(self):  # noqa: D105
        return f'{_("Ustawienia")}'

    class Meta:  # noqa: D106
        verbose_name = _('Ustawienia')
        verbose_name_plural = verbose_name
