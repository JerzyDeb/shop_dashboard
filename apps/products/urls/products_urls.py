"""Products urls."""

# Django
from django.urls import path

# Local
from ..views.products_views import ProductCreateView
from ..views.products_views import ProductDeleteView
from ..views.products_views import ProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('create/', ProductCreateView.as_view(), name='products_create'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='products_delete'),
]
