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
    path('pedidos/create/',
         views.PedidoCreateView.as_view(), name='crear pedido'),
    path('pedidos/cantidad', views.CantidadCreateView.as_view(),
         name='crear cantidad'),
    path('categoria/<int:pk>',
         views.CategoriaDetailView.as_view(), name='detalle categoria'),
    path('categoria/',         views.CategoriasListView.as_view(),
         name='lista categorias'),

    path('componentes/<int:pk>',
         views.ComponenteDetailView.as_view(), name='detalle componentes'),
    path('componentes/',
         views.ComponenteListView.as_view(), name='lista componentes'),
    path('clientes/',
         views.ClientesListView.as_view(), name='lista clientes'),
    path('clientes/<int:pk>',
         views.ClienteDetailView.as_view(), name='detalle cliente'),
    path('cliente/create', views.ClienteCreateView.as_view(),
         name='crear cliente'),

    path('componentes/create', views.ComponenteCreateView.as_view(),
         name='crear componente'),
    path('componentes/<int:pk>/update/',
         views.ComponenteUpdateView.as_view(), name='actualiza componente'),
    path('componentes/<int:pk>/delete/',
         views.ComponenteDeleteView.as_view(), name='borra componente'),
]
