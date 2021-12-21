from django.db import models
#from apps.comentario.models import Comentario


class Categoria(models.Model):
	detalle = models.CharField(max_length=255)
#	autor = models.ForeignKey(Comentario, on_delete=models.CASCADE, null=True)

	class Meta:
		db_table="Categoria"

	def __str__(self):
		return self.detalle