"""Core urls."""

# Django
from django.urls import path

# Local
from .views import CustomUserListView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', CustomUserListView.as_view(), name='users_list'),
]
