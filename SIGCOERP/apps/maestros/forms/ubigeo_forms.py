from django import forms
from ..models.models_base import Ubigeo


class UbigeoForm(forms.ModelForm):
	class Meta:
		model = Ubigeo
		fields = '__all__'

		widgets = {
			"ubigeo": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"departamento": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"provincia": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"distrito": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"tipo_ubigeo": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'})
		}
