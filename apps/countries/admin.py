"""Countries admin."""

# Django
from django.contrib import admin

# Local
from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):  # noqa: D101
    pass
