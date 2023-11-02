from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='lista'),
    path('add_item', views.add_item, name='add_item')
]