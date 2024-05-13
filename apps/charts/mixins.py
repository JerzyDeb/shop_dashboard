from django.http import JsonResponse


class ChartMixin:
    type = None
    label = None
    title = None
    display_title = True
    font_size = 25

    @staticmethod
    def _get_queryset():
        pass

    def get_labels(self):
        pass

    def get_data(self):
        pass

    @staticmethod
    def get_background_colors():
        return []

    def get_chart_data(self):
        datasets = {
            'label': self.label,
            'data': self.get_data(),
        }
        if self.get_background_colors():
            datasets['backgroundColors'] = self.get_background_colors()
        return {
            'labels': self.get_labels(),
            'datasets': [datasets]
        }

    def get_chart_options(self):
        return {
            'plugins': {
                'title': {
                    'display': self.display_title,
                    'text': self.title,
                    'font': {
                        'size': self.font_size,
                    }
                }
            }
        }

    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'type': self.type,
            'data': self.get_chart_data(),
            'options': self.get_chart_options(),
        })