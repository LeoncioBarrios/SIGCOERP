from django import forms
from ..models.models_base import Color


class ColorForm(forms.ModelForm):
	class Meta:
		model = Color
		fields = '__all__'

		widgets = {
			"nombre_color": forms.TextInput(
				attrs={'class': 'form-control border border-primary'})
		}
