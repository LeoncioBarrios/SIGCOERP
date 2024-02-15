from django import forms
from ..models.models_base import CajaBanco


class CajaBancoForm(forms.ModelForm):
	class Meta:
		model = CajaBanco
		fields = '__all__'

		widgets = {
			"id_banco": forms.Select(
				attrs={'class': 'form-select border border-primary'}),
			"nombre_caja_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"tipo_caja_banco": forms.Select(
				attrs={'class': 'form-select border border-primary'}),
			"cuenta_caja_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"cuentacci_caja_banco": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"id_moneda": forms.Select(
				attrs={'class': 'form-select border border-primary'}),
			"estatus_caja_banco": forms.Select(
				attrs={'class': 'form-select border border-primary'})
		}
