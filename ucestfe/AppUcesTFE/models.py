from django.db import models

from django.db.models.fields import BooleanField

from django.contrib.auth.models import User


# Create your models here.


#Usuario -< proyecto -< Variable


class Proyecto(models.Model):

    tema = models.CharField(max_length=500)
    hasta = models.IntegerField(null=True, blank=True)
    precision = models.CharField(max_length=50)
    # Define la relación uno a muchos con el modelo User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class Datos_Globales_Editables(models.Model):
     
     api_key = models.CharField(max_length=100)
     email = models.EmailField()
     password = models.CharField(max_length=100)

class VariableBD(models.Model):

     nombre = models.CharField(max_length=100)
     nombre_corto = models.CharField(max_length=100)
     descripcion = models.CharField(max_length=1000)
     #IMPO-INCE
     importancia = models.IntegerField(null=True, blank=True)
     incertidumbre = models.IntegerField(null=True, blank=True)
     #Para MIC MAC directo
     influencia1 = models.FloatField(null=True, blank=True)
     dependencia1 = models.FloatField(null=True, blank=True)
     #Para MIC MAC indirecto
     influencia2 = models.FloatField(null=True, blank=True)
     dependencia2 = models.FloatField(null=True, blank=True)
     #Para MIC MAC estable
     influencia5 = models.FloatField(null=True, blank=True)
     dependencia5 = models.FloatField(null=True, blank=True)
     #Para el PESTEl pertinecia
     categoria = models.CharField(max_length=100)

     #Colección de string con determinadas caracteristicas para manejar como array
     numeros = models.CharField(max_length=100)
     tendencias = models.CharField(max_length=1000)

     #Relaciono con el proyecto
     proyecto = models.ManyToManyField(Proyecto)

