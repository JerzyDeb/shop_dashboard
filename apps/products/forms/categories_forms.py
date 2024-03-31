"""Categories forms."""

# Django
from django import forms

# Project
from apps.core.mixins import BootstrapFormMixin

# Local
from ..models import Category


class CategoryForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Category
        fields = [
            'name',
        ]
