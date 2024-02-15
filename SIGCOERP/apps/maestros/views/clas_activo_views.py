from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import ClasActivo
from ..forms.clas_activo_forms import ClasActivoForm


modelo = ClasActivo
modelo_string = "clas_activo"
formulario = ClasActivoForm

plantilla_form = f"{modelo_string}_form.html"
url_home = "inicio"
url_list = f"{modelo_string}_list"
url_create = f"{modelo_string}_create"
url_update = f"{modelo_string}_update"
url_delete = f"{modelo_string}_delete"


# @method_decorator(login_required, name='dispatch')
class ClasActivoListView(GenericListView):
	model = modelo
	context_object_name = 'datos'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_familia_activo__icontains=text) | \
					 Q(cta_compra__icontains=text) | \
					 Q(cta_venta__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": url_home,
		"url_create": url_create,
		"url_update": url_update,
		"url_delete": url_delete
	}


# @method_decorator(login_required, name='dispatch')
class ClasActivoCreateView(GenericCreateView):
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
class ClasActivoUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Editar {model.__name__}",
		"accion": f"Editar {model._meta.verbose_name}",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ClasActivoDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Eliminar {model.__name__}",
		"accion": f"Eliminar {model._meta.verbose_name}",
		"url_list" : url_list,
		"mensaje": "Estás seguro de que deseas eliminar la Familia Activo"
	}
# ------------------------------------------------------------------------------
