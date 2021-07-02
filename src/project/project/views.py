from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse

# Register your models here.

def default(request):
    return HttpResponseRedirect(reverse('i18n_account:login'))