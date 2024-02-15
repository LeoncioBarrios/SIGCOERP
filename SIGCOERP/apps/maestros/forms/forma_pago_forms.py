from django import forms
from ..models.models_base import FormaPago


class FormaPagoForm(forms.ModelForm):
	class Meta:
		model = FormaPago
		fields = '__all__'

		widgets = {
			"nombre_forma_pago": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"codigo_forma_pago": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"compra": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"venta": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"pventa": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"otros": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'})
		}
