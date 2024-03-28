"""Products models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from .managers import ProductVariantCustomManager
from .utils import set_slug


class Category(models.Model):  # noqa: D101
    name = models.CharField(
        _('Nazwa kategorii'),
        max_length=255,
    )
    slug = models.CharField(
        _('Slug'),
        max_length=255,
        editable=False,
    )

    def __str__(self):  # noqa: D105
        return self.name

    def save(self, *args, **kwargs):
        """Set slug for object."""

        set_slug(self)
        super().save(*args, **kwargs)

    class Meta:  # noqa: D106
        verbose_name = _('Kategoria')
        verbose_name_plural = _('Kategorie')


class Product(models.Model):  # noqa: D101
    name = models.CharField(
        _('Nazwa produktu'),
        max_length=255,
    )
    slug = models.CharField(
        _('Slug'),
        max_length=255,
        unique=True,
        editable=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_('Kategoria'),
    )

    def __str__(self):  # noqa: D105
        return self.name

    def save(self, *args, **kwargs):
        """Set slug for object."""

        set_slug(self)
        super().save(*args, **kwargs)

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
