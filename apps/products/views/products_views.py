"""Products views."""
# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView

# Local
from ..forms.products_forms import ProductForm, ProductVariantFormset
from ..models import Product


class ProductListView(ListView):  # noqa: D101
    model = Product
    template_name = 'products/products_list.html'


class ProductCreateView(CreateView):  # noqa: D101
    model = Product
    template_name = 'products/products_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formset'] = ProductVariantFormset()
        return context


class ProductDeleteView(DeleteView):  # noqa: D101
    model = Product
    template_name = 'products/products_delete.html'
    success_url = reverse_lazy('products:products_list')
