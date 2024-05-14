"""Core views."""

# Django
from django.utils import timezone
from django.views.generic import TemplateView

# Project
from apps.accounts.models import CustomUser
from apps.orders.models import Order
from apps.products.models import Product
from apps.products.models import ProductVariant


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Pass statistic to context."""

        context = super().get_context_data(**kwargs)
        context['users_count'] = CustomUser.objects.count()
        context['new_users'] = CustomUser.objects.filter(
            date_joined__day=timezone.now().day,
        ).count()
        context['orders_count'] = Order.objects.count()
        context['new_orders'] = Order.objects.filter(
            purchased_date__day=timezone.now().day,
        ).count()
        context['products_count'] = Product.objects.count()
        context['variants_count'] = ProductVariant.objects.count()
        return context
