"""Orders admin."""

# Django
from django.contrib import admin

# Local
from .models import Order
from .models import OrderItem


class OrderItemInline(admin.TabularInline):  # noqa: D101
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):  # noqa: D101
    list_display = ['number', 'purchased_date']
    inlines = [
        OrderItemInline,
    ]
