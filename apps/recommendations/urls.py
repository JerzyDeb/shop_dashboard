"""Recommendations urls."""

# Django
from django.urls import path

# Local
from .views import RecommendedProductsView

app_name = 'recommendations'

urlpatterns = [
    path(
        'get-recommended-products',
        RecommendedProductsView.as_view(),
        name='get_recommended_products',
    ),
]
