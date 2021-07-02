from django import forms
from django.utils.translation import (
    pgettext as _c,
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
    
class ExampleForm(forms.Form):
    state = forms.CharField(
        required = False,
        label = _c('territorio', 'Estado'),
        max_length = 100,
        widget = forms.PasswordInput(
            attrs={
                'class': 'input100'
            }
        )
    )
    
    marital_CHOICES=[
        ( True, _('Claro que si') ),
        ( False, _('Aun no') )
    ]
    marital = forms.ChoiceField(
        required = False,
        label = _c('civil', 'Estado'),
        choices=marital_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                
            }
        )
    )
    
    status_CHOICES=[
        ( True, _('Activo') ),
        ( False, _('Inactivo') )
    ]
    status = forms.ChoiceField(
        required = False,
        label = _c('status', 'Estado'),
        choices=status_CHOICES,
        widget=forms.RadioSelect(
            attrs={
                
            }
        )
    )

    
    