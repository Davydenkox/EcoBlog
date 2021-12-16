
# Register your models here.
from django.contrib import admin

from .models import Categoria



class categoriaAdmin(admin.ModelAdmin):
    list_display = ('detalle', )

admin.site.register(Categoria,categoriaAdmin)