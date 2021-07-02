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

def example(request):
    form = forms.ExampleForm( request.POST or None, use_required_attribute=False )
    
    context = {

        'form': form
    }
    return render(request, "account/example.html", context)

def html(request):
    form = forms.ExampleForm( request.POST or None, use_required_attribute=False )
    
    context = {

        'form': form
    }
    return render(request, "examples/example_html.html", context)


def py(request):
    return HttpResponse('py')

def js(request):
    return HttpResponse('js')