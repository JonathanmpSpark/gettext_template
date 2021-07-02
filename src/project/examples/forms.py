from django import forms
from django.utils.translation import (
    pgettext_lazy,
    ugettext_lazy as _,
)


class ExampleForm(forms.Form):
    singular_or_plural = forms.CharField(
        required = False,
        label = _('Cantidad de artículos'),
        max_length = 3,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )