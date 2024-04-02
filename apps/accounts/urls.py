"""Accounts urls."""

# Django
from django.urls import path

# Local
from .views import CustomUserCreateView
from .views import CustomUserDeleteView
from .views import CustomUserListView
from .views import CustomUserUpdateView

app_name = 'accounts'

urlpatterns = [
    path('', CustomUserListView.as_view(), name='users_list'),
    path('create/', CustomUserCreateView.as_view(), name='users_create'),
    path('update/<int:pk>/', CustomUserUpdateView.as_view(), name='users_update'),
    path('delete/<int:pk>/', CustomUserDeleteView.as_view(), name='users_delete'),
]
