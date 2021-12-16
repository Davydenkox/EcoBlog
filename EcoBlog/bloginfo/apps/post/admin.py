from django.contrib import admin

from .models import Post



class postAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor')

admin.site.register(Post,postAdmin)
