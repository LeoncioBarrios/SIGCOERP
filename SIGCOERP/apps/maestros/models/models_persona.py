from django.db import models
from apps.maestros.models.models_base_gen import ModeloBaseGenerico
from apps.maestros.models.models_base import *


class Persona(ModeloBaseGenerico):
    TIPOS_PRECIO = (
        ("Todos", "Todos"),
        ("Minorista", "Minorista"),
        ("Mayorista", "Mayorista"),
        ("Cobertura", "Cobertura"),
        ("Mercados", "Mercados"),
        ("", "Seleccione una opción"))

    id_persona = models.AutoField(primary_key=True)
    estatus_persona = models.BooleanField("Activo", default=True)
    id_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad,
                                             on_delete=models.RESTRICT,
                                             null=True, blank=True,
                                             verbose_name="Tipo de Documento")
    nro_doc_identidad = models.CharField("Número Documento Identidad",
                                         max_length=15, null=True,
                                         blank=True)
    nombre_persona = models.CharField("Nombre", max_length=100, null=True,
                                      blank=True)
    direccion_persona = models.CharField("Dirección", max_length=100,
                                         null=True, blank=True)
    id_pais_t = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                  blank=True)
    telefono_persona = models.CharField("Teléfono", max_length=12, null=True,
                                        blank=True)
    email_persona = models.CharField("e-MAIL", max_length=100, null=True,
                                     blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_cese = models.DateField(null=True, blank=True)
    observacion_persona = models.TextField(verbose_name="Observación Persona",
                                           null=True, blank=True)
    comision_factura = models.DecimalField(max_digits=5, decimal_places=2)
    comision_prod_tf = models.BooleanField("% Comisión Venta", default=False)
    id_persona_cargo = models.ForeignKey(PersonaCargo, on_delete=models.PROTECT,
                                         null=True, blank=True)
    tipo_precio = models.CharField("Tipos de Precio", max_length=15,
                                   choices=TIPOS_PRECIO, default="Todos")

    def __str__(self):
        return self.nombre_persona

    class Meta:
        db_table = 'sgc_personal'
