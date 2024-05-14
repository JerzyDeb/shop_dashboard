"""Core views."""
from collections import OrderedDict

from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth, ExtractDay
from django.http import JsonResponse
from django.utils import timezone
from django.views import View
from django.utils.translation import gettext_lazy as _
# Django
from django.views.generic import TemplateView

from apps.accounts.models import CustomUser
from apps.charts.mixins import ChartMixin
from apps.orders.models import Order, OrderItem
from apps.products.models import Product, ProductVariant


class IndexView(TemplateView):  # noqa: D101
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users_count'] = CustomUser.objects.count()
        context['new_users'] = CustomUser.objects.filter(date_joined__day=timezone.now().day).count()
        context['orders_count'] = Order.objects.count()
        context['new_orders'] = Order.objects.filter(purchased_date__day=timezone.now().day).count()
        context['products_count'] = Product.objects.count()
        context['variants_count'] = ProductVariant.objects.count()
        return context


class CountriesOrderChartView(ChartMixin, View):
    type = 'doughnut'
    label = _('Zamówienia')
    title = _('Zamówienia według krajów')
    display_legend = False

    @staticmethod
    def _get_queryset():
        return Order.objects.values('country__name').annotate(order_count=Count('id')).order_by('-order_count')[:5]

    def get_labels(self):
        return list(self._get_queryset().values_list('country__name', flat=True))

    def get_data(self):
        return list(self._get_queryset().values_list('order_count', flat=True))


class OrdersChartView(ChartMixin, View):
    type = 'line'
    label = _('Zamówienia')
    title = _('Zamówienia')

    @staticmethod
    def _get_queryset():
        current_year = timezone.now().year

        # Użyj agregacji, aby zliczyć ilość zamówień dla każdego miesiąca w bieżącym roku
        return Order.objects.filter(purchased_date__year=current_year) \
            .annotate(month=ExtractMonth('purchased_date')) \
            .values('month') \
            .annotate(order_count=Count('id')) \
            .order_by('month')

    def get_labels(self):
        return [
            _('Styczeń'),
            _('Luty'),
            _('Marzec'),
            _('Kwiecień'),
            _('Maj'),
            _('Czerwiec'),
            _('Lipiec'),
            _('Sierpień'),
            _('Wrzesień'),
            _('Październik'),
            _('Listopad'),
            _('Grudzień'),
        ]

    def get_data(self):
        qs = self._get_queryset()
        orders_by_month_dict = {month['month']: month['order_count'] for month in qs}
        for month in range(1, 13):
            if month not in orders_by_month_dict:
                orders_by_month_dict[month] = 0
        sorted_dict = OrderedDict(sorted(orders_by_month_dict.items()))
        return list(sorted_dict.values())


class CurrentMonthOrdersChartView(ChartMixin, View):
    type = 'bar'
    label = _('Zamówienia')
    title = _('Zamówienia')

    def get_labels(self):
        return [
            i for i in range(1, 32)
        ]

    @staticmethod
    def _get_queryset():
        now = timezone.now()

        return Order.objects.filter(
            purchased_date__year=now.year,
            purchased_date__month=now.month,
        ).annotate(
            day=ExtractDay('purchased_date'),
        ).values(
            'day',
        ).annotate(
            order_count=Count('id'),
        ).order_by(
            'day',
        )

    @staticmethod
    def get_background_colors():
        return ['red']

    def get_data(self):
        qs = self._get_queryset()
        orders_by_day_dict = {
            day['day']: day['order_count']
            for day in qs
        }
        for day in range(1, 32):
            if day not in orders_by_day_dict:
                orders_by_day_dict[day] = 0
        sorted_dict = OrderedDict(sorted(orders_by_day_dict.items()))
        return list(sorted_dict.values())


class ProductCategoryChartView(ChartMixin, View):
    type = 'doughnut'
    label = _('Produkty')
    title = _('Ilość produktów w kategoriach')
    display_legend = False

    @staticmethod
    def _get_queryset():
        return Product.objects.values('category__name').annotate(product_count=Count('id')).order_by('category__name')[:5]

    def get_labels(self):
        return list(self._get_queryset().values_list('category__name', flat=True))

    def get_data(self):
        return list(self._get_queryset().values_list('product_count', flat=True))


class TopSellsProductsChartView(ChartMixin, View):
    type = 'doughnut'
    label = _('Zamówienia')
    title = _('Najlepiej sprzedające się produkty')
    display_legend = False

    @staticmethod
    def _get_queryset():
        return OrderItem.objects.values(
            'product_variant__product',
        ).annotate(
            product_count=Count('id'),
        ).order_by(
            '-product_count',
        )[:5]

    def get_labels(self):
        return list(self._get_queryset().values_list('product_variant__product__name', flat=True))

    def get_data(self):
        return list(self._get_queryset().values_list('product_count', flat=True))


class DoughnutChartView(ChartMixin, View):
    type = 'doughnut'
    label = 'My First Dataset'
    title = 'Donut'

    @staticmethod
    def get_labels():
        return ['Red', 'Blue', 'Yellow']

    @staticmethod
    def get_data():
        return [300, 50, 100]


class PolarAreaChartView(ChartMixin, View):
    type = 'polarArea'
    label = 'My First Dataset'
    title = 'POLAR'

    @staticmethod
    def get_labels():
        return [
            'Red',
            'Green',
            'Yellow',
            'Grey',
            'Blue',
        ]

    @staticmethod
    def get_data():
        return [11, 16, 7, 3, 14]
