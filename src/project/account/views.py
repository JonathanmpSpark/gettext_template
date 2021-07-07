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
            return redirect(reverse('i18n_examples:html'))

    context = {
        'form': form,
    }
    return render(request, template_name, context)
