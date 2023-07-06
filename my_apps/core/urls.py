"""Core urls."""

# Django
from django.urls import path

# Project
from my_apps.core.views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
