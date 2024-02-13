from django.urls import path

from .views.unidad_views import *
from .views.clas_producto_views import *
from .views.clas_producto_det_views import *
from .views.marca_views import *
from .views.modelo_views import *
from .views.ubicacion_views import *


urlpatterns = [
	# -- Unidades.
	path('unidade/listar/', 
		UnidadListView.as_view(), name='unidad_list'),
	path('unidade/crear/', 
		UnidadCreateView.as_view(), name='unidad_create'),
	path('unidade/editar/<int:pk>/', 
		UnidadUpdateView.as_view(), name='unidad_update'),
	path('unidade/eliminar/<int:pk>/', 
		UnidadDeleteView.as_view(), name='unidad_delete'),
	
	# -- Familias.
	path('clas_producto/listar/', 
		ClasProductoListView.as_view(), name='clas_producto_list'),
	path('clas_producto/crear/',
		ClasProductoCreateView.as_view(), name='clas_producto_create'),
	path('clas_producto/editar/<int:pk>/', 
		ClasProductoUpdateView.as_view(), name='clas_producto_update'),
	path('clas_producto/eliminar/<int:pk>/', 
		ClasProductoDeleteView.as_view(), name='clas_producto_delete'),
	
	# -- Sub Familias.
	path('clas_producto_det/listar/',
		ClasProductoDetListView.as_view(), name='clas_producto_det_list'),
	path('clas_producto_det/crear/',
		ClasProductoDetCreateView.as_view(), name='clas_producto_det_create'),
	path('clas_producto_det/editar/<int:pk>/', 
		ClasProductoDetUpdateView.as_view(), name='clas_producto_det_update'),
	path('clas_producto_det/eliminar/<int:pk>/', 
		ClasProductoDetDeleteView.as_view(), name='clas_producto_det_delete'),
	
	# -- Marcas.
	path('marca/listar/',
		MarcaListView.as_view(), name='marca_list'),
	path('marca/crear/',
		MarcaCreateView.as_view(), name='marca_create'),
	path('marca/editar/<int:pk>/', 
		MarcaDetUpdateView.as_view(), name='marca_update'),
	path('marca/eliminar/<int:pk>/', 
		MarcaDeleteView.as_view(), name='marca_delete'),
	
	# -- Modelos.
	path('modelo/listar/',
		ModeloListView.as_view(), name='modelo_list'),
	path('modelo/crear/',
		ModeloCreateView.as_view(), name='modelo_create'),
	path('modelo/editar/<int:pk>/', 
		ModeloUpdateView.as_view(), name='modelo_update'),
	path('modelo/eliminar/<int:pk>/', 
		ModeloDeleteView.as_view(), name='modelo_delete'),
	
	# -- Ubicaciones.
	path('ubicacion/listar/',
		UbicacionListView.as_view(), name='ubicacion_list'),
	path('ubicacion/crear/',
		UbicacionCreateView.as_view(), name='ubicacion_create'),
	path('ubicacion/editar/<int:pk>/', 
		UbicacionUpdateView.as_view(), name='ubicacion_update'),
	path('ubicacion/eliminar/<int:pk>/', 
		UbicacionDeleteView.as_view(), name='ubicacion_delete'),
	
]
