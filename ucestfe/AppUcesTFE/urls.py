from django.urls import path
from . import views
urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("", views.index, name="index"),


    path("inicio", views.inicio, name="inicio"),
    path("procesar_proyecto", views.procesar_proyecto, name="procesar_proyecto"),

]

