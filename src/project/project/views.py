from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

# Register your models here.

def default(request):
    return HttpResponseRedirect(reverse('i18n_account:login'))