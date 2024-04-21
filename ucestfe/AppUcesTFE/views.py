from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from .funciones import *

from datetime import datetime

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("¡Hola, mundo!")


def inicio(request):

    return render(request, 'AppUcesTFE/index.html')


def procesar_proyecto(request):

  
        if request.method == 'POST':
                
                anio= int(request.POST.get('anio'))
                tema= request.POST.get('tema')
                precision= request.POST.get('precision')

                print(f"{anio} ---- {tema} ---- {precision}")

                #en caso que el año no sea correcto tambien devuelvo el error
                now = datetime.now().year

                #Caso año incorrecto
                if (anio  < now + 5) or (anio > 2200):
                      datos= {"error":"El reporte debe ser como minimo a 5 años y menor al 2200!!!"}
                      return render(request, 'AppUcesTFE/index.html', {"datos":datos})
                #caso año correcto     
                else:
                    
                    print("Empieza a procesar la informacion")
                    generar_persistencia(request, tema, anio, precision)

                    return render(request, 'AppUcesTFE/index.html')
                

        #caso primer increo sin post
        else:
                return render(request, 'AppUcesTFE/index.html')


def procesar_proyecto2(request):

    try:
        if request.method == 'POST':
                
                anio= int(request.POST.get('anio'))
                tema= request.POST.get('tema')
                precision= request.POST.get('precision')

                print(f"{anio} ---- {tema} ---- {precision}")

                #en caso que el año no sea correcto tambien devuelvo el error
                now = datetime.now().year

                #Caso año incorrecto
                if (anio  < now + 5) or (anio > 2200):
                      datos= {"error":"El reporte debe ser como minimo a 5 años y menor al 2200!!!"}
                      return render(request, 'AppUcesTFE/index.html', {"datos":datos})
                #caso año correcto     
                else:
                    
                    print("Empieza a procesar la informacion")
                    generar_persistencia(request, tema, anio, precision)

                    return render(request, 'AppUcesTFE/index.html')
                

        #caso primer increo sin post
        else:
                return render(request, 'AppUcesTFE/index.html')
        
    #Caso que falto el casteo   
    except ValueError:

        datos= {"error":"El valor tiene que ser entero!!!"}
        print(datos)
        return render(request, 'AppUcesTFE/index.html', {"datos":datos})
        #return HttpResponse(diccionario["error"])
    
    

#Funciones asociadas a vistas
def generar_persistencia(request,tema, anio, precision):
     
    instancia_proyecto = Proyecto(tema=tema, hasta=anio, precision=precision, usuario = request.user)
    
    instancia_proyecto.save()

    id_proyecto = instancia_proyecto.id

    lim_inf = 2
    lim_sup = 5

    #Mejor hacer una funcion pero como no está definido lo dejo así
    if (precision == "Normal"):
         lim_inf = 10
         lim_sup = 15
         
    if (precision == "Alta"):
         lim_inf = 25
         lim_sup = 30

    #Llamo a chatgpt
    #Recibo variables separadas por ;
    respuesta = pedir_variables(tema, anio, lim_inf, lim_sup)

    #Ahora las separo en un array
    variables_limpias = respuestas_a_lista(respuesta) 

    #al array de variables le genero un array de importancia y de incertidumbre
    variables_importancias_limpias = asignar_importancia(variables_limpias, tema, anio)
    variables_incertidumbres_limpias = asignar_incertidumbres(variables_limpias, tema, anio)

    #Ahora creo el conjunto de nombre abreviados
    variables_limpias_abreviadas = crear_variables(variables_limpias)

    #Proceso más largo, genero variables con todo junto y llamo a CHATGPT par asignar MICMAC por renglon
    cant_var = len(variables_limpias)
    variables_cargadas = cargar_variables(id_proyecto, variables_limpias,variables_limpias_abreviadas,variables_importancias_limpias,variables_incertidumbres_limpias,cant_var )