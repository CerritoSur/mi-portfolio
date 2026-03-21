from django.contrib import admin
from .models import Proyecto

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tecnologia', 'fecha_creacion')
    list_filter = ('tecnologia',)
    search_fields = ('titulo', 'descripcion')
