"""Accounts views."""

# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

# Local
from .forms import CustomUserForm
from .models import CustomUser


class CustomUserListView(ListView):  # noqa: D101
    model = CustomUser
    template_name = 'accounts/users_list.html'
    paginate_by = 20


class CustomUserCreateView(CreateView):  # noqa: D101
    model = CustomUser
    template_name = 'accounts/users_create.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:users_list')


class CustomUserUpdateView(UpdateView):  # noqa: D101
    model = CustomUser
    template_name = 'accounts/users_update.html'
    form_class = CustomUserForm
    success_url = reverse_lazy('accounts:users_list')


class CustomUserDeleteView(DeleteView):  # noqa: D101
    model = CustomUser
    template_name = 'accounts/users_delete.html'
    success_url = reverse_lazy('accounts:users_list')
