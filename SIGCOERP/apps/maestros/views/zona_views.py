from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import Zona
from ..forms.zona_forms import ZonaForm


modelo = Zona
modelo_string = modelo.__name__.lower()
formulario = ZonaForm

plantilla_form = f"{modelo_string}_form.html"
url_home = "inicio"
url_list = f"{modelo_string}_list"
url_create = f"{modelo_string}_create"
url_update = f"{modelo_string}_update"
url_delete = f"{modelo_string}_delete"


# @method_decorator(login_required, name='dispatch')
class ZonaListView(GenericListView):
	model = modelo
	context_object_name = 'datos'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_zona__icontains=text) | \
					 Q(descripcion_zona__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": url_home,
		"url_create": url_create,
		"url_update": url_update,
		"url_delete": url_delete
	}


# @method_decorator(login_required, name='dispatch')
class ZonaCreateView(GenericCreateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Crear {model._meta.verbose_name}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ZonaUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Editar {model._meta.verbose_name}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ZonaDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Eliminar {model._meta.verbose_name}",
		"url_list" : url_list,
		"mensaje": "Estás seguro de que deseas eliminar la Zona"
	}
# ------------------------------------------------------------------------------
