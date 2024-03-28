"""Countries models."""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(models.Model):  # noqa: D101
    name = models.CharField(
        _('Nazwa'),
        max_length=64,
        unique=True,
    )

    def __str__(self):  # noqa: D105
        return self.name

    class Meta:  # noqa: D106
        verbose_name = _('Państwo')
        verbose_name_plural = _('Państwa')
