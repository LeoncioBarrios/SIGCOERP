from django import forms
from ..models.models_base import ClasProductoDet


class ClasProductoDetForm(forms.ModelForm):
	class Meta:
		model = ClasProductoDet
		fields = '__all__'

		widgets = {
			"nombre_sub_familia": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"id_clas_producto": forms.Select(
				attrs={'class': 'form-control border border-primary'}),
		}
