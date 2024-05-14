"""Charts views."""

# Standard Library
from collections import OrderedDict
from datetime import datetime

# Django
from django.db.models import Count
from django.db.models import F
from django.db.models import Sum
from django.db.models.functions import ExtractDay
from django.db.models.functions import ExtractMonth
from django.db.models.functions import ExtractYear
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views import View

# 3rd-Party
from dateutil.relativedelta import relativedelta

# Project
from apps.charts.mixins import ChartMixin
from apps.charts.mixins import MixedChartMixin
from apps.orders.models import Order
from apps.orders.models import OrderItem
from apps.products.models import Product


class CountriesOrderChartView(ChartMixin, View):
    """
    View to show the number of orders group by country in a doughnut chart.
    """

    type = 'doughnut'
    label = _('Zamówienia')
    title = _('Zamówienia według krajów')
    display_legend = False

    def _get_queryset(self):
        """
        Retrieve the top 5 countries based on the count of orders.

        Returns:
            QuerySet: A queryset containing the top 5 countries
            along with the count of orders for each country.
        """

        return Order.objects.values(
            'country__name',
        ).annotate(
            order_count=Count('id'),
        ).order_by(
            '-order_count',
        )[:5]

    def _get_labels(self):
        """
        Retrieve the labels (country names) for the chart.

        Returns:
            list: A list of country names.
        """

        return list(
            self._get_queryset().values_list(
                'country__name',
                flat=True,
            ),
        )

    def _get_data(self):
        """
        Retrieve the data (order counts) for the chart.

        Returns:
            list: A list of order counts.
        """

        return list(
            self._get_queryset().values_list(
                'order_count',
                flat=True,
            ),
        )


class TopSellsProductsChartView(ChartMixin, View):
    """
    View to show the number of orders group by products in a doughnut chart.
    """

    type = 'doughnut'
    label = _('Zamówienia')
    title = _('Najlepiej sprzedające się produkty')
    display_legend = False

    def _get_queryset(self):
        """
        Retrieve the top 5 products based on the count of orders.

        Returns:
            QuerySet: A queryset containing the top 5 products
            along with the count of orders for each product.
        """

        return OrderItem.objects.values(
            'product_variant__product',
        ).annotate(
            product_count=Count('id'),
        ).order_by(
            '-product_count',
        )[:5]

    def _get_labels(self):
        """
        Retrieve the labels (product names) for the chart.

        Returns:
            list: A list of product names.
        """

        return list(
            self._get_queryset().values_list(
                'product_variant__product__name',
                flat=True,
            ),
        )

    def _get_data(self):
        """
        Retrieve the data (order counts) for the chart.

        Returns:
            list: A list of order counts.
        """

        return list(
            self._get_queryset().values_list(
                'product_count',
                flat=True,
            ),
        )


class ProductCategoryChartView(ChartMixin, View):
    """
    View to show the number of products group by category in a doughnut chart.
    """

    type = 'doughnut'
    label = _('Produkty')
    title = _('Ilość produktów w kategoriach')
    display_legend = False

    def _get_queryset(self):
        """
        Retrieve the top 5 categories based on the count of products.

        Returns:
            QuerySet: A queryset containing the top 5 categories
            along with the count of products for each category.
        """

        return Product.objects.values(
            'category__name',
        ).annotate(
            product_count=Count('id'),
        ).order_by(
            'category__name',
        )[:5]

    def _get_labels(self):
        """
        Retrieve the labels (category names) for the chart.

        Returns:
            list: A list of category names.
        """

        return list(
            self._get_queryset().values_list(
                'category__name',
                flat=True,
            ),
        )

    def _get_data(self):
        """
        Retrieve the data (products counts) for the chart.

        Returns:
            list: A list of products counts.
        """

        return list(
            self._get_queryset().values_list(
                'product_count',
                flat=True,
            ),
        )


class OrdersChartView(MixedChartMixin, View):
    """
    View to show the number and value of orders in last 12 months in a line-bar chart.
    """

    title = _('Zamówienia - ostatnie 12 miesięcy')

    first_chart_type = 'line'
    first_chart_label = _('Wartość zamówień')

    second_chart_type = 'bar'
    second_chart_label = _('Ilość zamówień')

    @staticmethod
    def _get_last_12_months():
        """
        Retrieve the dates for the last 12 months.

        Returns:
            list: A list of datetime objects representing the dates for the last 12 months.
        """

        now = timezone.now()
        return [
            now - relativedelta(month=i)
            if i <= now.month
            else
            now - relativedelta(month=i, years=1)
            for i in range(1, 13)
        ]

    def _get_specific_data(self, specific_field_name):
        """
        Retrieve data for each month for the last 12 months.

        Args:
            specific_field_name (str):
            The name of the specific field for which data is to be retrieved.

        Returns:
            list: A list of specific data values for each month for the last 12 months.
        """

        qs = self._get_queryset()
        orders_by_month_dict = {
            f'{month["month"]}-{month["year"]}': month[specific_field_name]
            for month in qs
        }
        last_12_months = self._get_last_12_months()

        for m in last_12_months:
            if f'{m.month}-{m.year}' not in orders_by_month_dict:
                orders_by_month_dict[f'{m.month}-{m.year}'] = 0

        sorted_data = OrderedDict(
            sorted(
                orders_by_month_dict.items(),
                key=lambda x: datetime.strptime(x[0], '%m-%Y'),
            ),
        )

        return list(sorted_data.values())

    def _get_queryset(self):
        """
        Retrieve queryset for the last 12 months.

        Returns:
            QuerySet: A queryset containing data for the last 12 months,
            annotated with order count and total value.
        """

        last_12_months = self._get_last_12_months()
        return Order.objects.filter(
            purchased_date__month__in=[m.month for m in last_12_months],
            purchased_date__year__in=[m.year for m in last_12_months],
        ).annotate(
            month=ExtractMonth('purchased_date'),
            year=ExtractYear('purchased_date'),
        ).values(
            'month',
            'year',
        ).annotate(
            order_count=Count('id'),
            total_value=Sum(
                F('orderitem__unit_price') * F('orderitem__quantity')
            ),
        ).order_by(
            'year',
            'month',
        )

    def _get_labels(self):
        """
        Retrieve labels (month-year) for the chart.

        Returns:
            list: A list of strings representing the labels for the last 12 months.
        """

        last_12_months = self._get_last_12_months()
        last_12_months.sort()
        return [
            f'{month.month}-{month.year}'
            for month in last_12_months
        ]

    def _get_data(self):  # noqa: D105
        return self._get_specific_data('total_value')

    def _get_additional_data(self):  # noqa: D105
        return self._get_specific_data('order_count')


class CurrentMonthOrdersChartView(MixedChartMixin, View):
    """
    View to show the number and value of orders in current month in a line-bar chart.
    """

    title = _('Zamówienia - aktualny miesiąc')

    first_chart_type = 'line'
    first_chart_label = _('Wartość zamówień')

    second_chart_type = 'bar'
    second_chart_label = _('Ilość zamówień')

    def _get_specific_data(self, specific_field_name):
        """
        Retrieve data for each day in current month.

        Args:
            specific_field_name (str):
            The name of the specific field for which data is to be retrieved.

        Returns:
            list: A list of specific data values for each day in current month.
        """

        qs = self._get_queryset()
        orders_by_day_dict = {
            day['day']: day[specific_field_name]
            for day in qs
        }
        for day in range(1, timezone.now().day + 1):
            if day not in orders_by_day_dict:
                orders_by_day_dict[day] = 0
        sorted_dict = OrderedDict(
            sorted(
                orders_by_day_dict.items(),
            ),
        )
        return list(sorted_dict.values())

    def _get_labels(self):
        """
        Retrieve labels (day number) for the chart.

        Returns:
            list: A list of strings representing the labels for each day in current month.
        """

        return [
            i for i in range(1, timezone.now().day + 1)
        ]

    def _get_queryset(self):
        """
        Retrieve queryset for each day in current month.

        Returns:
            QuerySet: A queryset containing data for each day in current month,
            annotated with order count and total value.
        """

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
            total_value=Sum(
                F('orderitem__unit_price') * F('orderitem__quantity'),
            ),
        ).order_by(
            'day',
        )

    def _get_data(self):  # noqa: D105
        return self._get_specific_data('total_value')

    def _get_additional_data(self):  # noqa: D105
        return self._get_specific_data('order_count')
