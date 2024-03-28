"""Products admin."""

# Django
from django.contrib import admin

# Local
from .models import Category
from .models import Product
from .models import ProductVariant


class ProductVariantInline(admin.TabularInline):  # noqa: D101
    model = ProductVariant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # noqa: D101
    inlines = [
        ProductVariantInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # noqa: D101
    pass
