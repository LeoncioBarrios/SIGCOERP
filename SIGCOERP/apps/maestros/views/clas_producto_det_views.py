from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import ClasProductoDet
from ..forms.clas_producto_det_forms import ClasProductoDetForm


modelo = ClasProductoDet
formulario = ClasProductoDetForm
plantilla_form = "clas_producto_det_form.html"
url_list = "clas_producto_det_list"


# @method_decorator(login_required, name='dispatch')
class ClasProductoDetListView(GenericListView):
	model = modelo
	context_object_name = 'clas_productos_det'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_sub_familia__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": "inicio"
	}


# @method_decorator(login_required, name='dispatch')
class ClasProductoDetCreateView(GenericCreateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Crear {model}",
		"accion": "Crear Sub Familia",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ClasProductoDetUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Editar {model}",
		"accion": "Editar Sub Familia",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ClasProductoDetDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Eliminar {model.__name__}",
		"accion": "Eliminar Sub Familia",
		"url_list" : url_list,
		"mensaje": "Estás seguro de que deseas eliminar la Sub Familia"
	}
# ------------------------------------------------------------------------------
