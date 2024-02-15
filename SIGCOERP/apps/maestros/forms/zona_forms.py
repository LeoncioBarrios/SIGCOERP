from django import forms
from ..models.models_base import Zona


class ZonaForm(forms.ModelForm):
	class Meta:
		model = Zona
		fields = '__all__'

		widgets = {
			"nombre_zona": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_zona": forms.TextInput(
				attrs={'class': 'form-control border border-primary'})
		}
