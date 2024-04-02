"""Orders models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Project
from apps.accounts.models import CustomUser
from apps.countries.models import Country
from apps.products.models import ProductVariant

# Local
from .managers import OrderItemCustomManager


class Order(models.Model):  # noqa: D101
    number = models.CharField(
        _('Numer zamówienia'),
        max_length=255,
        unique=True,
    )
    purchased_date = models.DateTimeField(
        _('Data zamówienia'),
        auto_now_add=True,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_('Użytkownik'),
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_('Państwo'),
    )

    @property
    def total_value(self):
        """Return the sum of the products of quantity and price for each item in this order."""

        all_items = self.orderitem_set.all()
        total_value = sum([
            item.unit_price * item.quantity
            for item in all_items])
        return total_value or 0

    def __str__(self):  # noqa: D105
        return f'{_("Zamówienie nr.")} {self.number}'

    class Meta:  # noqa: D106
        verbose_name = _('Zamówienie')
        verbose_name_plural = _('Zamówienia')
        ordering = [
            'purchased_date',
        ]


class OrderItem(models.Model):  # noqa: D101
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name=_('Zamówienie'),
    )
    product_variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.PROTECT,
        verbose_name=_('Wariant produktu'),
    )
    quantity = models.PositiveIntegerField(
        _('Ilość'),
    )
    unit_price = models.FloatField(
        _('Cena'),
    )
    objects = OrderItemCustomManager()

    def save(self, *args, **kwargs):
        """Copy unit price from product variant to order item."""

        self.unit_price = self.product_variant.unit_price
        super().save(*args, **kwargs)

    def __str__(self):  # noqa: D105
        return f'{_("Element")}{self.id} {_("zamówienia nr.")} {self.order.number}'

    class Meta:  # noqa: D106
        verbose_name = _('Element zamówienia')
        verbose_name_plural = _('Elementy zamówień')
