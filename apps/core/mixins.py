"""Core mixins."""

# Local
from .utils import set_bootstrap_class


class BootstrapFormMixin:
    """Mixin for setting bootstrap classes to form fields."""

    def __init__(self, *args, **kwargs):
        """Set bootstrap classes."""

        super().__init__(*args, **kwargs)
        set_bootstrap_class(self.fields)


class InlineFormsetMixin:
    """Mixin for saving inline models in view."""

    def form_valid(self, form):
        """Save the formset."""

        formset = self.get_context_data()['formset']
        if formset.is_valid():
            instance = form.save()
            formset.instance = instance
            formset.save()
            return super().form_valid(form)
        return self.render_to_response(
            self.get_context_data(
                form=form,
                formset=formset
            )
        )
