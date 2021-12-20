from django import forms


from .models import Comentario

class ComentarioForm(forms.ModelForm):
	#autor = forms.CharField(label="Nombre del Post", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre del post"}))
	detalle = forms.CharField(widget=forms.Textarea)
	estado = forms.BooleanField(required=False,initial=False)
	class Meta:
		model = Comentario
		fields = ["detalle","autor","estado"]