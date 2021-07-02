from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from django.utils import translation
from django.utils.translation import gettext as _, ngettext as _n

# Register your models here.

def login(request):
    template_name = "account/login.html"
    form = forms.LoginForm( request.POST or None, use_required_attribute=False )
    
    if request.method == 'POST':
        if form.is_valid():
            return redirect(reverse('account:example'))

    context = {
        'form': form,
    }
    return render(request, template_name, context)


def example(request):
    template_name = "account/example.html"
    n = 1
    message1 = _n('%d archivo actualizado', '%d archivos actualizados', n)%n
    message2 = _n('{contactos} contacto actualizado', '{contactos} contactos actualizados', n).format(contactos=n)
    
    context = {
        'message1': message1,
        'message2': message2
    }
    return render(request, template_name, context)
    #return HttpResponse(f'{message1} <br>{message2}<br>OK!')