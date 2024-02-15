from django import forms
from ..models.models_base import CodigoSunat


class CodigoSunatForm(forms.ModelForm):
	class Meta:
		model = CodigoSunat
		fields = '__all__'

		widgets = {
			"codigo_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_codigo_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
		}
