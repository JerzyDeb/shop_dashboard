"""Categories forms."""

# Django
from django import forms
from django.forms import modelformset_factory

# Project
from apps.core.mixins import BootstrapFormMixin

# Local
from ..models import Product
from ..models import ProductVariant


class ProductForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Product
        fields = [
            'name',
            'category',
        ]


class ProductVariantForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = ProductVariant
        fields = [
            'name',
            'stock_code',
            'unit_price',
        ]


ProductVariantFormset = modelformset_factory(ProductVariant, form=ProductVariantForm, extra=1)
