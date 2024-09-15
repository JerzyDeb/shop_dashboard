"""Recommendations views."""

# Django
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import View

# Local
from .utils import get_recommended_products_by_interactions
from .utils import get_recommended_products_by_user_orders


class RecommendedProductsView(View):
    """View for getting recommended products."""

    def get(self, request, *args, **kwargs):
        """Get recommended products for given user."""

        user_id = int(self.request.GET.get('user_id'))
        try:
            return JsonResponse({
                'users_recommended_html': render_to_string(
                    'orders/_partials/users_recommended_products.html',
                    {
                        'products': get_recommended_products_by_interactions(user_id),
                    },
                    request=request,
                ),
                'products_recommended_html': render_to_string(
                    'orders/_partials/products_recommended_products.html',
                    {
                        'products': get_recommended_products_by_user_orders(user_id),
                    },
                    request=request,
                ),
            }, status=200)
        except ValueError as e:
            return JsonResponse({
                'error_message': str(e),
            }, status=400)
