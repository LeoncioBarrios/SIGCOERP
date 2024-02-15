from django import forms
from ..models.models_base import Banco


class BancoForm(forms.ModelForm):
	class Meta:
		model = Banco
		fields = '__all__'

		widgets = {
			"codigo_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nombre_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
		}
