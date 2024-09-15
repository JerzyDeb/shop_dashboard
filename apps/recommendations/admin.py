"""Recommendations admin."""

# Django
from django.contrib import admin

# Local
from .models import UserProductInteraction


@admin.register(UserProductInteraction)
class ProductAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = [
        'user',
        'product',
        'interaction_type',
        'timestamp',
    ]
