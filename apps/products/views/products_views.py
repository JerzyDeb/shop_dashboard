"""Products views."""

# Django
from django.views.generic import ListView

# Local
from ..models import Product


class ProductListView(ListView):  # noqa: D101
    model = Product
    template_name = 'products/products_list.html'
