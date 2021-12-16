
# Register your models here.
from django.contrib import admin

from .models import Comentario



class comentarioAdmin(admin.ModelAdmin):
    list_display = ('autor','detalle', 'posteo')

admin.site.register(Comentario,comentarioAdmin)