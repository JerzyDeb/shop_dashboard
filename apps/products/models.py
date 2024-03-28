"""Products models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.products.managers import ProductVariantCustomManager


class Product(models.Model):  # noqa: D101
    name = models.CharField(
        _('Nazwa produktu'),
        max_length=255,
    )
    slug = models.CharField(
        _('Slug'),
        max_length=255,
        unique=True,
    )

    def __str__(self):  # noqa: D105
        return self.name

    class Meta:  # noqa: D106
        verbose_name = _('Produkt')
        verbose_name_plural = _('Produkty')


class ProductVariant(models.Model):  # noqa: D101
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Produkt'),
    )
    name = models.CharField(
        _('Nazwa wariantu'),
        max_length=255,
    )
    stock_code = models.CharField(
        _('Kod magazynowy'),
        max_length=255,
        unique=True,
    )
    unit_price = models.FloatField(
        _('Cena'),
    )
    objects = ProductVariantCustomManager()

    def __str__(self):  # noqa: D105
        return self.name

    class Meta:  # noqa: D106
        verbose_name = _('Wariant produktu')
        verbose_name_plural = _('Warianty produktów')
