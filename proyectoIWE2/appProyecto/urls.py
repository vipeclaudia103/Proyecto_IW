from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('productos/', views.ProductosListView.as_view(), name='lista productos'),
    path('productos/<int:pk>/',
         views.ProductoDetailView.as_view(), name='detalle producto'),
    path('productos/create/',
         views.ProductoCreateView.as_view(), name='crear producto'),
    path('productos/<int:pk>/update/',
         views.ProductoUpdateView.as_view(), name='actualiza producto'),
    path('productos/<int:pk>/delete/',
         views.ProductoDeleteView.as_view(), name='borrar producto'),

    path('elementos/<int:pk>/delete/',
         views.ElementoDeleteView.as_view(), name='borrar elemento'),

    path('pedidos/',
         views.PedidosListView.as_view(), name='lista pedidos'),
    path('pedidos/<int:pk>',  views.PedidoDetailView.as_view(),
         name='detalle pedido'),
    path('pedidos/create/',
         views.PedidoCreateView.as_view(), name='crear pedido'),
    path('pedidos/<int:pk>/delete/',
         views.PedidoDeleteView.as_view(), name='borrar pedido'),
    path('pedidos/<int:pk>/update/',
         views.PedidoUpdateView.as_view(), name='actualiza pedido'),

    path('pedidos/cantidad', views.CantidadCreateView.as_view(),
         name='crear cantidad'),
    path('cantidad/<int:pk>/delete/',
         views.CantidadDeleteView.as_view(), name='borrar cantidad'),
    path('cantidad/<int:pk>/update/',
         views.CantidadUpdateView.as_view(), name='actualizar cantidad'),

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
    path('clientes/<int:pk>/delete/',
         views.ClienteDeleteView.as_view(), name='borra cliente'),
    path('clientes/<int:pk>/update/',
         views.ClienteUpdateView.as_view(), name='actualiza cliente'),

    path('componentes/create', views.ComponenteCreateView.as_view(),
         name='crear componente'),
    path('componentes/<int:pk>/update/',
         views.ComponenteUpdateView.as_view(), name='actualiza componente'),
    path('componentes/<int:pk>/delete/',
         views.ComponenteDeleteView.as_view(), name='borra componente'),
     path('categoria/<int:pk>/update/',
         views.CategoriaUpdateView.as_view(), name='actualiza categoria'),
    path('categoria/<int:pk>/delete/',
         views.CategoriaDeleteView.as_view(), name='borra categoria'),
     path('categoria/create', views.CategoriaCreateView.as_view(),
          name='crear categoria'),

]
