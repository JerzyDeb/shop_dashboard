"""Products utils."""

# 3rd-Party
from slugify import slugify


def set_slug(obj):
    """Set slug field value for object."""

    if not obj.pk:
        obj.slug = slugify(obj.name)
