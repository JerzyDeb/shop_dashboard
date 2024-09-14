"""Core urls."""

# Django
from django.urls import path

# Local
from .views import IndexView
from .views import ReloadDataView
from .views import SettingsUpdateView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('settings/<int:pk>/', SettingsUpdateView.as_view(), name='settings'),
    path('reload-data', ReloadDataView.as_view(), name='reload_data'),
]
