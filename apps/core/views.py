"""Core views."""
# Django
from django.db.models import Count
from django.db.models import F
from django.db.models import Q
from django.db.models import Value
from django.db.models.functions import Coalesce
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
from apps.recommendations.models import UserProductInteraction


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'

    @staticmethod
    def interaction_count(interaction_type):
        """Count interactions of a specific type for each product."""

        interaction_type_dict = {
            'view': UserProductInteraction.InteractionType.VIEW,
            'add_to_cart': UserProductInteraction.InteractionType.ADD_TO_CART,
            'rate': UserProductInteraction.InteractionType.RATE,
            'purchase': UserProductInteraction.InteractionType.PURCHASE,
        }

        return Coalesce(
            Count(
                'userproductinteraction',
                filter=Q(userproductinteraction__interaction_type=interaction_type_dict[interaction_type]),  # noqa: E501
            ), Value(0)
        )

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
        context['products_interactions'] = Product.objects.annotate(
            view_count=self.interaction_count('view'),
            add_to_cart_count=self.interaction_count('add_to_cart'),
            rate_count=self.interaction_count('rate'),
            purchased_count=self.interaction_count('purchase'),
            total_count=F('view_count') + F('add_to_cart_count') + F('rate_count') + F('purchased_count')  # noqa: E501
        ).order_by('-total_count')
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

        UserProductInteraction.generate_new_interactions()

        return HttpResponseRedirect(self.success_url)
