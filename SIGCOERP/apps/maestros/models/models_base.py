from django.db import models
from apps.maestros.models.models_base_gen import ModeloBaseGenerico


# Modelo Unidad - Unidad
class Unidad(ModeloBaseGenerico):
	id_unidad = models.AutoField(primary_key=True)
	nombre_unidad = models.CharField("Nombre Unidad", max_length=20, null=True,
									 blank=True)
	abreviado = models.CharField("Abreviado", max_length=10, null=True,
								 blank=True)
	codigo_sunat = models.CharField("Código Sunat", max_length=4, null=True,
									blank=True)
	equivalente = models.DecimalField("Equivalente", max_digits=18,
									  decimal_places=8, default=1.00000000)
	
	def __str__(self):
		return self.nombre_unidad
	
	class Meta:
		db_table = 'sgc_unidad'
		verbose_name = ('Unidad')
		verbose_name_plural = ('Unidades')
		ordering = ['nombre_unidad']


# Modelo ClasProducto - Familia
class ClasProducto(ModeloBaseGenerico):
	id_clas_producto = models.AutoField(primary_key=True)
	nombre_familia = models.CharField("Nombre Familia", max_length=50,
									  null=True, blank=True)
	cta_compra = models.CharField("Cuenta de Compra", max_length=12, null=True,
								  blank=True)
	cta_venta = models.CharField("Cuenta de Venta", max_length=12, null=True,
								 blank=True)
	nc_compra = models.CharField("NC Compra", max_length=12, null=True,
								 blank=True)
	nc_venta = models.CharField("NC Venta", max_length=12, null=True,
								blank=True)
	nd_compra = models.CharField("ND Compra", max_length=12, null=True,
								 blank=True)
	nd_venta = models.CharField("ND Venta", max_length=12, null=True,
								blank=True)
	
	def __str__(self):
		return self.nombre_familia
	
	class Meta:
		db_table = 'sgc_clas_producto'
		verbose_name = ('Familia')
		verbose_name_plural = ('Familias')
		ordering = ['nombre_familia']


# Modelo ClasProductoDet - Sub Familia
class ClasProductoDet(ModeloBaseGenerico):
	id_subclas_producto = models.AutoField(primary_key=True)
	id_clas_producto = models.ForeignKey(ClasProducto,
										 on_delete=models.PROTECT,
										 null=True, blank=True)
	nombre_sub_familia = models.CharField("Sub Familia", max_length=20,
										  null=True, blank=True)

	def __str__(self):
		return self.nombre_sub_familia

	class Meta:
		db_table = 'sgc_clas_producto_det'
		verbose_name = ('Sub Familia')
		verbose_name_plural = ('Sub Familias')
		ordering = ['nombre_sub_familia']


# Modelo Marca - Marca
class Marca(ModeloBaseGenerico):
	id_marca = models.AutoField(primary_key=True)
	nombre_marca = models.CharField("Marca", max_length=40, null=True,
									blank=True)

	def __str__(self):
		return self.nombre_marca

	class Meta:
		db_table = 'sgc_marca'
		verbose_name = ('Marca')
		verbose_name_plural = ('Marcas')
		ordering = ['nombre_marca']


# Modelo Modelo - Modelo
class Modelo(ModeloBaseGenerico):
	id_modelo = models.AutoField(primary_key=True)
	nombre_modelo = models.CharField("Modelo", max_length=40, null=True,
									 blank=True)

	def __str__(self):
		return self.nombre_modelo

	class Meta:
		db_table = 'sgc_modelo'
		verbose_name = ('Modelo')
		verbose_name_plural = ('Modelos')
		ordering = ['nombre_modelo']


# Modelo Ubicacion - Ubicación
class Ubicacion(ModeloBaseGenerico):
	id_ubicacion = models.AutoField(primary_key=True)
	nombre_ubicacion = models.CharField("Ubicación", max_length=20, null=True,
										blank=True)
	ubicacion_fisica = models.CharField("Ubicación Física", max_length=100,
										null=True, blank=True)

	def __str__(self):
		return self.nombre_ubicacion

	class Meta:
		db_table = 'sgc_ubicacion'
		verbose_name = ('Ubicación')
		verbose_name_plural = ('Ubicaciones')
		ordering = ['nombre_ubicacion']


# Modelo CodigoSunat - Código SUNAT
class CodigoSunat(ModeloBaseGenerico):
	id_codigo_sunat = models.AutoField(primary_key=True)
	codigo_sunat = models.CharField("Código SUNAT", max_length=8, null=True,
									blank=True)
	descripcion_codigo_sunat = models.CharField("Descripción", max_length=80,
												null=True, blank=True)

	def __str__(self):
		return self.codigo_sunat

	class Meta:
		db_table = 'sgc_codigo_sunat'
		verbose_name = ('Código SUNAT')
		verbose_name_plural = ('Códigos SUNAT')
		ordering = ['codigo_sunat']


# Modelo UnidadSunat - Unidad SUNAT
class UnidadSunat(ModeloBaseGenerico):
	id_unidad_sunat = models.AutoField(primary_key=True)
	codigo_unidad_sunat = models.CharField("Código Unidad SUNAT", max_length=3,
										   null=True, blank=True)
	descripcion_unidad_sunat = models.CharField("Descripción", max_length=80,
												null=True, blank=True)

	def __str__(self):
		return self.codigo_unidad_sunat if self.codigo_unidad_sunat else \
			self.descripcion_unidad_sunat

	class Meta:
		db_table = 'sgc_unidad_sunat'
		verbose_name = ('Código Unidad SUNAT')
		verbose_name_plural = ('Códigos Unidad SUNAT')
		ordering = ['codigo_unidad_sunat']


# Modelo Color - Color
class Color(ModeloBaseGenerico):
	id_color = models.AutoField(primary_key=True)
	nombre_color = models.CharField("Color", max_length=40, null=True,
									blank=True)

	def __str__(self):
		return self.nombre_color

	class Meta:
		db_table = 'sgc_color'
		verbose_name = ('Color')
		verbose_name_plural = ('Colores')
		ordering = ['nombre_color']


# Modelo TipoDocumentoIdentidad - Tipo de Documento de Identidad
class TipoDocumentoIdentidad(ModeloBaseGenerico):
	id_tipodoc_identidad = models.AutoField(primary_key=True)
	codigo_tipodoc_identidad = models.CharField("Código Documento Identidad",
												max_length=1, null=True,
												blank=True, unique=True)
	nombre_tipodoc_identidad = models.CharField("Tipo Documento Identidad",
												max_length=40, null=True,
												blank=True)
	longitud = models.SmallIntegerField("Longitud", null=True, blank=True)

	def __str__(self):
		return self.nombre_tipodoc_identidad

	class Meta:
		db_table = 'sgc_tipodoc_identidad'
		verbose_name = ('Tipo Documento Identidad')
		verbose_name_plural = ('Tipos Documento Identidad')
		ordering = ['nombre_tipodoc_identidad']


# Modelo Ubigeo - Ubigeo
class Ubigeo(ModeloBaseGenerico):
	id_ubigeo = models.AutoField(primary_key=True)
	ubigeo = models.CharField("Ubigeo", max_length=6, null=True, blank=True)
	departamento = models.CharField("Departamento", max_length=50, null=True,
									blank=True)
	provincia = models.CharField("Provincia", max_length=50, null=True,
								 blank=True)
	distrito = models.CharField("Distrito", max_length=50, null=True,
								blank=True)
	tipo_ubigeo = models.BooleanField("Tipo de Ubigeo", default=False)

	def __str__(self):
		return self.ubigeo

	class Meta:
		db_table = 'sgc_ubigeo'
		verbose_name = ('Ubigeo')
		verbose_name_plural = ('Ubigeos')
		ordering = ['ubigeo']


# Modelo FormaPago - Forma de Pago
class FormaPago(ModeloBaseGenerico):
	id_forma_pago = models.AutoField(primary_key=True)
	nombre_forma_pago = models.CharField("Forma de Pago", max_length=20,
										 null=True, blank=True)
	codigo_forma_pago = models.CharField("Código Forma de Pago", max_length=2,
										 null=True, blank=True)
	compra = models.BooleanField("Compra", default=False)
	venta = models.BooleanField("Venta", default=False)
	pventa = models.BooleanField("PVenta", default=False)
	otros = models.BooleanField("Otros", default=False)

	def __str__(self):
		return self.nombre_forma_pago

	class Meta:
		db_table = 'sgc_forma_pago'
		verbose_name = ('Forma de Pago')
		verbose_name_plural = ('Formas de Pago')
		ordering = ['nombre_forma_pago']


# Modelo ClasServicio - Familia Servicio
class ClasServicio(ModeloBaseGenerico):
	id_clas_servicio = models.AutoField(primary_key=True)
	nombre_familia_servicio = models.CharField("Nombre Familia Servicio",
											   max_length=50, null=True,
											   blank=True)
	cta_compra = models.CharField("Cuenta de Compra", max_length=12, null=True,
								  blank=True)
	cta_venta = models.CharField("Cuenta de Venta", max_length=12, null=True,
								 blank=True)
	nc_compra = models.CharField("NC Compra", max_length=12, null=True,
								 blank=True)
	nc_venta = models.CharField("NC Venta", max_length=12, null=True,
								blank=True)
	nd_compra = models.CharField("ND Compra", max_length=12, null=True,
								 blank=True)
	nd_venta = models.CharField("ND Venta", max_length=12, null=True,
								blank=True)

	def __str__(self):
		return self.nombre_familia_servicio

	class Meta:
		db_table = 'sgc_clas_servicio'
		verbose_name = ('Familia Servicio')
		verbose_name_plural = ('Familias Servicio')
		ordering = ['nombre_familia_servicio']


# Modelo ClasGasto - Familia Gasto
class ClasGasto(ModeloBaseGenerico):
	id_clas_gasto = models.AutoField(primary_key=True)
	nombre_familia_gasto = models.CharField("Nombre Familia Gasto", max_length=50,
											null=True, blank=True)
	cta_compra = models.CharField("Cuenta de Compra", max_length=12, null=True,
								  blank=True)
	cta_venta = models.CharField("Cuenta de Venta", max_length=12, null=True,
								 blank=True)
	nc_compra = models.CharField("NC Compra", max_length=12, null=True,
								 blank=True)
	nc_venta = models.CharField("NC Venta", max_length=12, null=True,
								blank=True)
	nd_compra = models.CharField("ND Compra", max_length=12, null=True,
								 blank=True)
	nd_venta = models.CharField("ND Venta", max_length=12, null=True,
								blank=True)

	def __str__(self):
		return self.nombre_familia_gasto

	class Meta:
		db_table = 'sgc_clas_gasto'
		verbose_name = ('Familia Gasto')
		verbose_name_plural = ('Familias Gasto')
		ordering = ['nombre_familia_gasto']


# Modelo ClasInsumo - Familia Insumo
class ClasInsumo(ModeloBaseGenerico):
	id_clas_insumo = models.AutoField(primary_key=True)
	nombre_familia_insumo = models.CharField("Nombre Familia Insumo", max_length=50,
											 null=True, blank=True)
	cta_compra = models.CharField("Cuenta de Compra", max_length=12, null=True,
								  blank=True)
	cta_venta = models.CharField("Cuenta de Venta", max_length=12, null=True,
								 blank=True)
	nc_compra = models.CharField("NC Compra", max_length=12, null=True,
								 blank=True)
	nc_venta = models.CharField("NC Venta", max_length=12, null=True,
								blank=True)
	nd_compra = models.CharField("ND Compra", max_length=12, null=True,
								 blank=True)
	nd_venta = models.CharField("ND Venta", max_length=12, null=True,
								blank=True)

	def __str__(self):
		return self.nombre_familia_insumo

	class Meta:
		db_table = 'sgc_clas_insumo'
		verbose_name = ('Familia Insumo')
		verbose_name_plural = ('Familias Insumo')
		ordering = ['nombre_familia_insumo']


# Modelo ClasActivo - Familia Activo
class ClasActivo(ModeloBaseGenerico):
	id_clas_activo = models.AutoField(primary_key=True)
	nombre_familia_activo = models.CharField("Nombre Familia Activo", max_length=50,
											 null=True, blank=True)
	cta_compra = models.CharField("Cuenta de Compra", max_length=12, null=True,
								  blank=True)
	cta_venta = models.CharField("Cuenta de Venta", max_length=12, null=True,
								 blank=True)
	nc_compra = models.CharField("NC Compra", max_length=12, null=True,
								 blank=True)
	nc_venta = models.CharField("NC Venta", max_length=12, null=True,
								blank=True)
	nd_compra = models.CharField("ND Compra", max_length=12, null=True,
								 blank=True)
	nd_venta = models.CharField("ND Venta", max_length=12, null=True,
								blank=True)

	def __str__(self):
		return self.nombre_familia_activo

	class Meta:
		db_table = 'sgc_clas_activo'
		verbose_name = ('Familia Activo')
		verbose_name_plural = ('Familias Activo')
		ordering = ['nombre_familia_activo']


# Modelo Moneda - Moneda
class Moneda(ModeloBaseGenerico):
	id_moneda = models.AutoField(primary_key=True)
	nombre_moneda = models.CharField("Nombre Moneda", max_length=20,
									 null=True, blank=True)
	simbolo_moneda = models.CharField("Símbolo Moneda", max_length=5,
									  null=True, blank=True)
	descripcion_moneda = models.CharField("Descripción", max_length=50,
										  null=True, blank=True)

	def __str__(self):
		return self.nombre_moneda

	class Meta:
		db_table = 'sgc_moneda'
		verbose_name = ('Moneda')
		verbose_name_plural = ('Monedas')
		ordering = ['nombre_moneda']


# Modelo TipoCambio - Tipo de Cambio
class TipoCambio(ModeloBaseGenerico):
	id_tipo_cambio = models.AutoField(primary_key=True)
	id_moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT,
								  null=True, blank=True)
	fecha_cambio = models.DateField(null=True, blank=True)
	tasa_compra = models.DecimalField(max_digits=14, decimal_places=3,
									  null=True, blank=True)
	tasa_venta = models.DecimalField(max_digits=14, decimal_places=3,
									 null=True, blank=True)

	def __str__(self):
		if self.id_moneda:
			return f"{self.id_moneda.nombre_moneda} - {self.fecha_cambio}"
		else:
			return f"Sin Moneda - {self.fecha_cambio}"

	class Meta:
		db_table = 'sgc_tipo_cambio'
		verbose_name = ('Tipo de Cambio')
		verbose_name_plural = ('Tipos de Cambio')
		ordering = ['fecha_cambio', 'id_moneda__nombre_moneda']


# Modelo DocumentoSunat - Documento Sunat
class DocumentoSunat(ModeloBaseGenerico):
	id_documento_sunat = models.AutoField(primary_key=True)
	nombre_documento_sunat = models.CharField("Documento SUNAT",
											  max_length=200, null=True,
											  blank=True)
	abreviado = models.CharField("Abreviado", max_length=10, null=True,
								 blank=True)
	compra = models.BooleanField("Compra", default=False)
	venta = models.BooleanField("Venta", default=False)
	gasto = models.BooleanField("Gasto", default=False)
	honorario = models.BooleanField("Honorario", default=False)
	guia = models.BooleanField("Guía", default=False)
	nc = models.BooleanField("NC", default=False)
	nd = models.BooleanField("ND", default=False)
	percepcion = models.BooleanField("Percepción", default=False)
	retencion = models.BooleanField("Retención", default=False)
	otros = models.BooleanField("Otros", default=False)

	def __str__(self):
		return self.nombre_documento_sunat

	class Meta:
		db_table = 'sgc_documento_sunat'
		verbose_name = ('Documento SUNAT')
		verbose_name_plural = ('Documentos SUNAT')
		ordering = ['nombre_documento_sunat']


# Modelo Zona - Zona
class Zona(ModeloBaseGenerico):
	id_zona = models.AutoField(primary_key=True)
	nombre_zona = models.CharField("Nombre Zona", max_length=50, null=True,
								   blank=True)
	descripcion_zona = models.CharField("Descripción Zona", max_length=80, null=True,
										blank=True)

	def __str__(self):
		return self.nombre_zona

	class Meta:
		db_table = 'sgc_zona'
		verbose_name = ('Zona')
		verbose_name_plural = ('Zonas')
		ordering = ['nombre_zona']


# Modelo SubZona - Sub Zona
class SubZona(ModeloBaseGenerico):
	id_sub_zona = models.AutoField(primary_key=True)
	id_zona = models.ForeignKey(Zona, on_delete=models.PROTECT, null=True,
								blank=True)
	nombre_sub_zona = models.CharField("Sub Zona", max_length=20,
									   null=True, blank=True)
	descripcion_sub_zona = models.CharField("Descripción Zona", max_length=80,
											null=True, blank=True)

	def __str__(self):
		return self.nombre_sub_zona

	class Meta:
		db_table = 'sgc_sub_zona'
		verbose_name = ('Sub Zona')
		verbose_name_plural = ('Sub Zonas')
		ordering = ['nombre_sub_zona']


# Modelo Banco - Banco
class Banco(ModeloBaseGenerico):
	id_banco = models.AutoField(primary_key=True)
	codigo_banco = models.CharField("Código Banco", max_length=4, null=True,
									blank=True)
	nombre_banco = models.CharField("Nombre Banco", max_length=50, null=True,
									blank=True)
	descripcion_banco = models.CharField("Descripción Banco", max_length=80,
										 null=True, blank=True)

	def __str__(self):
		return f"{self.codigo_banco} - {self.nombre_banco}"

	class Meta:
		db_table = 'sgc_banco'
		verbose_name = ('Banco')
		verbose_name_plural = ('Bancos')
		ordering = ['nombre_banco']


# Modelo CajaBanco - Caja Bancos
class CajaBanco(ModeloBaseGenerico):
	id_caja_banco = models.AutoField(primary_key=True)
	id_banco = models.ForeignKey(Banco, on_delete=models.PROTECT, null=True,
								 blank=True, verbose_name="Banco")
	nombre_caja_banco = models.CharField("Nombre Caja o Banco", max_length=100,
										 null=True, blank=True)
	tipo_caja_banco = models.SmallIntegerField(choices=((1, 'Caja'),
														(2, 'Banco')))
	cuenta_caja_banco = models.CharField("Nro de Cuenta", max_length=20,
										 null=True, blank=True)
	cuentacci_caja_banco = models.CharField("No CCI de Cuenta", max_length=20,
											null=True, blank=True)
	id_moneda = models.ForeignKey(Moneda, on_delete=models.PROTECT, null=True,
								  blank=True, verbose_name="Moneda")
	estatus_caja_banco = models.SmallIntegerField(choices=((1, 'Activo'),
														   (2, 'Inactivo')))

	def __str__(self):
		return self.nombre_caja_banco

	class Meta:
		db_table = 'sgc_caja_banco'
		verbose_name = ('Caja Banco')
		verbose_name_plural = ('Caja Bancos')
		ordering = ['nombre_caja_banco']


# Modelo Pais - Pais
class Pais(ModeloBaseGenerico):
	CONTINENTES = (
		("América", "América"),
		("Europa", "Europa"),
		("Asia", "Asía"),
		("África", "África"),
		("Oceanía", "Oceanía"),
		("Antártida", "Antártida"),
		("", "Seleccione una opción"))

	id_pais = models.AutoField(primary_key=True)
	nombre_pais = models.CharField("Pais", max_length=100, null=True,
								   blank=True)
	nombre_pais_ingles = models.CharField("Country", max_length=100, null=True,
										  blank=True)
	nombre_pais_frances = models.CharField("Pays", max_length=100, null=True,
										   blank=True)
	continente = models.CharField("Continente", max_length=15,
								  choices=CONTINENTES, default="América")
	codigo_telefonico = models.SmallIntegerField("Código Telefónico",
												 null=True, blank=True)
	codigo_iso2 = models.CharField("Código ISO2", max_length=2, null=True,
								   blank=True)
	codigo_iso3 = models.CharField("Código ISO3", max_length=3, null=True,
								   blank=True)

	def __str__(self):
		return f"{self.nombre_pais} - {self.codigo_telefonico}"

	class Meta:
		db_table = 'sgc_pais'
		verbose_name = ('País')
		verbose_name_plural = ('Paises')
		ordering = ['nombre_pais']


# Modelo PersonaCargo - Persona Cargo
class PersonaCargo(ModeloBaseGenerico):
	id_persona_cargo = models.AutoField(primary_key=True)
	nombre_cargo = models.CharField("Cargo", max_length=50, null=True,
									blank=True)

	def __str__(self):
		return self.nombre_cargo

	class Meta:
		db_table = 'sgc_persona_cargo'
		verbose_name = ('Persona Cargo')
		verbose_name_plural = ('Personas Cargo')
		ordering = ['nombre_cargo']


# Modelo AgendaRubro - Agenda Rubro
class AgendaRubro(ModeloBaseGenerico):
	id_agenda_rubro = models.AutoField(primary_key=True)
	nombre_agenda_rubro = models.CharField("Rubro", max_length=50, null=True,
										   blank=True)
	comision_venta = models.DecimalField(max_digits=18, decimal_places=2,
										 null=True, blank=True)

	def __str__(self):
		return self.nombre_agenda_rubro

	class Meta:
		db_table = 'sgc_agenda_rubro'
		verbose_name = ('Agenda Rubro')
		verbose_name_plural = ('Agendas Rubro')
		ordering = ["nombre_agenda_rubro"]
