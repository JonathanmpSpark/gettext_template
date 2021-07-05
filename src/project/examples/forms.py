from django import forms
from django.utils.translation import (
    pgettext_lazy as _c,
    ugettext_lazy as _,
)


class ExampleForm(forms.Form):
    qty = forms.CharField(
        required = False,
        label = _('Cantidad de artículos'),
        max_length = 3,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )

    state = forms.CharField(
        required = False,
        label = _c('País', 'Estado'),
        max_length = 3,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )

    status = forms.CharField(
        required = False,
        label = _c('Estatus', 'Estado'),
        max_length = 3,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )