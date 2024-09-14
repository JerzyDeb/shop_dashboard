"""Orders models."""
# Standard Library
import random

# Django
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# 3rd-Party
from faker import Faker

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
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_('Użytkownik'),
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        verbose_name=_('Państwo'),
        null=True,
    )

    @classmethod
    def generate_new_orders(cls, orders_number=100):
        """Delete all orders and create new based on created users and countries."""

        cls.objects.all().delete()
        fake = Faker()
        users = CustomUser.objects.all()
        countries = Country.objects.all()
        orders_to_create = [cls(
            number=fake.unique.uuid4(),
            user=random.choice(users),
            country=random.choice(countries),
            purchased_date=fake.date_time_this_year(
                before_now=True,
                after_now=False,
                tzinfo=timezone.get_current_timezone(),
            ),
        ) for x in range(orders_number)]
        cls.objects.bulk_create(orders_to_create)

    @property
    def total_value(self):
        """Return the sum of the products of quantity and price for each item in this order."""

        all_items = self.orderitem_set.all()
        total_value = sum([
            item.unit_price * item.quantity
            for item in all_items])
        return round(total_value, 2) or 0

    def save(self, *args, **kwargs):
        """Set purchased date if not given."""

        if not self.purchased_date:
            self.purchased_date = timezone.now()
        super().save(*args, **kwargs)

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
        on_delete=models.SET_NULL,
        verbose_name=_('Wariant produktu'),
        null=True,
    )
    quantity = models.PositiveIntegerField(
        _('Ilość'),
    )
    unit_price = models.FloatField(
        _('Cena'),
    )
    objects = OrderItemCustomManager()

    @classmethod
    def generate_new_orders_items(cls):
        """Delete all order items and create new based on created orders and variants."""

        cls.objects.all().delete()
        orders = Order.objects.all()
        product_variants = list(ProductVariant.objects.all())
        order_items_to_create = [
            cls(
                order=order,
                product_variant=variant,
                quantity=random.randint(1, 10),
                unit_price=variant.unit_price
            )
            for order in orders
            for x in range(random.randint(2, 6))
            for variant in [random.choice(product_variants)]
        ]
        cls.objects.bulk_create(order_items_to_create)

    def save(self, *args, **kwargs):
        """Copy unit price from product variant to order item."""

        self.unit_price = self.product_variant.unit_price
        super().save(*args, **kwargs)

    def __str__(self):  # noqa: D105
        return f'{_("Element")}{self.id} {_("zamówienia nr.")} {self.order.number}'

    class Meta:  # noqa: D106
        verbose_name = _('Element zamówienia')
        verbose_name_plural = _('Elementy zamówień')
