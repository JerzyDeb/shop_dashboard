"""Core admin."""
# Django
from django.contrib import admin

# Project
from apps.core.models import Settings


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):  # noqa: D101
    pass
