from django.contrib import admin
from .models import *





# Register your models here..


class ProyectoAdmin(admin.ModelAdmin):

    list_display = ("id", "tema", "hasta", "precision")


class VariableBDAdmin(admin.ModelAdmin):

    list_display = ("id", "nombre", "nombre", "nombre_corto", "descripcion","importancia", "incertidumbre", "numeros")


admin.site.register(Proyecto,ProyectoAdmin)
admin.site.register(VariableBD, VariableBDAdmin)

