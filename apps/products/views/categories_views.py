"""Categories views."""

# Django
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import ListView
from django.views.generic import UpdateView

# Local
from ..forms.categories_forms import CategoryForm
from ..models import Category


class CategoryListView(ListView):  # noqa: D101
    model = Category
    template_name = 'categories/categories_list.html'
    paginate_by = 20


class CategoryCreateView(CreateView):  # noqa: D101
    model = Category
    template_name = 'categories/categories_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories:categories_list')


class CategoryUpdateView(UpdateView):  # noqa: D101
    model = Category
    template_name = 'categories/categories_update.html'
    form_class = CategoryForm
    success_url = reverse_lazy('categories:categories_list')


class CategoryDeleteView(DeleteView):  # noqa: D101
    model = Category
    template_name = 'categories/categories_delete.html'
    success_url = reverse_lazy('categories:categories_list')
