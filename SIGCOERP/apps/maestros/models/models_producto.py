from django.db import models
from apps.maestros.models.models_base_gen import ModeloBaseGenerico
from apps.maestros.models.models_base import *
from apps.maestros.models.models_agenda import *


class Producto(ModeloBaseGenerico):
	id_producto = models.AutoField(primary_key=True)
	estatus_producto = models.BooleanField("Activo", default=True)
	codigo_producto = models.CharField(max_length=20, null=True, blank=True)
	nombre_producto = models.CharField(max_length=100, null=True, blank=True)
	id_unidad = models.ForeignKey(Unidad, on_delete=models.PROTECT, null=True,
								  blank=True, verbose_name="Unidad")
	id_clas_producto = models.ForeignKey(ClasProducto,
										 on_delete=models.PROTECT,
										 null=True, blank=True,
										 verbose_name='Familia')
	id_subclas_producto = models.ForeignKey(ClasProductoDet,
											on_delete=models.PROTECT,
											null=True, blank=True,
											verbose_name='Sub Familia')
	id_marca = models.ForeignKey(Marca, on_delete=models.PROTECT, null=True,
								 blank=True, verbose_name='Marca')
	id_modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, null=True,
								  blank=True, verbose_name='Modelo')
	id_ubicacion = models.ForeignKey(Ubicacion, on_delete=models.PROTECT,
									 null=True, blank=True,
									 verbose_name='Ubicación')
	id_codigo_sunat = models.ForeignKey(CodigoSunat, on_delete=models.PROTECT,
										null=True, blank=True,
										verbose_name='Código SUNAT')
	id_unidad_sunat = models.ForeignKey(UnidadSunat, on_delete=models.PROTECT,
										null=True, blank=True,
										verbose_name='Unidad SUNAT')
	id_color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True,
								 blank=True, verbose_name='Color')
	stock_minimo = models.DecimalField("Stock Mínimo", max_digits=18,
									   decimal_places=2, null=True, blank=True)
	stock_maximo = models.DecimalField("Stock Máximo", max_digits=18,
									   decimal_places=2, null=True, blank=True)
	precio_promedio = models.DecimalField("Precio Promedio", max_digits=18,
										  decimal_places=2, null=True, blank=True)
	comision_venta = models.DecimalField(max_digits=18, decimal_places=2,
										 null=True, blank=True)
	bonificacion_tf = models.BooleanField(default=False)
	ventasoles_tf = models.BooleanField(default=False)
	balanza_tf = models.BooleanField(default=False)
	icbper_tf = models.BooleanField(default=False)
	exonerado_tf = models.BooleanField(default=False)
	muevekardex_tf = models.BooleanField(default=False)
	controlastock_tf = models.BooleanField(default=False)
	combo_producto_tf = models.BooleanField(default=False)
	id_proveedor = models.ForeignKey(Agenda, on_delete=models.PROTECT,
									 null=True, blank=True,
									 verbose_name='Proveedor')
	descuento = models.DecimalField("Descuento", max_digits=18,
									decimal_places=2, null=True, blank=True)
	ruta_imagen_producto = models.CharField("Ruta Imagen", max_length=100,
											null=True, blank=True)
	detalle_producto = models.TextField("Detalle del Producto", null=True,
										blank=True)

	def __str__(self):
		return self.nombre_producto

	class Meta:
		db_table = 'sgc_catalogo_producto'
