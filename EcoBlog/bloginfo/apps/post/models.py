from django.db import models
from apps.usuarios.models import Usuario


class Post(models.Model):
	nombre = models.CharField(max_length=255)
	detalle = models.TextField(max_length=1000)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
	estado = models.IntegerField(null=True)
	categoria = models.CharField(max_length=255, null=True)

	class Meta:
		db_table="post"

	def __str__(self):
		return self.nombre

