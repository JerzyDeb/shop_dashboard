"""Core views."""
# Django
from django.views.generic import TemplateView

from apps.accounts.models import CustomUser
from apps.orders.models import Order
from apps.products.models import Product, ProductVariant


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_count'] = CustomUser.objects.count()
        context['orders_count'] = Order.objects.count()
        context['products_count'] = Product.objects.count()
        context['variants_count'] = ProductVariant.objects.count()
        return context
