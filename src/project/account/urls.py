from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'account'

urlpatterns = [
    path('login', views.login, name='login'),
    path('example', views.example, name='example'),
]