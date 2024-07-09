from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
import json

from .funciones import *

from datetime import datetime

from .models import *

from .tasks import procesar_proyecto_task
from datetime import datetime

# Create your views here.


def inicio(request):

    proyectos = Proyecto.objects.all()

    return render(request, 'AppUcesTFE/index.html', {'proyectos': proyectos})

def  detalles(request):

    proyectos = Proyecto.objects.all()

    return render(request, 'AppUcesTFE/detalles.html', {'proyectos': proyectos})


def detalle_proyecto(request, proyecto_id):
    

    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    variables = VariableBD.objects.filter(proyecto=proyecto)
    matriz = get_object_or_404(Matriz, proyecto=proyecto)
    elementos_matriz = ElementoMatriz.objects.filter(matriz=matriz).order_by('fila', 'columna')

    #Agrego matriz cuadrada, sin chat gpt
    matriz2 = get_object_or_404(MatrizCuadrada, proyecto=proyecto)
    elementos_matriz2 = ElementoMatrizCuadrada.objects.filter(matrizCuadrada=matriz2).order_by('fila', 'columna')



    # Crear una estructura de matriz con filas y columnas adicionales
    cant_var = variables.count()
    matriz_completa = [[''] * (cant_var + 2) for _ in range(cant_var + 2)]

    #mio
    matriz_completa2 = [[''] * (cant_var + 2) for _ in range(cant_var + 2)]

    # Rellenar la primera fila y columna con los nombres cortos de las variables
    for idx, variable in enumerate(variables, start=1):
        matriz_completa[0][idx] = variable.nombre_corto
        matriz_completa[idx][0] = variable.nombre_corto

    # Mio
    for idx, variable in enumerate(variables, start=1):
        matriz_completa2[0][idx] = variable.nombre_corto
        matriz_completa2[idx][0] = variable.nombre_corto

    # Rellenar la matriz con los valores de los elementos
    for elemento in elementos_matriz:
        matriz_completa[elemento.fila + 1][elemento.columna + 1] = elemento.valor

    # mio
    for elemento in elementos_matriz2:
        matriz_completa2[elemento.fila + 1][elemento.columna + 1] = elemento.valor

    # Calcular las sumas por filas y columnas
    sumas_filas = []
    sumas_columnas = []
    for i in range(1, cant_var + 1):
        suma_fila = 0
        suma_columna = 0
        for j in range(1, cant_var + 1):
            valor = matriz_completa[i][j]
            if valor != '':
                suma_fila += valor
                suma_columna += matriz_completa[j][i]
        matriz_completa[i][cant_var + 1] = suma_fila  # Suma de la fila
        matriz_completa[cant_var + 1][i] = suma_columna  # Suma de la columna
        sumas_filas.append(suma_fila)
        sumas_columnas.append(suma_columna)

    #mio
    sumas_filas2 = []
    sumas_columnas2 = []
    for i in range(1, cant_var + 1):
        suma_fila2 = 0
        suma_columna2 = 0
        for j in range(1, cant_var + 1):
            valor2 = matriz_completa2[i][j]
            if valor2 != '':
                suma_fila2 += valor2
                suma_columna2 += matriz_completa2[j][i]
        matriz_completa2[i][cant_var + 1] = suma_fila2  # Suma de la fila
        matriz_completa2[cant_var + 1][i] = suma_columna2  # Suma de la columna
        sumas_filas2.append(suma_fila2)
        sumas_columnas2.append(suma_columna2)

    # Preparar los datos para Highcharts Heatmap
    data = []
    for i in range(1, cant_var + 1):
        for j in range(1, cant_var + 1):
            if matriz_completa[i][j] != '':
                data.append([j - 1, i - 1, matriz_completa[i][j]])  # Highcharts usa índices base 0

    x_categories = [variable.nombre_corto for variable in variables]
    y_categories = x_categories.copy()  # Porque es una matriz cuadrada

    # MIO Preparar los datos para Highcharts Heatmap
    data2 = []
    for i in range(1, cant_var + 1):
        for j in range(1, cant_var + 1):
            if matriz_completa2[i][j] != '':
                data2.append([j - 1, i - 1, matriz_completa2[i][j]])  # Highcharts usa índices base 0

    x_categories2 = [variable.nombre_corto for variable in variables]
    y_categories2 = x_categories2.copy()  # Porque es una matriz cuadrada

    # Preparar los datos para el gráfico de dispersión de sumas
    scatter_data = []
    for i in range(cant_var):
        scatter_data.append({
            'x': sumas_filas[i],
            'y': sumas_columnas[i],
            'name': x_categories[i]
        })

    # MIO Preparar los datos para el gráfico de dispersión de sumas
    scatter_data2 = []
    for i in range(cant_var):
        scatter_data2.append({
            'x': sumas_filas2[i],
            'y': sumas_columnas2[i],
            'name': x_categories2[i]
        })

    # Preparar los datos para el gráfico de dispersión de importancia e incertidumbre
    importance_uncertainty_data = []
    for variable in variables:
        importance_uncertainty_data.append({
            'x': variable.importancia,
            'y': variable.incertidumbre,
            'name': variable.nombre_corto
        })

    # Calcular puntajes de relevancia y seleccionar las dos variables más relevantes
    relevancias = []
    for i, variable in enumerate(variables):
        puntaje = (variable.importancia + variable.incertidumbre + sumas_filas[i] + sumas_columnas[i]+ sumas_filas2[i] + sumas_columnas2[i]) / 6
        relevancias.append((puntaje, variable))

    relevancias.sort(reverse=True, key=lambda x: x[0])
    variables_mas_relevantes = [var for _, var in relevancias[:2]]

    if not proyecto.cuadrante1:
    # Generar nombres para los cuadrantes usando la API de OpenAI
        variable_x = variables_mas_relevantes[0].nombre
        variable_y = variables_mas_relevantes[1].nombre
        openai.api_key = obtener_api_key()
        prompt = (f"Necesito que me des cuatro nombres marketineros y mediaticos, para describir 4 cuadrantes. "
                f"El primero tiene que ser para cuando {variable_x} y {variable_y} mejoran mucho con el tiempo; "
                f"el segundo cuando solo mejora {variable_y}; el tercero cuando ambas decrecen; "
                f"y el 4to cuando solo crece {variable_x}. No me des preambulos, solo damelos numerados del 1 al 4 separados por ;")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt}
            ]
        )

        quadrant_names = response['choices'][0]['message']['content'].strip().split("\n")
        proyecto.cuadrante1 = quadrant_names[0]
        proyecto.cuadrante2 = quadrant_names[1]
        proyecto.cuadrante3 = quadrant_names[2]
        proyecto.cuadrante4 = quadrant_names[3]
        proyecto.save()
    else:
        quadrant_names = [
            proyecto.cuadrante1,
            proyecto.cuadrante2,
            proyecto.cuadrante3,
            proyecto.cuadrante4
        ]

    # Construir los datos del árbol PESTEL
    tree_data = [
        {'id': '0.0', 'parent': '', 'name2': proyecto.tema, 'name': f"Estudio al {proyecto.hasta}, creado por: {proyecto.usuario}"}
    ]

    pestel_categories = ['Política', 'Económica', 'Social', 'Tecnológica', 'Ecológica', 'Legal']
    for idx, category in enumerate(pestel_categories, start=1):
        tree_data.append({'id': f'1.{idx}', 'parent': '0.0', 'name': category, 'name2':category})
        variables_categoria = variables.filter(categoria=category)
        for var_idx, variable in enumerate(variables_categoria, start=1):
            tree_data.append({'id': f'2.{idx}.{var_idx}', 'parent': f'1.{idx}', 'name': variable.nombre,'name2': variable.nombre_corto})
            for tend_idx in range(1, 11):
                tendencia = getattr(variable, f'tendencia_{tend_idx}', None)
                if tendencia:
                    tree_data.append({'id': f'3.{idx}.{var_idx}.{tend_idx}', 'parent': f'2.{idx}.{var_idx}', 'name': tendencia})

    print(json.dumps(tree_data))
    return render(request, 'AppUcesTFE/detalles.html', {
        'proyecto': proyecto,
        'variables': variables,
        'variables_mas_relevantes': variables_mas_relevantes,
        'quadrant_names': quadrant_names,
        'matriz_completa': json.dumps(matriz_completa),  # Por si necesitas la matriz completa en JS
        'matriz_completa2': json.dumps(matriz_completa2),  # Por si necesitas la matriz completa en JS
        'data': json.dumps(data),
        'data2': json.dumps(data2),
        'x_categories': json.dumps(x_categories),
        'y_categories': json.dumps(y_categories),
        'x_categories2': json.dumps(x_categories2),
        'y_categories2': json.dumps(y_categories2),
        'scatter_data': json.dumps(scatter_data),
        'scatter_data2': json.dumps(scatter_data2),
        'importance_uncertainty_data': json.dumps(importance_uncertainty_data),
        'tree_data': json.dumps(tree_data)  # Pasar los datos del árbol al template
    })


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


#Funciones asociadas a vistas
def generar_persistencia(request,tema, anio, precision):
     
    instancia_proyecto = Proyecto(tema=tema, hasta=anio, precision=precision, usuario = request.user)
    
    instancia_proyecto.save()

    id_proyecto = instancia_proyecto.id

    # Crear la matriz
    matriz = Matriz.objects.create(proyecto=instancia_proyecto)

    # Crear la matriz
    matriz_cuadrada = MatrizCuadrada.objects.create(proyecto=instancia_proyecto)

    lim_inf = 2
    lim_sup = 5

    #Mejor hacer una funcion pero como no está definido lo dejo así
    if (precision == "Normal"):
         lim_inf = 5
         lim_sup = 10
         
    if (precision == "Alta"):
         lim_inf = 10
         lim_sup = 20

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

    #Ahora creo el conjunto de nombre abreviados
    variables_internas = asignar_variables_internas(variables_limpias, tema, anio)

    #Proceso más largo, genero variables con todo junto y llamo a CHATGPT par asignar MICMAC por renglon
    cant_var = len(variables_limpias)
    
    variables_cargadas = cargar_variables(id_proyecto, variables_limpias,variables_limpias_abreviadas,variables_importancias_limpias,variables_incertidumbres_limpias,variables_internas,cant_var )

   
    
    # Crear los elementos de la matriz

    for i, variable in enumerate(variables_cargadas):
            
            numeros = variable.numeros
            for j, valor in enumerate(numeros):
                ElementoMatriz.objects.create(matriz=matriz, fila=i, columna=j, valor=valor)

    # Calcular la matriz cuadrada
    n = len(variables_cargadas)
    matriz_valores = [[0] * n for _ in range(n)]

    # Llenar matriz_valores con los valores de ElementoMatriz
    elementos_matriz = ElementoMatriz.objects.filter(matriz=matriz)
    for elemento in elementos_matriz:
        matriz_valores[elemento.fila][elemento.columna] = elemento.valor

    # Calcular producto matricial para la matriz cuadrada
    matriz_cuadrada_valores = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matriz_cuadrada_valores[i][j] += matriz_valores[i][k] * matriz_valores[k][j]
    
    # Guardar los elementos en ElementoMatrizCuadrada
    for i in range(n):
        for j in range(n):
            ElementoMatrizCuadrada.objects.create(matrizCuadrada=matriz_cuadrada, fila=i, columna=j, valor=matriz_cuadrada_valores[i][j])

    # Obtener actores desde la API de OpenAI
    actores = generar_actores(tema, anio)

    # Crear y asociar actores al proyecto
    for nombre_actor, objetivo_actor in actores:
        # Aquí puedes ajustar cómo se asignan los objetivos y números a los actores
        actor = Actor(nombre=nombre_actor, objetivo=objetivo_actor, numeros="1,2,3,4")
        actor.save()
        actor.proyecto.add(instancia_proyecto)

    # Obtener actores desde la API de OpenAI
    fortalezas = generar_fortalezas(tema, anio)

    for f in fortalezas:
        # Aquí puedes ajustar cómo se asignan los objetivos y números a los actores
        fortaleza = Fortaleza(nombre=f)
        fortaleza .save()
        fortaleza .proyecto.add(instancia_proyecto)


        # Obtener actores desde la API de OpenAI
    debilidades= generar_debilidades(tema, anio)

    for f in debilidades:
        # Aquí puedes ajustar cómo se asignan los objetivos y números a los actores
        fortaleza = Debilidad(nombre=f)
        fortaleza.save()
        fortaleza.proyecto.add(instancia_proyecto)

            # Obtener actores desde la API de OpenAI
    oportunidades= generar_oportunidades(tema, anio)

    for f in oportunidades:
        # Aquí puedes ajustar cómo se asignan los objetivos y números a los actores
        fortaleza = Oportunidad(nombre=f)
        fortaleza.save()
        fortaleza.proyecto.add(instancia_proyecto)

    amenazas= generar_amenazas(tema, anio)

    for f in amenazas:
        # Aquí puedes ajustar cómo se asignan los objetivos y números a los actores
        fortaleza = Amenaza(nombre=f)
        fortaleza.save()
        fortaleza.proyecto.add(instancia_proyecto)


    

# Trae las variables de un proyecto y les agrega una descripción con CHAT GPT
def variables_por_proyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    variables = VariableBD.objects.filter(proyecto=proyecto)

    for variable in variables:
        
            descripcion = generar_descripcion(variable)
            variable.descripcion = descripcion
            variable.save()

    variables = VariableBD.objects.filter(proyecto=proyecto)


    return render(request, 'AppUcesTFE/tu_template.html', {'variables': variables})





def variables_con_tendencias(request, proyecto_id):

    proyecto = Proyecto.objects.get(id=proyecto_id)

    variables = VariableBD.objects.filter(proyecto=proyecto)

    for variable in variables:
        
            tendencia= generar_tendencias(variable)
            variable.tendencias = tendencia
            variable.save()

    variables = VariableBD.objects.filter(proyecto=proyecto)


    return render(request, 'AppUcesTFE/tu_template.html', {'variables': variables})