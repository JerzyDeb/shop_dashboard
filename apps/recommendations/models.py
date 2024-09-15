"""Recommendations models."""

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
from apps.products.models import Product

# Local
from .managers import UserProductInteractionCustomManager


class UserProductInteraction(models.Model):
    """Model for representing an interaction between a user and a product."""

    class InteractionType(models.TextChoices):
        """Available interaction types."""

        VIEW = 'view', _('Oglądanie')
        ADD_TO_CART = 'add_to_cart', _('Dodanie do koszyka')
        PURCHASE = 'purchase', _('Zakup')
        RATE = 'rate', _('Wystawienie oceny')

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_('Użytkownik'),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Produkt'),
    )
    interaction_type = models.CharField(
        _('Typ interakcji'),
        max_length=15,
        choices=InteractionType.choices,
    )
    timestamp = models.DateTimeField(
        _('Data interakcji'),
    )
    objects = UserProductInteractionCustomManager()

    @classmethod
    def generate_new_interactions(cls):
        """Delete all interactions and create new."""

        cls.objects.all().delete()
        products = Product.objects.all()
        fake = Faker()
        interactions_to_create = [cls(
            user=user,
            product=random.choice(products),
            interaction_type=random.choice(cls.InteractionType.choices)[0],
            timestamp=fake.date_time_this_year(
                before_now=True,
                after_now=False,
                tzinfo=timezone.get_current_timezone(),
            ),
        ) for user in CustomUser.objects.all() for x in range(20)]
        cls.objects.bulk_create(interactions_to_create)

    def save(self, *args, **kwargs):
        """Set timestamp if not given."""

        if not self.timestamp:
            self.timestamp = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):  # noqa: D105
        return '{0} [{1}]'.format(_('Interakcja użytkownika'), self.user.username)

    class Meta:  # noqa: D106
        verbose_name = _('Interkacja użytkownika')
        verbose_name_plural = _('Interkacje użytkowników')
