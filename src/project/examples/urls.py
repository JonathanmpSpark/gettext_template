from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'examples'

urlpatterns = [
    path('html', views.html, name='html'),
    path('py', views.py, name='py'),
    path('js', views.js, name='js'),
]