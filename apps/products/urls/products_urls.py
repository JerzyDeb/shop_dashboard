"""Products urls."""

# Django
from django.urls import path

# Local
from ..views.products_views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
]
