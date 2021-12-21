from django.db import models
from apps.usuarios.models import Usuario
from apps.post.models import Post


class Comentario(models.Model):
	detalle = models.TextField(max_length=1000)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
	estado = models.BooleanField(default=False)
	posteo = models.ForeignKey(Post,on_delete=models.CASCADE, null=True)


	class Meta:
		db_table="Comentario"

	def __str__(self):
		return self.detalle