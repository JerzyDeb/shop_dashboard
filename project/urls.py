"""Project urls."""

# Django
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('categories/', include('apps.products.urls.categories_urls')),
    path('products/', include('apps.products.urls.products_urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('orders/', include('apps.orders.urls')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
