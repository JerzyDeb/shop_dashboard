"""Countries translations."""

# 3rd-Party
from modeltranslation.translator import TranslationOptions
from modeltranslation.translator import register

# Local
from .models import Country


@register(Country)
class CountryTranslationOptions(TranslationOptions):  # noqa: D101
    fields = [
        'name',
    ]
