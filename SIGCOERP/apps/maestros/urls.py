from django.urls import path

from .views.unidad_views import *
from .views.clas_producto_views import *
from .views.clas_producto_det_views import *
from .views.marca_views import *
from .views.modelo_views import *
from .views.ubicacion_views import *
from .views.codigo_sunat_views import *
from .views.unidad_sunat_views import *
from .views.color_views import *
from .views.tipo_documento_identidad_views import *
from . views.ubigeo_views import *
from . views.forma_pago_views import *
from . views.clas_servicio_views import *
from . views.clas_gasto_views import *
from . views.clas_insumo_views import *
from . views.clas_activo_views import *
from . views.moneda_views import *
from . views.tipo_cambio_views import *
from . views.documento_sunat_views import *
from . views.zona_views import *
from . views.sub_zona_views import *
from . views.banco_views import *
from . views.caja_banco_views import *


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
	
	# -- Código SUNAT.
	path('codigo_sunat/listar/',
		CodigoSunatListView.as_view(), name='codigo_sunat_list'),
	path('codigo_sunat/crear/',
		CodigoSunatCreateView.as_view(), name='codigo_sunat_create'),
	path('codigo_sunat/editar/<int:pk>/', 
		CodigoSunatUpdateView.as_view(), name='codigo_sunat_update'),
	path('codigo_sunat/eliminar/<int:pk>/', 
		CodigoSunatDeleteView.as_view(), name='codigo_sunat_delete'),
	
	# -- Código Unidad SUNAT.
	path('unidad_sunat/listar/',
		UnidadSunatListView.as_view(), name='unidad_sunat_list'),
	path('unidad_sunat/crear/',
		UnidadSunatCreateView.as_view(), name='unidad_sunat_create'),
	path('unidad_sunat/editar/<int:pk>/', 
		UnidadSunatUpdateView.as_view(), name='unidad_sunat_update'),
	path('unidad_sunat/eliminar/<int:pk>/', 
		UnidadSunatDeleteView.as_view(), name='unidad_sunat_delete'),
	
	# -- Color.
	path('color/listar/',
		ColorListView.as_view(), name='color_list'),
	path('color/crear/',
		ColorCreateView.as_view(), name='color_create'),
	path('color/editar/<int:pk>/', 
		ColorUpdateView.as_view(), name='color_update'),
	path('color/eliminar/<int:pk>/', 
		ColorDeleteView.as_view(), name='color_delete'),
	
	# -- Tipo Documento Identidad.
	path('tipo_documento_identidad/listar/',
		TipoDocumentoIdentidadListView.as_view(), 
		name='tipo_documento_identidad_list'),
	path('tipo_documento_identidad/crear/',
		TipoDocumentoIdentidadCreateView.as_view(), 
		name='tipo_documento_identidad_create'),
	path('tipo_documento_identidad/editar/<int:pk>/', 
		TipoDocumentoIdentidadUpdateView.as_view(), 
		name='tipo_documento_identidad_update'),
	path('tipo_documento_identidad/eliminar/<int:pk>/', 
		TipoDocumentoIdentidadDeleteView.as_view(), 
		name='tipo_documento_identidad_delete'),
	
	# -- Ubigeo.
	path('ubigeo/listar/',
		UbigeoListView.as_view(), name='ubigeo_list'),
	path('ubigeo/crear/',
		UbigeoCreateView.as_view(), name='ubigeo_create'),
	path('ubigeo/editar/<int:pk>/', 
		UbigeoUpdateView.as_view(), name='ubigeo_update'),
	path('ubigeo/eliminar/<int:pk>/', 
		UbigeoDeleteView.as_view(), name='ubigeo_delete'),
	
	# -- Forma de Pago.
	path('forma_pago/listar/',
		FormaPagoListView.as_view(), name='forma_pago_list'),
	path('forma_pago/crear/',
		FormaPagoCreateView.as_view(), name='forma_pago_create'),
	path('forma_pago/editar/<int:pk>/', 
		FormaPagoUpdateView.as_view(), name='forma_pago_update'),
	path('forma_pago/eliminar/<int:pk>/', 
		FormaPagoDeleteView.as_view(), name='forma_pago_delete'),
	
	# -- Familia Servicio.
	path('clas_servicio/listar/', 
		ClasServicioListView.as_view(), name='clas_servicio_list'),
	path('clas_servicio/crear/',
		ClasServicioCreateView.as_view(), name='clas_servicio_create'),
	path('clas_servicio/editar/<int:pk>/', 
		ClasServicioUpdateView.as_view(), name='clas_servicio_update'),
	path('clas_servicio/eliminar/<int:pk>/', 
		ClasServicioDeleteView.as_view(), name='clas_servicio_delete'),
	
	# -- Familia Gasto.
	path('clas_gasto/listar/', 
		ClasGastoListView.as_view(), name='clas_gasto_list'),
	path('clas_gasto/crear/',
		ClasGastoCreateView.as_view(), name='clas_gasto_create'),
	path('clas_gasto/editar/<int:pk>/', 
		ClasGastoUpdateView.as_view(), name='clas_gasto_update'),
	path('clas_gasto/eliminar/<int:pk>/', 
		ClasGastoDeleteView.as_view(), name='clas_gasto_delete'),
	
	# -- Familia Insumo.
	path('clas_insumo/listar/', 
		ClasInsumoListView.as_view(), name='clas_insumo_list'),
	path('clas_insumo/crear/',
		ClasInsumoCreateView.as_view(), name='clas_insumo_create'),
	path('clas_insumo/editar/<int:pk>/', 
		ClasInsumoUpdateView.as_view(), name='clas_insumo_update'),
	path('clas_insumo/eliminar/<int:pk>/', 
		ClasInsumoDeleteView.as_view(), name='clas_insumo_delete'),
	
	# -- Familia Activo.
	path('clas_activo/listar/', 
		ClasActivoListView.as_view(), name='clas_activo_list'),
	path('clas_activo/crear/',
		ClasActivoCreateView.as_view(), name='clas_activo_create'),
	path('clas_activo/editar/<int:pk>/', 
		ClasActivoUpdateView.as_view(), name='clas_activo_update'),
	path('clas_activo/eliminar/<int:pk>/', 
		ClasActivoDeleteView.as_view(), name='clas_activo_delete'),
	
	# -- Moneda.
	path('moneda/listar/', 
		MonedaListView.as_view(), name='moneda_list'),
	path('moneda/crear/',
		MonedaCreateView.as_view(), name='moneda_create'),
	path('moneda/editar/<int:pk>/', 
		MonedaUpdateView.as_view(), name='moneda_update'),
	path('moneda/eliminar/<int:pk>/', 
		MonedaDeleteView.as_view(), name='moneda_delete'),
	
	# -- Tipo de Cambio.
	path('tipo_cambio/listar/', 
		TipoCambioListView.as_view(), name='tipo_cambio_list'),
	path('tipo_cambio/crear/',
		TipoCambioCreateView.as_view(), name='tipo_cambio_create'),
	path('tipo_cambio/editar/<int:pk>/', 
		TipoCambioUpdateView.as_view(), name='tipo_cambio_update'),
	path('tipo_cambio/eliminar/<int:pk>/', 
		TipoCambioDeleteView.as_view(), name='tipo_cambio_delete'),
	
	# -- Documento SUNAT.
	path('documento_sunat/listar/', 
		DocumentoSunatListView.as_view(), name='documento_sunat_list'),
	path('documento_sunat/crear/',
		DocumentoSunatCreateView.as_view(), name='documento_sunat_create'),
	path('documento_sunat/editar/<int:pk>/', 
		DocumentoSunatUpdateView.as_view(), name='documento_sunat_update'),
	path('documento_sunat/eliminar/<int:pk>/', 
		DocumentoSunatDeleteView.as_view(), name='documento_sunat_delete'),
	
	# -- Zona.
	path('zona/listar/', 
		ZonaListView.as_view(), name='zona_list'),
	path('zona/crear/',
		ZonaCreateView.as_view(), name='zona_create'),
	path('zona/editar/<int:pk>/', 
		ZonaUpdateView.as_view(), name='zona_update'),
	path('zona/eliminar/<int:pk>/', 
		ZonaDeleteView.as_view(), name='zona_delete'),
	
	# -- Sub Zona.
	path('sub_zona/listar/', 
		SubZonaListView.as_view(), name='sub_zona_list'),
	path('sub_zona/crear/',
		SubZonaCreateView.as_view(), name='sub_zona_create'),
	path('sub_zona/editar/<int:pk>/', 
		SubZonaUpdateView.as_view(), name='sub_zona_update'),
	path('sub_zona/eliminar/<int:pk>/', 
		SubZonaDeleteView.as_view(), name='sub_zona_delete'),
	
	# -- Banco.
	path('banco/listar/', 
		BancoListView.as_view(), name='banco_list'),
	path('banco/crear/',
		BancoCreateView.as_view(), name='banco_create'),
	path('banco/editar/<int:pk>/', 
		BancoUpdateView.as_view(), name='banco_update'),
	path('banco/eliminar/<int:pk>/', 
		BancoDeleteView.as_view(), name='banco_delete'),
	
	# -- Caja Banco.
	path('caja_banco/listar/', 
		CajaBancoListView.as_view(), name='caja_banco_list'),
	path('caja_banco/crear/',
		CajaBancoCreateView.as_view(), name='caja_banco_create'),
	path('caja_banco/editar/<int:pk>/', 
		CajaBancoUpdateView.as_view(), name='caja_banco_update'),
	path('caja_banco/eliminar/<int:pk>/', 
		CajaBancoDeleteView.as_view(), name='caja_banco_delete'),
	
]
