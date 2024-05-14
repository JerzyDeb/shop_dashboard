"""Charts mixins."""

# Django
from django.http import JsonResponse


class ChartMixin:
    """Mixin for single chart."""

    type = None
    label = None
    title = None
    display_title = True
    display_legend = True
    font_size = 25
    background_color = None
    border_color = None

    def _get_queryset(self):
        """Retrieve specific queryset."""

        raise NotImplementedError

    def _get_labels(self):
        """Retrieve labels for the chart."""

        raise NotImplementedError

    def _get_data(self):
        """Retrieve data for the chart."""

        raise NotImplementedError

    def _get_chart_data(self):
        """
        Retrieve chart data.

        Returns:
            dict: A dictionary containing labels and datasets for the chart.
        """

        datasets = {
            'label': self.label,
            'data': self._get_data(),
        }
        return {
            'labels': self._get_labels(),
            'datasets': [datasets]
        }

    def _get_chart_options(self):
        """
        Retrieve chart options.

        Returns:
            dict: A dictionary containing options for the chart.
        """

        return {
            'plugins': {
                'legend': {
                    'display': self.display_legend,
                },
                'title': {
                    'display': self.display_title,
                    'text': self.title,
                    'font': {
                        'size': self.font_size,
                    }
                },
            },
            # 'layout': {
            #     'responsive': True,
            #     'maintainAspectRatio': False
            # },
            'responsive': True,
            'maintainAspectRatio': False,
            'aspectRatio': 1,
            # 'aspectRatio': 2 / 1,
        }

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        Args:
           request: The HTTP request object.
           *args: Additional positional arguments.
           **kwargs: Additional keyword arguments.

        Returns:
           JsonResponse: A JSON response containing the chart type, data, and options.
        """

        return JsonResponse({
            'type': self.type,
            'data': self._get_chart_data(),
            'options': self._get_chart_options(),
        })


class MixedChartMixin:
    """Mixin for two charts on one."""

    title = None
    display_title = True
    display_legend = True
    font_size = 25

    first_chart_type = None
    first_chart_label = None

    second_chart_type = None
    second_chart_label = None

    def _get_queryset(self):
        """Retrieve specific queryset."""

        raise NotImplementedError

    def _get_labels(self):
        """Retrieve labels for the chart."""

        raise NotImplementedError

    def _get_data(self):
        """Retrieve data for the chart."""

        raise NotImplementedError

    def _get_additional_data(self):
        """Retrieve data for the second chart."""

        raise NotImplementedError

    def _add_datasets(self):
        """
        Add additional datasets for the combined chart.

        Returns:
            list: A list of dictionaries containing additional datasets for the combined chart.
        """

        return [{
            'type': self.second_chart_type,
            'label': self.second_chart_label,
            'data': self._get_additional_data(),
            'yAxisID': 'B',
        }]

    def _get_chart_data(self):
        """
        Retrieve data for a combined chart.

        Returns:
            dict: A dictionary containing labels and datasets for the combined chart.
        """

        base_dataset = {
            'type': self.first_chart_type,
            'label': self.first_chart_label,
            'data': self._get_data(),
            'yAxisID': 'A',
        }
        datasets = [base_dataset] + self._add_datasets()
        return {
            'labels': self._get_labels(),
            'datasets': datasets
        }

    @staticmethod
    def _get_scales():
        return {
            'A': {
                'type': 'linear',
                'position': 'left',
            },
            'B': {
                'type': 'linear',
                'position': 'right',
            },
        }

    def _get_chart_options(self):
        """
        Retrieve chart options.

        Returns:
            dict: A dictionary containing options for the chart.
        """

        return {
            'plugins': {
                'legend': {
                    'display': self.display_legend,
                },
                'title': {
                    'display': self.display_title,
                    'text': self.title,
                    'font': {
                        'size': self.font_size,
                    }
                },
            },
            'responsive': True,
            'maintainAspectRatio': False,
            'aspectRatio': 1,
            'scales': self._get_scales(),
        }

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests.

        Args:
           request: The HTTP request object.
           *args: Additional positional arguments.
           **kwargs: Additional keyword arguments.

        Returns:
           JsonResponse: A JSON response containing the chart type, data, and options.
        """

        return JsonResponse({
            'data': self._get_chart_data(),
            'options': self._get_chart_options(),
        })
