"""Core urls."""

# Django
from django.urls import path

# Local
from .views import IndexView, CountriesOrderChartView, DoughnutChartView, PolarAreaChartView, OrdersChartView, \
    CurrentMonthOrdersChartView, ProductCategoryChartView, TopSellsProductsChartView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chart/', CountriesOrderChartView.as_view(), name='line_chart_json'),
    path('donut/', OrdersChartView.as_view(), name='orders'),
    path('donut11/', CurrentMonthOrdersChartView.as_view(), name='orders_month'),
    path('donut1111/', ProductCategoryChartView.as_view(), name='product_categories'),
    path('donut1111xxx/', TopSellsProductsChartView.as_view(), name='top_products'),
    path('polar/', PolarAreaChartView.as_view(), name='polar'),
]
