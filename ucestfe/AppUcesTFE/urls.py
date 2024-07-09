from django.urls import path
from . import views 

urlpatterns = [
    # Usar una cadena vacía para que sea la URL de inicio.
    path("detalles", views.detalles, name="detalles"),


    path("", views.inicio, name="inicio"),
  
    path("procesar_proyecto", views.procesar_proyecto, name="procesar_proyecto"),
    path('proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    #path('variables/proyecto/<int:proyecto_id>/', views.variables_por_proyecto, name='variables_por_proyecto'),
    #path('variables/proyecto_tendencias/<int:proyecto_id>/', views.variables_con_tendencias, name='variables_por_proyecto_tendencias'),

]

