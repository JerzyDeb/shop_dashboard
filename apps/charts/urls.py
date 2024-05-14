"""Charts urls."""

# Django
from django.urls import path

# Local
from .views import CountriesOrderChartView
from .views import CurrentMonthOrdersChartView
from .views import OrdersChartView
from .views import ProductCategoryChartView
from .views import TopSellsProductsChartView

app_name = 'charts'

urlpatterns = [
    path(
        'countries-orders/',
        CountriesOrderChartView.as_view(),
        name='countries_orders_chart',
    ),
    path(
        'categories-products/',
        ProductCategoryChartView.as_view(),
        name='categories_products_chart',
    ),
    path(
        'top-sells-products/',
        TopSellsProductsChartView.as_view(),
        name='top_sells_products_chart',
    ),
    path(
        'last-12-months-orders/',
        OrdersChartView.as_view(),
        name='last_12_month_orders_chart',
    ),
    path(
        'current-month-orders/',
        CurrentMonthOrdersChartView.as_view(),
        name='current_month_orders_chart',
    ),

]
