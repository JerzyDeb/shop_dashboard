"""Recommendations admin."""

# Django
from django.contrib import admin

# Local
from .models import ProductTag
from .models import UserProductInteraction


@admin.register(UserProductInteraction)
class UserProductInteractionAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'user',
        'product',
        'interaction_type',
        'timestamp',
    ]


@admin.register(ProductTag)
class ProductTagAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'product',
        'tag',
    ]
