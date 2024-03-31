"""Products urls."""

# Django
from django.urls import include
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('products/', include('apps.products.urls.products_urls')),
    path('categories/', include('apps.products.urls.categories_urls')),
]
