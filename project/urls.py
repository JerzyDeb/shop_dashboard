"""Project urls."""

# Django
from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('charts/', include('apps.charts.urls')),
    path('categories/', include('apps.products.urls.categories_urls')),
    path('products/', include('apps.products.urls.products_urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('orders/', include('apps.orders.urls')),
]

if not settings.DEBUG:
    urlpatterns += (
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    )

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if 'debug_toolbar' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls'))
    ]
