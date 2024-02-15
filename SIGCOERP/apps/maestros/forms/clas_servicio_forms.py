from django import forms
from ..models.models_base import ClasServicio


class ClasServicioForm(forms.ModelForm):
	class Meta:
		model = ClasServicio
		fields = '__all__'

		widgets = {
			"nombre_familia_servicio": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"cta_compra": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"cta_venta": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nc_compra": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nc_venta": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nd_compra": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nd_venta": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
		}
