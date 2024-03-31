"""Core utils."""


def set_bootstrap_class(fields):
    """Set Bootstrap classes for specific fields."""
    classes_dict = {
        'CharField': {
            'field': 'form-control',
        },
        'IntegerField': {
            'field': 'form-control',
        },
        'EmailField': {
            'field': 'form-control',
        },
        'ChoiceField': {
            'field': 'form-select',
        },
        'SlugField': {
            'field': 'form-control',
        },
        'TypedChoiceField': {
            'field': 'form-control bs-select',
        },
        'PasswordField': {
            'field': 'form-control',
        },
        'SetPasswordField': {
            'field': 'form-control',
        },
        'BooleanField': {
            'field': 'form-check-input',
        },
        'ModelChoiceField': {
            'field': 'form-select',
        },
        'RegexField': {
            'field': 'form-control',
        },
        'TreeNodeChoiceField': {
            'field': 'form-control bs-select',
        },
        'ModelMultipleChoiceField': {
            'field': 'form-select',
        },
        'ImageField': {
            'field': 'form-control',
        },
        'FileField': {
            'field': 'form-control',
        },
        'MoneyField': {
            'field': 'form-control',
        },
        'DecimalField': {
            'field': 'form-control',
        },
        'DateField': {
            'field': 'form-control custom-datepicker',
        },
        'DateTimeField': {
            'field': 'form-control form-control-clear bg-transparent rangepicker',
        },
        'DurationField': {
            'field': 'form-control',
        },
        'SimpleArrayField': {
            'field': 'form-control',
        },
        'URLField': {
            'field': 'form-control',
        },
        'NullCharField': {
            'field': 'form-control',
        },
        'MultipleFileField': {
            'field': '',
        },
        'FloatField': {
            'field': 'form-control',
        },
        'PhoneNumberField': {
            'field': 'form-control',
        },
        'UsernameField': {
            'field': 'form-control',
        },
    }
    for field in fields.values():
        try:
            old_class = field.widget.attrs.get('class', '')
            additional_class = classes_dict[field.__class__.__name__]['field']
            field.widget.attrs.update(
                {
                    'class': f'{old_class} {additional_class}',
                    'placeholder': field.label,
                },
            )
        except KeyError:
            pass
