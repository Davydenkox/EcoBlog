from django.db import models
from apps.usuarios.models import Usuario
#from apps.comentario.models import Comentario
from apps.categoria.models import Categoria

class Post(models.Model):
	nombre = models.CharField(max_length=255)
	detalle = models.TextField(max_length=1000)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True,blank=True)
	estado = models.BooleanField(default=False,null=True,blank=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,null=True,blank=True)
	
	#comentarios = models.ManyToManyField(Comentario,null=True, blank=True)

	class Meta:
		db_table="post"

	def __str__(self):
		return self.nombre

