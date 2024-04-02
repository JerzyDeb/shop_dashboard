"""Accounts forms."""

# Django
from django import forms

# Project
from apps.core.mixins import BootstrapFormMixin

# Local
from .models import CustomUser


class CustomUserForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'username',
            'is_staff',
        ]
