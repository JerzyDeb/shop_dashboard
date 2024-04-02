"""Orders views."""
# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

# Project
from apps.core.mixins import InlineFormsetMixin

# Local
from .forms import OrderForm
from .forms import OrderItemFormset
from .models import Order


class OrderListView(ListView):  # noqa: D101
    model = Order
    template_name = 'orders/orders_list.html'


class OrderCreateView(InlineFormsetMixin, CreateView):  # noqa: D101
    model = Order
    template_name = 'orders/orders_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        """Pass OrderItemFormset to context."""

        context = super().get_context_data(**kwargs)
        context['formset'] = OrderItemFormset()
        if self.request.POST:
            context['formset'] = OrderItemFormset(
                self.request.POST,
            )
        return context


class OrderUpdateView(InlineFormsetMixin, UpdateView):  # noqa: D101
    model = Order
    template_name = 'orders/orders_update.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        """Pass OrderItemFormset to context."""

        context = super().get_context_data(**kwargs)
        order = self.get_object()
        context['formset'] = OrderItemFormset(instance=order)
        if self.request.POST:
            context['formset'] = OrderItemFormset(
                self.request.POST,
                instance=order,
            )
        return context


class OrderDeleteView(DeleteView):  # noqa: D101
    model = Order
    template_name = 'orders/orders_delete.html'
    success_url = reverse_lazy('orders:orders_list')
