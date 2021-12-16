from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from . models import Usuario

class UsuarioForm(UserCreationForm):
	username = forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre de usuario"}))
	first_name = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre"}))
	last_name = forms.CharField(label="Apellido", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese su apellido"}))
	


	class Meta:
		model = Usuario
		fields = ["username", "first_name", "last_name", "email", "dni"]

	'''def clean_username(self):
		username = self.cleaned_data["username"]

         >>>PARA AGREGAR UNA VALIDACION clean_username DEVUELVE LA CONTRASENIA LIMPIA SI SE VALIDA<<<<
		if "123" not in username:
			raise ValidationError("El nombre de usuario debe incluir la cadena 123") 
		return username'''