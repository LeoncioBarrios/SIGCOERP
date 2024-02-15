from django import forms
from ..models.models_base import SubZona


class SubZonaForm(forms.ModelForm):
	class Meta:
		model = SubZona
		fields = '__all__'

		widgets = {
			"nombre_sub_zona": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"descripcion_sub_zona": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"id_zona": forms.Select(
				attrs={'class': 'form-select border border-primary'}),
			#"id_zona": forms.Select(
			#	attrs={'class': 'form-control border border-primary'})
		}
