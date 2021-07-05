from django.urls import path
from . import views
from . import api
from django.conf.urls import url


app_name = 'examples'

urlpatterns = [
    path('html', views.html, name='html'),
    path('py', views.py, name='py'),
    path('js', views.js, name='js'),


    path('api/add_item', api.agregar_al_carrito, name='add_to_cart'),
]