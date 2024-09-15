"""Recommendations views."""

# Django
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

# Local
from .utils import get_recommended_products_by_interactions


class RecommendedProductsView(View):
    """View for getting recommended products."""

    def get(self, request, *args, **kwargs):
        """Get recommended products for given user."""

        user_id = int(self.request.GET.get('user_id'))
        try:
            recommended_products = get_recommended_products_by_interactions(user_id)
            return JsonResponse({
                'html': render_to_string(
                    'orders/_partials/recommended_products.html',
                    {
                        'products': recommended_products,
                    },
                    request=request,
                ),
            }, status=200)
        except ValueError as e:
            return JsonResponse({
                'error_message': str(e),
            }, status=400)
