"""Products urls."""

# Django
from django.urls import path

# Local
from ..views.categories_views import CategoryCreateView
from ..views.categories_views import CategoryDeleteView
from ..views.categories_views import CategoryListView
from ..views.categories_views import CategoryUpdateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories_list'),
    path('create/', CategoryCreateView.as_view(), name='categories_create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='categories_update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='categories_delete'),
]
