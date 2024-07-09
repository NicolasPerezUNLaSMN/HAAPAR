from django.db import models

from django.db.models.fields import BooleanField

from django.contrib.auth.models import User

from django.shortcuts import render


# Create your models here.


#Usuario -< proyecto -< Variable


class Proyecto(models.Model):

    tema = models.CharField(max_length=500)
    hasta = models.IntegerField(null=True, blank=True)
    precision = models.CharField(max_length=50)
    # Define la relación uno a muchos con el modelo User
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    cuadrante1 = models.CharField(null=True,max_length=50)
    cuadrante2 = models.CharField(null=True,max_length=50)
    cuadrante3 = models.CharField(null=True,max_length=50)
    cuadrante4 = models.CharField(null=True,max_length=50)

    def __str__(self):
        return f"{self.tema} ({self.usuario.username})"

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
    
     
     #Para el PESTEl pertinecia
     categoria = models.CharField(max_length=100)

     #Colección de string con determinadas caracteristicas para manejar como array
     numeros = models.CharField(max_length=100)
     tendencias = models.CharField(max_length=1000)

     tipo = models.CharField(null=True,max_length=100) #interno o externo

     #Relaciono con el proyecto
     proyecto = models.ManyToManyField(Proyecto)

     def __str__(self):
        return self.nombre
     
class Actor(models.Model):

    nombre = models.CharField(max_length=100)
    objetivo = models.CharField(max_length=100)
    #Colección de string con determinadas caracteristicas para manejar como array
    numeros = models.CharField(max_length=100)

    #Relaciono con el proyecto
    proyecto = models.ManyToManyField(Proyecto)

    def __str__(self):
        return self.nombre
    
class Fortaleza(models.Model):

    nombre = models.CharField(max_length=100)

    #Relaciono con el proyecto
    proyecto = models.ManyToManyField(Proyecto)

    def __str__(self):
        return self.nombre
    
class Debilidad(models.Model):

    nombre = models.CharField(max_length=100)

    #Relaciono con el proyecto
    proyecto = models.ManyToManyField(Proyecto)

    def __str__(self):
        return self.nombre
    
class Oportunidad(models.Model):

    nombre = models.CharField(max_length=100)

    #Relaciono con el proyecto
    proyecto = models.ManyToManyField(Proyecto)

    def __str__(self):
        return self.nombre
    
class Amenaza(models.Model):

    nombre = models.CharField(max_length=100)

    #Relaciono con el proyecto
    proyecto = models.ManyToManyField(Proyecto)

    def __str__(self):
        return self.nombre


    



class Matriz(models.Model):
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Matriz de {self.proyecto.tema}"
    

class MatrizCuadrada(models.Model):
    proyecto = models.OneToOneField(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f"Matriz cuadrada de {self.proyecto.tema}"
    
    

class ElementoMatriz(models.Model):
    matriz = models.ForeignKey(Matriz, on_delete=models.CASCADE)
    fila = models.IntegerField()
    columna = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return f"Elemento ({self.fila}, {self.columna}): {self.valor}"


class ElementoMatrizCuadrada(models.Model):
    matrizCuadrada = models.ForeignKey(MatrizCuadrada, on_delete=models.CASCADE)
    fila = models.IntegerField()
    columna = models.IntegerField()
    valor = models.IntegerField()

    def __str__(self):
        return f"Elemento ({self.fila}, {self.columna}): {self.valor}"