from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import TipoDocumentoIdentidad
from ..forms.tipo_documento_identidad_forms import TipoDocumentoIdentidadForm


modelo = TipoDocumentoIdentidad
modelo_string = "tipo_documento_identidad"
formulario = TipoDocumentoIdentidadForm

plantilla_form = f"{modelo_string}_form.html"
url_home = "inicio"
url_list = f"{modelo_string}_list"
url_create = f"{modelo_string}_create"
url_update = f"{modelo_string}_update"
url_delete = f"{modelo_string}_delete"


# @method_decorator(login_required, name='dispatch')
class TipoDocumentoIdentidadListView(GenericListView):
	model = modelo
	context_object_name = 'datos'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_tipodoc_identidad__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": url_home,
		"url_create": url_create,
		"url_update": url_update,
		"url_delete": url_delete
	}


# @method_decorator(login_required, name='dispatch')
class TipoDocumentoIdentidadCreateView(GenericCreateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Crear {model.__name__}",
		"accion": f"Crear {model._meta.verbose_name}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class TipoDocumentoIdentidadUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Editar {model._meta.verbose_name}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class TipoDocumentoIdentidadDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Eliminar {model._meta.verbose_name}",
		"url_list" : url_list,
		"mensaje": "Estás seguro de que deseas eliminar el Tipo de Documento de Identidad"
	}
# ------------------------------------------------------------------------------
