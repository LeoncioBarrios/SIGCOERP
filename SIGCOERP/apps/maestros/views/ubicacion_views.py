from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import Ubicacion
from ..forms.ubicacion_forms import UbicacionForm


modelo = Ubicacion
formulario = UbicacionForm
plantilla_form = "ubicacion_form.html"
url_list = "ubicacion_list"


# @method_decorator(login_required, name='dispatch')
class UbicacionListView(GenericListView):
	model = modelo
	context_object_name = 'ubicaciones'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_marca__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": "inicio"
	}


# @method_decorator(login_required, name='dispatch')
class UbicacionCreateView(GenericCreateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Crear {model.__name__}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class UbicacionUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Editar {model.__name__}",
		"url_list" : url_list
	}

# @method_decorator(login_required, name='dispatch')
class UbicacionDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		"accion": f"Eliminar {model.__name__}",
		"url_list" : url_list,
		"mensaje": "Estás seguro que deseas eliminar la Ubicación"
	}
# ------------------------------------------------------------------------------
