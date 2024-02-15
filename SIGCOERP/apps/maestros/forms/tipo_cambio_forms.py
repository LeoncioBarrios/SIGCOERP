from django import forms
from ..models.models_base import TipoCambio


class TipoCambioForm(forms.ModelForm):
	class Meta:
		model = TipoCambio
		fields = '__all__'

		widgets = {
			"id_moneda": forms.Select(
				attrs={'class': 'form-control border border-primary'}),
			
			#"fecha_cambio": forms.DateInput(
			#	attrs={'class': 'form-control border border-primary'}),
			"fecha_cambio": forms.TextInput(
				attrs={'type': 'date', 'class': 'form-control border border-primary datetimepicker'}),
				
			"tasa_compra": forms.NumberInput(
				attrs={'class': 'form-control border border-primary'}),
			"tasa_venta": forms.NumberInput(
				attrs={'class': 'form-control border border-primary'}),
		}
