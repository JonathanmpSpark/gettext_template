from django import forms
from django.utils.translation import (
    pgettext_lazy,
    ugettext_lazy as _,
    #gettext as _,
)

class LoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = _('Usuario'),
        max_length = 100,
        widget = forms.TextInput(
            attrs={
                'class': 'input100'
            }
        )
    )

    password = forms.CharField(
        required = True,
        label = _('Contraseña'),
        max_length = 100,
        widget = forms.PasswordInput(
            attrs={
                'class': 'input100'
            }
        )
    )
    


    
    