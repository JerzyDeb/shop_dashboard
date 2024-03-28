"""Products managers."""

# Django
from django.db.models import Manager


class ProductVariantCustomManager(Manager):  # noqa: D101
    def get_queryset(self):  # noqa: D102
        return super().get_queryset().select_related(
            'product',
        )
