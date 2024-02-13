from django import forms
from ..models.models_base import Marca


class MarcaForm(forms.ModelForm):
	class Meta:
		model = Marca
		fields = '__all__'

		widgets = {
			"nombre_marca": forms.TextInput(
				attrs={'class': 'form-control border border-primary'})
		}
