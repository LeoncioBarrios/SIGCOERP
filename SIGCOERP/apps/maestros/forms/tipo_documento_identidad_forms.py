from django import forms
from ..models.models_base import TipoDocumentoIdentidad


class TipoDocumentoIdentidadForm(forms.ModelForm):
	class Meta:
		model = TipoDocumentoIdentidad
		fields = '__all__'

		widgets = {
			"codigo_tipodoc_identidad": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"nombre_tipodoc_identidad": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"longitud": forms.NumberInput(
				attrs={'class': 'form-control border border-primary'})
		}
