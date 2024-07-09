from django.contrib import admin
from .models import *





# Register your models here..


class ElementoMatrizInline(admin.TabularInline):
    model = ElementoMatriz
    extra = 0

class ElementoMatrizCuadradaInline(admin.TabularInline):
    model = ElementoMatrizCuadrada
    extra = 0

class MatrizAdmin(admin.ModelAdmin):
    inlines = [ElementoMatrizInline]

class MatrizCuadradaAdmin(admin.ModelAdmin):
    inlines = [ElementoMatrizCuadradaInline]

class VariableBDInline(admin.TabularInline):
    model = VariableBD.proyecto.through
    extra = 0

class ActorInline(admin.TabularInline):
    model = Actor.proyecto.through
    extra = 0



class ProyectoAdmin(admin.ModelAdmin):
    inlines = [VariableBDInline]

class ActorAdmin(admin.ModelAdmin):
    inlines = [ActorInline]

admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Datos_Globales_Editables)
admin.site.register(VariableBD)
admin.site.register(Matriz, MatrizAdmin)
admin.site.register(MatrizCuadrada, MatrizCuadradaAdmin)
admin.site.register(Fortaleza)
admin.site.register(Debilidad)
admin.site.register(Oportunidad)
admin.site.register(Amenaza)




