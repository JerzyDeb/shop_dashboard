"""Orders urls."""

# Django
from django.urls import path

# Local
from .views import OrderCreateView
from .views import OrderDeleteView
from .views import OrderListView
from .views import OrderUpdateView

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders_list'),
    path('create/', OrderCreateView.as_view(), name='orders_create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='orders_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='orders_delete'),
]
