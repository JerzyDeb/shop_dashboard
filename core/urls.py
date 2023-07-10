"""Core urls."""

# Django
from django.urls import path

# Project
from core.views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
