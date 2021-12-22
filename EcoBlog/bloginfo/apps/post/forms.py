from django import forms


from .models import Post

class PostForm(forms.ModelForm):
	nombre = forms.CharField(label="Nombre del Post", widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Ingrese nombre del post"}))
	detalle = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = Post
		fields = ["nombre", "detalle","estado","categoria"]