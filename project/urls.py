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
    path('', include('apps.products.urls.urls')),
    path('', include('apps.accounts.urls')),
]

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]
