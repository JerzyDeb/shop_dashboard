"""Core forms."""

# Django
from django import forms

# Project
from apps.core.mixins import BootstrapFormMixin
from apps.core.models import Settings


class SettingsForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Settings
        fields = '__all__'
