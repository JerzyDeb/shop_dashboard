"""Countries models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Local
from .consts import COUNTRIES


class Country(models.Model):  # noqa: D101
    name = models.CharField(
        _('Nazwa'),
        max_length=64,
        unique=True,
    )

    @classmethod
    def generate_new_countries(cls):
        """Delete all countries and create new based on COUNTRIES."""

        cls.objects.all().delete()
        countries_to_create = [cls(name=country) for country in COUNTRIES]
        cls.objects.bulk_create(countries_to_create)

    def __str__(self):  # noqa: D105
        return self.name

    class Meta:  # noqa: D106
        verbose_name = _('Państwo')
        verbose_name_plural = _('Państwa')
