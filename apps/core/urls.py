"""Core urls."""

# Django
from django.urls import path

# Local
from .views import IndexView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
