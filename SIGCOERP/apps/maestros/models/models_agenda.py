from django.db import models
from apps.maestros.models.models_base_gen import ModeloBaseGenerico
from apps.maestros.models.models_base import *
from apps.maestros.models.models_persona import Persona


class Agenda(ModeloBaseGenerico):
    PROCEDENCIA_CHOICES = (
        ("Local", "Local"),
        ("Nacional", "Nacional"),
        ("Importación", "Importación"),
        ("", "Seleccione una opción"))

    id_agenda = models.AutoField(primary_key=True)
    estatus_agenda = models.BooleanField("Activo", default=True)
    codigo_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad,
                                                 on_delete=models.RESTRICT,
                                                 null=True,
                                                 blank=True,
                                                 verbose_name="Tipo de Documento",
                                                 to_field='codigo_tipodoc_identidad')
    nro_doc_identidad = models.CharField("Documento Identidad", max_length=15,
                                         null=True, blank=True)
    nombre_agenda = models.CharField("Nombre Agenda", max_length=100,
                                     null=True, blank=True)
    nombres_agenda = models.CharField("Nombres", max_length=100,
                                      null=True, blank=True)
    apellidos_agenda = models.CharField("Apellidos", max_length=100,
                                        null=True, blank=True)
    procedencia = models.CharField("Procedencia", max_length=15,
                                   choices=PROCEDENCIA_CHOICES,
                                   default="Local")
    cliente_tf = models.BooleanField("Cliente", default=False)
    proveedor_tf = models.BooleanField("Proveedor", default=False)
    personal_tf = models.BooleanField("Personal", default=False)
    transporte_tf = models.BooleanField("Transporte", default=False)
    laboratorio_tf = models.BooleanField("Laboratorio", default=False)
    direccion = models.CharField("Direccion", max_length=100,
                                 null=True, blank=True)
    localidad = models.CharField("Localidad", max_length=100,
                                 null=True, blank=True)
    id_ubigeo = models.ForeignKey(Ubigeo, on_delete=models.PROTECT,
                                  null=True, blank=True)
    referencia = models.CharField("Referencia", max_length=200, null=True,
                                  blank=True)
    id_pais_t1 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                   blank=True, related_name="telefonos_t1",
                                   verbose_name="Código País")
    telefono1 = models.CharField("Teléfono 1", max_length=12, null=True,
                                 blank=True)
    id_pais_t2 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                   blank=True, related_name="telefonos_t2",
                                   verbose_name="Código País")
    telefono2 = models.CharField("Teléfono 2", max_length=12, null=True,
                                 blank=True)
    id_pais_c1 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                   blank=True, related_name="telefonos_c1",
                                   verbose_name="Código País")
    celular1 = models.CharField("Celular 1", max_length=12, null=True,
                                blank=True)
    id_pais_c2 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                   blank=True, related_name="telefonos_c2",
                                   verbose_name="Código País")
    celular2 = models.CharField("Celular 2", max_length=12, null=True,
                                blank=True)
    email_1 = models.CharField("e-MAIL 1", max_length=100, null=True,
                               blank=True)
    email_2 = models.CharField("e-MAIL 2", max_length=100, null=True,
                               blank=True)
    nombre_contacto1 = models.CharField("Nombre Contacto 1", max_length=100,
                                        null=True, blank=True)
    cargo_contacto1 = models.CharField("Cargo Contacto 1", max_length=100,
                                       null=True, blank=True)
    id_pais_tc1 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                    blank=True, related_name="telefonos_tc1",
                                    verbose_name="Código País")
    telef_contacto1 = models.CharField("Teléfono Contacto 1", max_length=12,
                                       null=True, blank=True)
    nombre_contacto2 = models.CharField("Nombre Contacto 2", max_length=100,
                                        null=True, blank=True)
    cargo_contacto2 = models.CharField("Cargo Contacto 2", max_length=100,
                                       null=True, blank=True)
    id_pais_tc2 = models.ForeignKey(Pais, on_delete=models.PROTECT, null=True,
                                    blank=True, related_name="telefonos_tc2",
                                    verbose_name="Código País")
    telef_contacto2 = models.CharField("Teléfono Contacto 2", max_length=12,
                                       null=True, blank=True)
    observacion_agenda = models.TextField(verbose_name="Observación Agenda",
                                          null=True, blank=True)
    id_forma_pago = models.ForeignKey(FormaPago, on_delete=models.PROTECT,
                                      null=True, blank=True,
                                      verbose_name="Forma de Pago")
    limite_credito = models.DecimalField(max_digits=18, decimal_places=2,
                                         null=True, blank=True)
    dias_credito = models.SmallIntegerField("Días de Crédito", null=True,
                                            blank=True)
    deuda = models.DecimalField(max_digits=18, decimal_places=2, null=True,
                                blank=True)
    descuento = models.DecimalField(max_digits=18, decimal_places=2, null=True,
                                    blank=True)
    id_vendedor = models.ForeignKey(Persona, on_delete=models.PROTECT,
                                    null=True, blank=True,
                                    verbose_name="Vendedor")
    id_agenda_rubro = models.ForeignKey(AgendaRubro, on_delete=models.PROTECT,
                                        null=True, blank=True,
                                        verbose_name="Rubro")
    id_zona = models.ForeignKey(Zona, on_delete=models.PROTECT, null=True,
                                blank=True, verbose_name="Zona")

    def __str__(self):
        return self.nombre_agenda

    class Meta:
        db_table = 'sgc_agenda'

# Modelo AgendaChofer - Agenda Chofer


class AgendaChofer(ModeloBaseGenerico):
    id_agenda_chofer = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT, null=True,
                                  blank=True, verbose_name="Transporte",
                                  limit_choices_to={'transporte_tf': True})
    id_tipodoc_identidad = models.ForeignKey(TipoDocumentoIdentidad,
                                             on_delete=models.RESTRICT,
                                             null=True, blank=True,
                                             verbose_name="Tipo de Documento")
    nro_doc_identidad = models.CharField("Documento Identidad", max_length=15,
                                         null=True, blank=True)
    apellidos_chofer = models.CharField("Apellidos", max_length=100, null=True,
                                        blank=True)
    nombres_chofer = models.CharField("Nombres", max_length=100, null=True,
                                      blank=True)
    licencia_chofer = models.CharField("Licencia", max_length=20, null=True,
                                       blank=True)
    placa_vehiculo = models.CharField("Placa", max_length=20, null=True,
                                      blank=True)
    observaciones_chofer = models.CharField("Observaciones", max_length=200,
                                            null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_apellidos_chofer} - {self.nombre_nombres_chofer}"

    class Meta:
        db_table = 'sgc_agenda_chofer'
        verbose_name = ('Agenda Chofer')
        verbose_name_plural = ('Agendas Chofer')
        ordering = ["apellidos_chofer", "nombres_chofer"]
