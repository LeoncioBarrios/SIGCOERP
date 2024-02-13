from django import forms
from ..models.models_base import Ubicacion


class UbicacionForm(forms.ModelForm):
	class Meta:
		model = Ubicacion
		fields = '__all__'

		widgets = {
			"nombre_ubicacion": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"ubicacion_fisica": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
		}
