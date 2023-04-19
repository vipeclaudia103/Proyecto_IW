from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='principal'),
    path('producto/', views.producto, name='producto'),

]
