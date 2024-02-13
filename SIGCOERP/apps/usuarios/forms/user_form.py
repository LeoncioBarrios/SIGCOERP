from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group

#from apps.usuarios.models.user_models import User
from apps.usuarios.models import User


# -- Registrar Usuario ------------------------------------------------------------------------------------------------
class RegistroUsuarioForm(UserCreationForm):
	
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'email_alt',
			'telefono',
			'is_active',
			'password1',
			'password2'
		]

class EditarUsuarioForm(UserChangeForm):
	
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
			'email_alt',
			'telefono',
			'is_active',
		]

class GroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ["name"]
