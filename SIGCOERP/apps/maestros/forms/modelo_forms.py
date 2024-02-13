from django import forms
from ..models.models_base import Modelo


class ModeloForm(forms.ModelForm):
	class Meta:
		model = Modelo
		fields = '__all__'

		widgets = {
			"nombre_modelo": forms.TextInput(
				attrs={'class': 'form-control border border-primary'})
		}
