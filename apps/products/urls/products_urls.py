"""Products urls."""

# Django
from django.urls import path

# Local
from ..views.products_views import ProductCreateView
from ..views.products_views import ProductDeleteView
from ..views.products_views import ProductListView
from ..views.products_views import ProductUpdateView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('create/', ProductCreateView.as_view(), name='products_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='products_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='products_delete'),
]
