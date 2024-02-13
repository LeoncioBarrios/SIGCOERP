from django import forms
from ..models.models_base import Unidad

class UnidadForm(forms.ModelForm):
	class Meta:
		model = Unidad
		fields = '__all__'
		
		widgets = {
			"nombre_unidad": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"abreviado": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"codigo_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"equivalente": forms.NumberInput(
				attrs={'class': 'form-control border border-primary'})
		}