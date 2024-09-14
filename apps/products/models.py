"""Products models."""
# Standard Library
import random

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# 3rd-Party
from faker import Faker
from slugify import slugify

# Local
from .consts import CATEGORY_PRODUCTS_VARIANTS
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

    @classmethod
    def generate_new_categories(cls):
        """Delete all categories items and create new based on CATEGORY_PRODUCTS_VARIANTS."""

        cls.objects.all().delete()
        categories_to_create = [cls(
            name=category_name,
            slug=slugify(category_name),
        ) for category_name in CATEGORY_PRODUCTS_VARIANTS.keys()]
        cls.objects.bulk_create(categories_to_create)

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

    @classmethod
    def generate_new_products(cls):
        """Delete all products and create new based on CATEGORY_PRODUCTS_VARIANTS."""

        cls.objects.all().delete()
        categories = Category.objects.all()
        products_to_create = [
            cls(
                name=product_name,
                slug=slugify(product_name),
                category=categories.filter(slug=slugify(category_name)).first()
            )
            for category_name, category_data in CATEGORY_PRODUCTS_VARIANTS.items()
            for product_name in category_data['products']
        ]
        cls.objects.bulk_create(products_to_create)

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

    @classmethod
    def generate_new_variants(cls, max_variants_number=3):
        """Delete all variants and create new based on CATEGORY_PRODUCTS_VARIANTS."""

        cls.objects.all().delete()
        fake = Faker()
        products = Product.objects.all()
        variants_to_create = [
            cls(
                product=products.filter(slug=slugify(product_name)).first(),
                name=random.choice(category_data['variants']),
                stock_code=fake.unique.ean(length=13),
                unit_price=round(random.uniform(10.0, 500.0), 2)
            )
            for category_name, category_data in CATEGORY_PRODUCTS_VARIANTS.items()
            for product_name in category_data['products']
            for x in range(random.randint(1, max_variants_number))
        ]
        cls.objects.bulk_create(variants_to_create)

    def __str__(self):  # noqa: D105
        return f'{self.product} - {self.name}'

    class Meta:  # noqa: D106
        verbose_name = _('Wariant produktu')
        verbose_name_plural = _('Warianty produktów')
