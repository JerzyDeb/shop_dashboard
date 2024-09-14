"""Core views."""
# Django
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import UpdateView

# Project
from apps.accounts.models import CustomUser
from apps.core.forms import SettingsForm
from apps.core.models import Settings
from apps.countries.models import Country
from apps.orders.models import Order
from apps.orders.models import OrderItem
from apps.products.models import Category
from apps.products.models import Product
from apps.products.models import ProductVariant


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        """Pass statistic to context."""

        context = super().get_context_data(**kwargs)
        context['users_count'] = CustomUser.objects.count()
        context['new_users'] = CustomUser.objects.filter(
            date_joined__date=timezone.now().date(),
        ).count()
        context['orders_count'] = Order.objects.count()
        context['new_orders'] = Order.objects.filter(
            purchased_date__date=timezone.now().date(),
        ).count()
        context['products_count'] = Product.objects.count()
        context['variants_count'] = ProductVariant.objects.count()
        return context


class SettingsUpdateView(UpdateView):  # noqa: D101
    model = Settings
    template_name = 'settings_update.html'
    form_class = SettingsForm
    success_url = reverse_lazy('core:index')


class ReloadDataView(View):
    """View for reload all data in database."""

    success_url = reverse_lazy('core:index')

    def post(self, *args, **kwargs):
        """Reload all data in database."""

        Country.generate_new_countries()
        CustomUser.generate_new_users()

        Category.generate_new_categories()
        Product.generate_new_products()
        ProductVariant.generate_new_variants()

        Order.generate_new_orders()
        OrderItem.generate_new_orders_items()

        return HttpResponseRedirect(self.success_url)
