"""Products translations."""

# 3rd-Party
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import register

# Local
from .models import Category
from .models import Product
from .models import ProductVariant


@register(Product)
class ProductTranslationOptions(TranslationOptions):  # noqa: D101
    fields = [
        'name',
    ]


@register(ProductVariant)
class ProductVariantTranslationOptions(TranslationOptions):  # noqa: D101
    fields = [
        'name',
    ]


@register(Category)
class CategoryTranslationOptions(TranslationOptions):  # noqa: D101
    fields = [
        'name',
    ]
