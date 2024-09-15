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


class ProductTag(models.Model):
    """Model for representing tags in products."""

    class Tags(models.TextChoices):
        """Available tags for products."""

        NEW_ARRIVAL = 'new_arrival', _('Nowość')
        BEST_SELLER = 'best_seller', _('Najlepiej sprzedający się')
        DISCOUNTED = 'discounted', _('Przeceniony')
        LIMITED_EDITION = 'limited_edition', _('Edycja limitowana')
        ECO_FRIENDLY = 'eco_friendly', _('Ekologiczny')
        PREMIUM_QUALITY = 'premium_quality', _('Wysoka jakość')
        ON_SALE = 'on_sale', _('Na wyprzedaży')
        EXCLUSIVE = 'exclusive', _('Ekskluzywny')
        TRENDING = 'trending', _('Trendy')
        TOP_RATED = 'top_rated', _('Najwyżej oceniany')
        SEASONAL = 'seasonal', _('Sezonowy')
        GIFT_IDEA = 'gift_idea', _('Pomysł na prezent')
        HANDMADE = 'handmade', _('Ręcznie robiony')
        LOW_STOCK = 'low_stock', _('Niski stan magazynowy')
        BEST_VALUE = 'best_value', _('Najlepsza wartość')

    tag = models.CharField(
        _('Tag'),
        max_length=15,
        choices=Tags.choices,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_('Produkt'),
    )

    @classmethod
    def generate_new_products_tags(cls):
        """Delete all tags and create new."""

        cls.objects.all().delete()
        tags_to_create = [cls(
            product=product,
            tag=random.choice(cls.Tags.choices)[0],
        ) for product in Product.objects.all() for x in range(random.randint(1, 3))]
        cls.objects.bulk_create(tags_to_create)

    def __str__(self):  # noqa: 105
        return f'{self.product} [{self.get_tag_display()}]'

    class Meta:  # noqa: D106
        verbose_name = _('Tag produktu')
        verbose_name_plural = _('Tagi produktów')
