from django.urls import reverse_lazy

# from django.contrib.auth.decorators import login_required

from .cruds_views_generics import *
from ..models.models_base import ClasProducto
from ..forms.clas_producto_forms import ClasProductoForm


modelo = ClasProducto
formulario = ClasProductoForm
plantilla_form = "clas_producto_form.html"
url_list = "clas_producto_list"


# @method_decorator(login_required, name='dispatch')
class ClasProductoListView(GenericListView):
	model = modelo
	context_object_name = 'clas_productos'
	template_name = f"maestros/{url_list}.html"
	cadena_filtro = "Q(nombre_familia__icontains=text) | \
		Q(cta_compra__icontains=text) | Q(cta_venta__icontains=text) | \
		Q(nc_compra__icontains=text) | Q(nc_venta__icontains=text) | \
		Q(nd_compra__icontains=text) | Q(nd_venta__icontains=text)"
	extra_context = {
		"titulo": model._meta.verbose_name_plural,
		"url_inicio": "inicio"
	}

# @method_decorator(login_required, name='dispatch')
class ClasProductoCreateView(GenericCreateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Crear {model.__name__}",
		"accion": "Crear Familia",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ClasProductoUpdateView(GenericUpdateView):
	model = modelo
	form_class = formulario
	template_name = f"maestros/{plantilla_form}"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Editar {model.__name__}",
		"accion": "Editar Familia",
		"url_list" : url_list
	}


# @method_decorator(login_required, name='dispatch')
class ClasProductoDeleteView(GenericDeleteView):
	model = modelo
	template_name = "base_confirm_delete.html"
	success_url = reverse_lazy(url_list) # Nombre de la url.
	extra_context = {
		#"accion": f"Eliminar {model.__name__}",
		"accion": "Eliminar Familia",
		"url_list" : url_list,
		"mensaje": "Estás seguro de que deseas eliminar la Familia"
	}
# ------------------------------------------------------------------------------
