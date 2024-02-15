from django import forms
from ..models.models_base import UnidadSunat


class UnidadSunatForm(forms.ModelForm):
	class Meta:
		model = UnidadSunat
		fields = '__all__'

		widgets = {
			"codigo_unidad_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_unidad_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
		}
