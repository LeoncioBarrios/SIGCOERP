from django.contrib import admin
from .models.models_base import *
from .models.models_producto import Producto
from .models.models_persona import Persona
from .models.models_agenda import Agenda, AgendaChofer

# admin.site.register(Unidad)


# Modelo Unidad - Unidad
@admin.register(Unidad)
class UnidadAdmin(admin.ModelAdmin):
	# Lista de campos a visualizar para la edición
	fields = ["nombre_unidad", "abreviado", "codigo_sunat",
			  "equivalente", "usuario", "estacion", "fcontrol"]
	# Lista de campos en edición de solo lectura
	readonly_fields = ("usuario", "estacion", "fcontrol")
	# Lista de campos en el listado de la tabla
	list_display = ("nombre_unidad", "abreviado", "codigo_sunat",
					"equivalente")
	# Lista de campos para filtros de la tabla
	list_filter = ("nombre_unidad", "abreviado", "codigo_sunat")
	# Lista de campos para la búsqueda de registros
	search_fields = ("nombre_unidad", "abreviado", "codigo_sunat")


# Modelo ClasProducto - Familia
@admin.register(ClasProducto)
class ClasProductoAdmin(admin.ModelAdmin):
	fields = ["nombre_familia", "cta_compra", "cta_venta",
			  "nc_compra", "nc_venta", "nd_compra", "nd_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_familia", "cta_compra", "cta_venta",
					"nc_compra", "nc_venta", "nd_compra", "nd_venta")
	list_filter = ("nombre_familia", "cta_compra", "cta_venta")
	search_fields = ("nombre_familia", "cta_compra", "cta_venta")


# Modelo ClasProductoDet - Sub Familia
@admin.register(ClasProductoDet)
class ClasProductoDetAdmin(admin.ModelAdmin):
	fields = ["id_clas_producto", "nombre_sub_familia",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("get_familia", "nombre_sub_familia")
	list_filter = ("id_clas_producto__nombre_familia", "nombre_sub_familia")
	search_fields = ("id_clas_producto__nombre_familia", "nombre_sub_familia")

	def get_familia(self, obj):
		return obj.id_clas_producto.nombre_familia if obj.id_clas_producto else ""

	get_familia.short_description = "Familia"


# Modelo Marca - Marca
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
	fields = ["nombre_marca", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_marca",)
	list_filter = ("nombre_marca",)
	search_fields = ("nombre_marca",)


# Modelo Modelo - Modelo
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
	fields = ["nombre_modelo", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_modelo",)
	list_filter = ("nombre_modelo",)
	search_fields = ("nombre_modelo",)


# Modelo Ubicacion - Ubicación
@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
	fields = ["nombre_ubicacion", "ubicacion_fisica",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_ubicacion", "ubicacion_fisica")
	list_filter = ("nombre_ubicacion", )
	search_fields = ("nombre_ubicacion", )


# Modelo CodigoSunat - Código SUNAT
@admin.register(CodigoSunat)
class CodigoSunatAdmin(admin.ModelAdmin):
	fields = ["codigo_sunat", "descripcion_codigo_sunat",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("codigo_sunat", "descripcion_codigo_sunat")
	list_filter = ("codigo_sunat",)
	search_fields = ("codigo_sunat",)


# Modelo UnidadSunat - Unidad SUNAT
@admin.register(UnidadSunat)
class UnidadSunatAdmin(admin.ModelAdmin):
	fields = ["codigo_unidad_sunat", "descripcion_unidad_sunat",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("codigo_unidad_sunat", "descripcion_unidad_sunat")
	list_filter = ("codigo_unidad_sunat", "descripcion_unidad_sunat")
	search_fields = ("codigo_unidad_sunat", "descripcion_unidad_sunat")


# Modelo Color - Color
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
	fields = ["nombre_color", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_color",)
	list_filter = ("nombre_color",)
	search_fields = ("nombre_color",)


# Modelo TipoDocumentoIdentidad - Tipo de Documento de Identidad
@admin.register(TipoDocumentoIdentidad)
class TipoDocumentoIdentidadAdmin(admin.ModelAdmin):
	fields = ["nombre_tipodoc_identidad", "codigo_tipodoc_identidad",
			  "longitud", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_tipodoc_identidad", "codigo_tipodoc_identidad",
					"longitud")
	list_filter = ("nombre_tipodoc_identidad",)
	search_fields = ("nombre_tipodoc_identidad",)


# Modelo Ubigeo - Ubigeo
@admin.register(Ubigeo)
class UbigeoAdmin(admin.ModelAdmin):
	fields = ["ubigeo", "departamento", "provincia", "distrito",
			  "tipo_ubigeo", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("ubigeo", "departamento", "provincia", "distrito",
					"tipo_ubigeo")
	list_filter = ("ubigeo", "departamento", "provincia", "distrito")
	search_fields = ("ubigeo", "departamento", "provincia", "distrito")


# Modelo FormaPago - Forma de Pago
@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
	fields = ['nombre_forma_pago', 'codigo_forma_pago',
			  'compra', 'venta', 'pventa', 'otros',
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ('id_forma_pago', 'nombre_forma_pago', 'codigo_forma_pago',
					'compra', 'venta', 'pventa', 'otros')
	list_filter = ('compra', 'venta', 'pventa', 'otros')
	search_fields = ('nombre_forma_pago', 'codigo_forma_pago')


# Modelo ClasServicio - Familia Servicio
@admin.register(ClasServicio)
class ClasServicioAdmin(admin.ModelAdmin):
	fields = ["nombre_familia_servicio", "cta_compra", "cta_venta",
			  "nc_compra", "nc_venta", "nd_compra", "nd_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_familia_servicio", "cta_compra", "cta_venta",
					"nc_compra", "nc_venta", "nd_compra", "nd_venta")
	list_filter = ("nombre_familia_servicio", "cta_compra", "cta_venta")
	search_fields = ("nombre_familia_servicio", "cta_compra", "cta_venta")


# Modelo ClasGasto - Familia Gasto
@admin.register(ClasGasto)
class ClasGastoAdmin(admin.ModelAdmin):
	fields = ["nombre_familia_gasto", "cta_compra", "cta_venta",
			  "nc_compra", "nc_venta", "nd_compra", "nd_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_familia_gasto", "cta_compra", "cta_venta",
					"nc_compra", "nc_venta", "nd_compra", "nd_venta")
	list_filter = ("nombre_familia_gasto", "cta_compra", "cta_venta")
	search_fields = ("nombre_familia_gasto", "cta_compra", "cta_venta")


# Modelo ClasInsumo - Familia Insumo
@admin.register(ClasInsumo)
class ClasInsumoAdmin(admin.ModelAdmin):
	fields = ["nombre_familia_insumo", "cta_compra", "cta_venta",
			  "nc_compra", "nc_venta", "nd_compra", "nd_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_familia_insumo", "cta_compra", "cta_venta",
					"nc_compra", "nc_venta", "nd_compra", "nd_venta")
	list_filter = ("nombre_familia_insumo", "cta_compra", "cta_venta")
	search_fields = ("nombre_familia_insumo", "cta_compra", "cta_venta")


# Modelo ClasActivo - Familia Activo
@admin.register(ClasActivo)
class ClasActivoAdmin(admin.ModelAdmin):
	fields = ["nombre_familia_activo", "cta_compra", "cta_venta",
			  "nc_compra", "nc_venta", "nd_compra", "nd_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_familia_activo", "cta_compra", "cta_venta",
					"nc_compra", "nc_venta", "nd_compra", "nd_venta")
	list_filter = ("nombre_familia_activo", "cta_compra", "cta_venta")
	search_fields = ("nombre_familia_activo", "cta_compra", "cta_venta")


# Modelo Moneda - Moneda
@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
	fields = ["nombre_moneda", "simbolo_moneda", "descripcion_moneda",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_moneda", "simbolo_moneda", "descripcion_moneda")
	list_filter = ("nombre_moneda", "simbolo_moneda", "descripcion_moneda")
	search_fields = ("nombre_moneda", "simbolo_moneda", "descripcion_moneda")


# Modelo TipoCambio - Tipo Cambio
@admin.register(TipoCambio)
class TipoCambioAdmin(admin.ModelAdmin):
	fields = ["id_moneda", "fecha_cambio", "tasa_compra", "tasa_venta",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_moneda", "fecha_cambio", "tasa_compra",
					"tasa_venta")
	list_filter = ("id_moneda__nombre_moneda", "fecha_cambio", "tasa_compra",
				   "tasa_venta")
	search_fields = ("id_moneda__nombre_moneda",)

	def nombre_moneda(self, obj):
		return obj.id_moneda.nombre_moneda if obj.id_moneda else "Sin Moneda"

	nombre_moneda.short_description = "Moneda"


# Modelo DocumentoSunat - Documento Sunat
@admin.register(DocumentoSunat)
class DocumentoSunatAdmin(admin.ModelAdmin):
	fields = ["nombre_documento_sunat", "abreviado", "compra", "venta",
			  "gasto", "honorario", "guia", "nc", "nd", "percepcion",
			  "retencion", "otros", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_documento_sunat", "abreviado")
	list_filter = ("nombre_documento_sunat", "abreviado")
	search_fields = ("nombre_documento_sunat", "abreviado")


# Modelo Zona - Zona
@admin.register(Zona)
class ZonaAdmin(admin.ModelAdmin):
	fields = ["nombre_zona", "descripcion_zona", "usuario", "estacion",
			  "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_zona", "descripcion_zona")
	list_filter = ("nombre_zona", "descripcion_zona")
	search_fields = ("nombre_zona", "descripcion_zona")


# Modelo SubZona - Sub Zona
@admin.register(SubZona)
class SubZonaAdmin(admin.ModelAdmin):
	fields = ["id_zona", "nombre_sub_zona", "descripcion_sub_zona",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("get_zona", "nombre_sub_zona")
	list_filter = ("id_zona__nombre_zona", "nombre_sub_zona")
	search_fields = ("id_zona__nombre_zona", "nombre_sub_zona")

	def get_zona(self, obj):
		return obj.id_zona.nombre_zona if obj.id_zona else ""

	get_zona.short_description = "Zona"


# Modelo Banco - Banco
@admin.register(Banco)
class ZonaAdmin(admin.ModelAdmin):
	fields = ["codigo_banco", "nombre_banco", "descripcion_banco",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("codigo_banco", "nombre_banco", "descripcion_banco")
	list_filter = ("codigo_banco", "nombre_banco")
	search_fields = ("codigo_banco", "nombre_banco")


# Modelo CajaBanco - Caja Banco
@admin.register(CajaBanco)
class CajaBancoAdmin(admin.ModelAdmin):
	fields = ["id_banco", "nombre_caja_banco", "tipo_caja_banco",
			  "cuenta_caja_banco", "cuentacci_caja_banco", "id_moneda",
			  "estatus_caja_banco", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("get_banco", "nombre_caja_banco", "tipo_caja_banco",
					"cuenta_caja_banco", "get_moneda")
	list_filter = ("id_banco__nombre_banco", "cuenta_caja_banco")
	search_fields = ("id_banco__nombre_banco", "cuenta_caja_banco")

	def get_banco(self, obj):
		return obj.id_banco.nombre_banco if obj.id_banco else ""

	def get_moneda(self, obj):
		return obj.id_moneda.nombre_moneda if obj.id_moneda else ""

	get_banco.short_description = "Banco"
	get_moneda.short_description = "Moneda"


# Modelo Producto - Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
	fields = ["codigo_producto", "estatus_producto", "nombre_producto",
			  "id_unidad", "id_clas_producto", "id_subclas_producto",
			  "id_marca", "id_modelo", "id_ubicacion", "id_codigo_sunat",
			  "id_unidad_sunat", "id_color", "stock_minimo", "stock_maximo",
			  "precio_promedio", "comision_venta", "bonificacion_tf",
			  "ventasoles_tf", "balanza_tf", "icbper_tf", "exonerado_tf",
			  "muevekardex_tf", "controlastock_tf", "combo_producto_tf",
			  "id_proveedor", "descuento", "ruta_imagen_producto",
			  "detalle_producto",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("codigo_producto", "estatus_producto", "nombre_producto",
					"id_unidad", "usuario", "estacion", "fcontrol")
	list_filter = ("codigo_producto", "nombre_producto")
	search_fields = ("codigo_producto", "nombre_producto")


# Modelo País - País
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	fields = ["nombre_pais", "nombre_pais_ingles", "nombre_pais_frances",
			  "continente", "codigo_telefonico", "codigo_iso2", "codigo_iso3",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_pais", "nombre_pais_ingles", "continente",
					"codigo_telefonico", "codigo_iso2", "codigo_iso3")
	list_filter = ("nombre_pais", "continente")
	search_fields = ("nombre_pais", "continente")


# Modelo AgendaRubro - Agenda Rubro
@admin.register(AgendaRubro)
class AgendaRubroAdmin(admin.ModelAdmin):
	fields = ["nombre_agenda_rubro", "comision_venta", "usuario",
			  "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_agenda_rubro", "comision_venta")
	list_filter = ("nombre_agenda_rubro",)
	search_fields = ("nombre_agenda_rubro",)


# Modelo Agenda - Agenda
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
	fields = ["estatus_agenda", "codigo_tipodoc_identidad", "nro_doc_identidad",
			  "nombre_agenda", "nombres_agenda", "apellidos_agenda",
			  "procedencia", "cliente_tf", "proveedor_tf", "personal_tf",
			  "transporte_tf", "laboratorio_tf", "direccion", "localidad",
			  "id_ubigeo", "referencia", "id_pais_t1", "telefono1",
			  "id_pais_t2", "telefono2", "id_pais_c1", "celular1",
			  "id_pais_c2", "celular2", "email_1", "email_2",
			  "nombre_contacto1", "cargo_contacto1", "id_pais_tc1",
			  "telef_contacto1", "nombre_contacto2", "cargo_contacto2",
			  "id_pais_tc2", "telef_contacto2", "observacion_agenda",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("codigo_tipodoc_identidad", "nro_doc_identidad",
					"nombre_agenda", "procedencia")
	list_filter = ("nro_doc_identidad", "nombre_agenda")
	search_fields = ("nro_doc_identidad", "nombre_agenda")


# Modelo AgendaChofer - Agenda Chofer
@admin.register(AgendaChofer)
class AgendaChoferAdmin(admin.ModelAdmin):
	fields = ["id_agenda", "id_tipodoc_identidad", "nro_doc_identidad",
			  "apellidos_chofer", "nombres_chofer", "licencia_chofer",
			  "placa_vehiculo", "observaciones_chofer", "usuario",
			  "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("apellidos_chofer", "nombres_chofer", "licencia_chofer",
					"placa_vehiculo")
	list_filter = ("apellidos_chofer", "nombres_chofer")
	search_fields = ("apellidos_chofer", "nombres_chofer")


# Modelo PersonaCargo - Persona Cargo
@admin.register(PersonaCargo)
class PersonaCargoAdmin(admin.ModelAdmin):
	fields = ["nombre_cargo", "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nombre_cargo",)
	list_filter = ("nombre_cargo",)
	search_fields = ("nombre_cargo",)


# Modelo Persona - Persona
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	fields = ["estatus_persona", "id_tipodoc_identidad", "nro_doc_identidad",
			  "nombre_persona", "direccion_persona", "id_pais_t",
			  "telefono_persona", "email_persona", "fecha_ingreso",
			  "fecha_cese", "observacion_persona", "comision_factura",
			  "comision_prod_tf", "id_persona_cargo", "tipo_precio",
			  "usuario", "estacion", "fcontrol"]
	readonly_fields = ("usuario", "estacion", "fcontrol")
	list_display = ("nro_doc_identidad", "nombre_persona", "estatus_persona", )
	list_filter = ("id_tipodoc_identidad", "nro_doc_identidad",
				   "nombre_persona", "estatus_persona",)
	search_fields = ("nro_doc_identidad", "nombre_persona",)
