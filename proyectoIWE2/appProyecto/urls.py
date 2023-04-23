from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    
    path('productos/', views.ProductosListView.as_view(), name='lista productos'),
    path('productos/<int:pk>/',
         views.ProductoDetailView.as_view(), name='detalle producto'),
     path('productos/create/',
         views.ProductoCreateView.as_view(), name='crear producto'),

    path('pedidos/',
         views.PedidosListView.as_view(), name='lista pedidos'),
    path('pedidos/<int:pk>',  views.PedidoDetailView.as_view(),
         name='detalle pedido'),
    path('categoria/<int:pk>/productos',
         views.CategoriaDetailView.as_view(), name='lista producto categoria'),
    path('categoria/',         views.CategoriasListView.as_view(),
         name='lista categorias'),

    path('productos/<int:pk>/componentes',
         views.ComponenteDetailView.as_view(), name='detalle componentes productos'),
    path('componentes/',
         views.ComponenteListView.as_view(), name='lista componentes'),
    path('clientes/',
         views.ClientesListView.as_view(), name='lista clientes'),
    path('clientes/<int:pk>',
         views.ClienteDetailView.as_view(), name='detalle cliente'),

     path('componentes/create', views.ComponenteCreateView.as_view(), name='componente_create'),
     path('componentes/<int:pk>/update/', views.ComponenteUpdateView.as_view(), name='departamento_update'),
     path('componentes/<int:pk>/delete/', views.ComponenteDeleteView.as_view(), name='departamento_delete'),
]
