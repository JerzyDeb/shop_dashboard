"""Orders managers."""

# Django
from django.db.models import Manager


class OrderItemCustomManager(Manager):  # noqa: D101
    def get_queryset(self):  # noqa: D102
        return super().get_queryset().select_related(
            'order',
        )
