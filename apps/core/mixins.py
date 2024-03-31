"""Core mixins."""

# Local
from .utils import set_bootstrap_class


class BootstrapFormMixin:
    """Mixin for setting bootstrap classes to form fields."""

    def __init__(self, *args, **kwargs):
        """Set bootstrap classes."""

        super().__init__(*args, **kwargs)
        set_bootstrap_class(self.fields)
