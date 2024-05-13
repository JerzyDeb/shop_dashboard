"""Core urls."""

# Django
from django.urls import path

# Local
from .views import IndexView, CountriesOrderChartView, DoughnutChartView, PolarAreaChartView, OrdersChartView

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('chart/', CountriesOrderChartView.as_view(), name='line_chart_json'),
    path('donut/', OrdersChartView.as_view(), name='orders'),
    path('polar/', PolarAreaChartView.as_view(), name='polar'),
]
