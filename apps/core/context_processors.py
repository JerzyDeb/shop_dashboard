"""Core context processors."""

# Local
from .models import Settings


def core(request):  # noqa: D103
    return {
        'settings': Settings.objects.get_or_create()[0],
    }
