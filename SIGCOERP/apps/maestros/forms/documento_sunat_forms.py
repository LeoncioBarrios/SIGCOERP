from django import forms
from ..models.models_base import DocumentoSunat


class DocumentoSunatForm(forms.ModelForm):
	class Meta:
		model = DocumentoSunat
		fields = '__all__'

		widgets = {
			"nombre_documento_sunat": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"abreviado": forms.TextInput(
				attrs={'class': 'form-control border border-primary'}),
			"compra": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"venta": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"gasto": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"honorario": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"guia": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"nc": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"nd": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"percepcion": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"retencion": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
			"otros": forms.CheckboxInput(
				attrs={'class': 'form-check-input border border-primary'}),
		}
