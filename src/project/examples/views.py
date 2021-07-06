# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from django.utils import translation
from django.utils.translation import gettext as _, ngettext as _n

# Create your views here.

def html(request):
    form = forms.ExampleForm( request.POST or None, use_required_attribute=False )
    
    context = {
        'hello_word': _('Hola Mundo'),
    }
    return render(request, "examples/example_html.html", context)


def py(request):
    form = forms.ExampleForm( request.POST or None, use_required_attribute=False )
    
    context = {
        'form': form,
        'hello_word': _('Hola Mundo'),
    }
    return render(request, "examples/example_py.html", context)


def js(request):
    form = forms.ExampleForm( request.POST or None, use_required_attribute=False )
    
    context = {
        'form': form
    }
    return render(request, "examples/example_js.html", context)
