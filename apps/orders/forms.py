"""Orders forms."""

# Django
from django import forms
from django.forms import inlineformset_factory

# Project
from apps.core.mixins import BootstrapFormMixin

# Local
from .models import Order
from .models import OrderItem


class OrderForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = Order
        fields = [
            'number',
            'user',
            'country',
        ]


class OrderItemForm(BootstrapFormMixin, forms.ModelForm):  # noqa: D101

    class Meta:  # noqa: D106
        model = OrderItem
        fields = [
            'product_variant',
            'quantity',
        ]


OrderItemFormset = inlineformset_factory(
    Order,
    OrderItem,
    form=OrderItemForm,
    extra=1,
)