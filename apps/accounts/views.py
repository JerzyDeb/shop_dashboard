"""Accounts views."""
from django.views.generic import ListView

from .models import CustomUser


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'accounts/users_list.html'
