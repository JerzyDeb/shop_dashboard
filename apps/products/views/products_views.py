"""Products views."""
# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

# Project
from apps.core.mixins import InlineFormsetMixin

# Local
from ..forms.products_forms import ProductForm
from ..forms.products_forms import ProductVariantFormset
from ..models import Product


class ProductListView(ListView):  # noqa: D101
    model = Product
    template_name = 'products/products_list.html'


class ProductCreateView(InlineFormsetMixin, CreateView):  # noqa: D101
    model = Product
    template_name = 'products/products_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_context_data(self, **kwargs):
        """Pass ProductVariantFormset to context."""

        context = super().get_context_data(**kwargs)
        context['formset'] = ProductVariantFormset()
        if self.request.POST:
            context['formset'] = ProductVariantFormset(self.request.POST)
        return context


class ProductUpdateView(InlineFormsetMixin, UpdateView):  # noqa: D101
    model = Product
    template_name = 'products/products_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_context_data(self, **kwargs):
        """Pass ProductVariantFormset to context."""

        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['formset'] = ProductVariantFormset(instance=product)
        if self.request.POST:
            context['formset'] = ProductVariantFormset(
                self.request.POST,
                instance=product,
            )
        return context


class ProductDeleteView(DeleteView):  # noqa: D101
    model = Product
    template_name = 'products/products_delete.html'
    success_url = reverse_lazy('products:products_list')
