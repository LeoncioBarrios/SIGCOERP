from django import forms
from ..models.models_base import Moneda


class MonedaForm(forms.ModelForm):
	class Meta:
		model = Moneda
		fields = '__all__'

		widgets = {
			"nombre_moneda": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"simbolo_moneda": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_moneda": forms.TextInput(
				attrs={'class': 'form-control border border-primary'})
		}
