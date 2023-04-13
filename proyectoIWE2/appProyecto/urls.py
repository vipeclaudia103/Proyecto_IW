from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),

    path('producto', views.producto, name='producto'),

]
