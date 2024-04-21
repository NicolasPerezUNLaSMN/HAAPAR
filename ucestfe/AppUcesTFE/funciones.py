from AppUcesTFE.models import *


#transforma las variables en nombres cortos
import re

import time

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import numpy as np

from openai import OpenAI

KEY= "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"

#Clase para trabajar en memoria, no es persistida en BD
class Variable:

    def __init__(self, variable_id, nombre, nombre_corto, importancia, incertidumbre, numeros, strings, categoria):
        self.variable_id = variable_id
        self.nombre = nombre
        self.nombre_corto = nombre_corto
        self.importancia = importancia
        self.incertidumbre = incertidumbre
        self.numeros = numeros #este lo usaré para el micmac
        self.strings = strings #este lo usaré para identificar tendencias

        #Para el PESTEL - Politico, economico, social tecnologico, ecologico, legal
        self.categoria = categoria

        #Influencia y dependencia de la micmac, potencia 1, 2 y 5
        self.inf = 0
        self.dep = 0

        self.inf2 = 0
        self.dep2 = 0

        self.inf5 = 0
        self.dep5 = 0


#cuento ; para saber cuantas respuestas me da chat gpt
def contar_puntos_y_coma(cadena):
    contador = 0
    for caracter in cadena:
        if caracter == ';':
            contador += 1
    return contador


def respuestas_a_lista(resp):
  # Dividir el texto en oraciones usando el punto y coma como delimitador
  variables = resp.split(';')

  # Limpiar espacios en blanco alrededor de cada oración
  variables_limpias = [var.strip() for var in variables]

  return variables_limpias

def crear_variables(oraciones):
    variables = []

    for oracion in oraciones:
        # Eliminar caracteres no alfanuméricos y convertir a minúsculas
        oracion_limpia = re.sub(r'[^a-zA-Z0-9 ]', '', oracion).lower()


         # Tomar las primeras cuatro letras de cada palabra y unirlas con "_"
        palabras = [palabra[:4] for palabra in oracion_limpia.split()]
        variable = '_'.join(palabras)[:20]

        variables.append(variable)



    return variables




#insertar las variables en la base de datos
def cargar_variables(id_proyecto, lista_or, lista_abr, lista_imp, lista_inc, cant):

  cantidad = len(lista_or)
  variables = list()

  for i in range (cantidad):

    array = influencia_pedir_matriz(lista_or[i], lista_or)

    cat = pedir_categoria(lista_or[i])

    array[i] = 3 #Pongo 3 en la diagonal, es decir en la pos correspondiente a la variable


    v = Variable(variable_id=i+1, nombre=lista_or[i], nombre_corto=lista_abr[i], importancia=lista_imp[i], incertidumbre=lista_inc[i], numeros=array, strings=[""]*cant, categoria=cat  )

    print(array)

    time.sleep(2) #Espero un rato antes d evolver a conectar con chat gpt

    #traigo el proyecto con el que relaciono
    proyecto = Proyecto.objects.get(id=id_proyecto)

    instancia_variable = VariableBD(nombre=v.nombre,
                                     nombre_corto=v.nombre_corto,
                                       descripcion="Nada", 
                                       importancia=v.importancia,
                                         incertidumbre=v.incertidumbre, 
                                         numeros=v.numeros, 
                                         categoria=v.categoria)

    

    instancia_variable.save()

    instancia_variable.proyecto.add(proyecto)

    instancia_variable.save()

    variables.append(v)

    #Acá seria la carga en la BD v.save()

  return variables


def influencia_pedir_matriz(var,vars_todas):

          client = OpenAI(api_key=KEY)
          tam = len(vars_todas)


          prompt = f"Hola. Necesito que me respondas con un array de {tam} elementos de números enteros. Los numeros deben ser 0 para nada, 1 para poco, 2 para algo y 3 para mucho. Te estoy dando una lista de oraciones: {vars_todas}, quiero que el array  este compuesto por esos numeros del 0 al 3, para identificar que tanto influye esto: '{var}' en cada una de las oraciones sobre todas las otras, los numeros en el mismo orden que las oraciones. Gracias, espero tu resultado. Solo dame el array, no hace falta más texto ni explicaciones."

          chat_completion = client.chat.completions.create(
              messages = [
                  {
                      "role":"user",
                  "content":prompt
                  },
              ],
              model="gpt-3.5-turbo"
          )

          matriz = chat_completion.choices[0].message.content

          # Elimina los corchetes y luego divide los valores por coma
          valores_string = matriz[1:-1].split(',')

          # Convierte los valores a enteros
          valores_enteros = [int(valor) for valor in valores_string]


          return valores_enteros

def pedir_categoria(var):

          client = OpenAI(api_key=KEY)



          prompt = f"Necesito que me digas en que categoria meterias a: {var}. Podes elegir solo una de estas categorias, no quiero explicaciones, solo dame la categoria, ¿Politica, Economica, Social, Tecnologica, Ecologica o Legal?"

          chat_completion = client.chat.completions.create(
              messages = [
                  {
                      "role":"user",
                  "content":prompt
                  },
              ],
              model="gpt-3.5-turbo"
          )

          respuesta = chat_completion.choices[0].message.content




          return respuesta


def pedir_variables(tema, anio, lim_inf, lim_sup):

            client = OpenAI(api_key=KEY)



            preguntar = True

            while preguntar:

              prompt = f"Qué variables te parecen necesarias para estudiar el futuro de: {tema} de acá al año: {anio}. Ya se que es difícil y que solo sos un modelo, dame entre {lim_inf} y {lim_sup} variables separadas por punto y coma. No quiero que me expliques nada, solo dame las variables separadas por punto y coma. Que las variables sean oraciones cortas, nada extenso, y escritas de forma cuantificable, es decir, cantidad de..., numero de..., tasa de..., nivel de..., grado de ... etc. Reitero, solo dame las variables (oraciones) separadas por punto y coma."

              chat_completion = client.chat.completions.create(
                  messages = [
                      {
                          "role":"user",
                      "content":prompt
                      },
                  ],
                  model="gpt-3.5-turbo"
              )

              respuesta = chat_completion.choices[0].message.content

              if contar_puntos_y_coma(respuesta) > lim_inf:
                preguntar = False


            return respuesta


def asignar_importancia(variables_limpias,tema,anio):

        client = OpenAI(api_key=KEY)
        preguntar = True


        while preguntar:
            prompt = f"Dadas estas variables: {variables_limpias}. Me gustaría que le asignes una importancia del 1 al 10 a cada una. No seas tibio quiero números sin que justifiques, tu sabrás el por qué. Esa importancia para estudiar {tema} al {anio}. Que los números estén separados por ; y en el orden de las oraciones que te di. Solo dame los valores separados por ; no le pongas comillas ni nada, ni termines en '.' porque necesito leer esa info. Se que todas son importantes, pero no tengas miedo de asignarle números bajos a algunas."

            chat_completion = client.chat.completions.create(
                messages = [
                    {
                        "role":"user",
                    "content":prompt
                    },
                ],
                model="gpt-3.5-turbo"
            )

            respuestas_importancias = chat_completion.choices[0].message.content

            #Le saco el punto que aveces pone chatgpt
            respuestas_importancias = respuestas_importancias.replace(".","")
            respuestas_importancias

            # Dividir el texto en oraciones usando el punto y coma como delimitador
            variables_importancias = respuestas_importancias.split(';')

            # Limpiar espacios en blanco alrededor de cada oración
            variables_importancias_limpias = [var.strip() for var in variables_importancias]
            print(f"Comparativa: {len(variables_importancias_limpias) -- len(variables_limpias) }")

            preguntar = not (len(variables_importancias_limpias) == len(variables_limpias))


        importancias_int = list(map(int, variables_importancias_limpias))

        return importancias_int


#Crear la matriz numerica mic_mac, recibe por parametro la lista de variables con el arreglo de numeros de la IA
def crear_matriz_micmac(variables_cargadas):
      matriz_mic_mac = []



      for var in variables_cargadas:

        matriz_mic_mac.append(var.numeros)

      return matriz_mic_mac


#Prueba para enviar mail con los resultados finales



#Funciona, super chequeado, sacar credenciales de la BD

def enviar_correo(destinatario, asunto, mensaje):
    remitente = "@gmail.com"  # Cambia esto por tu dirección de correo electrónico
    password = "tbkm iqfm wjpa tere"  # Cambia esto por tu contraseña

    # Crear mensaje MIME
    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    # Agregar cuerpo del mensaje
    msg.attach(MIMEText(mensaje, 'plain'))

    # Establecer conexión con el servidor SMTP de Gmail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Iniciar sesión y enviar correo electrónico
    server.login(remitente, password)
    server.sendmail(remitente, destinatario, msg.as_string())

    # Cerrar conexión con el servidor SMTP
    server.quit()

# Llamar a la función enviar_correo con el destinatario, asunto y mensaje
#enviar_correo("nico_perez_velez@hotmail.com", "Prueba UCES", "Andará.")
    


def elevar_matriz(matriz, potencia):

  resultado = np.linalg.matrix_power(matriz, potencia)

  return resultado




#Le doy mi matriz de nxn, y agrega una columna y una fila con las sumas normalizadas, devuelve matriz n+1 x n+1 ultimo elemento -1
#OJO la devuelve como matriz de INT no dividi por los maximos
def matriz_normalizada(matriz):



      # Agregar una columna con la suma de cada fila
      suma_filas = np.sum(matriz, axis=1, keepdims=True)
      matriz_con_suma_filas = np.hstack((matriz, suma_filas))

      # Agregar una fila con la suma de cada columna
      suma_columnas = np.sum(matriz_con_suma_filas, axis=0, keepdims=True)
      matriz_con_suma_total = np.vstack((matriz_con_suma_filas, suma_columnas))

      #Saco el ultimo elemento que no me sirve.

      # Obtener las dimensiones de la matriz
      filas, columnas = matriz_con_suma_total.shape

      # Cambiar el último elemento de la última fila y última columna por -1
      matriz_con_suma_total[filas-1, columnas-1] = -1



      return  matriz_con_suma_total


def asignar_incertidumbres(variables_limpias, tema, anio):

        client = OpenAI(api_key=KEY)


        preguntar = True


        while preguntar:

            prompt = f"Dadas estas variables: {variables_limpias}. Me gustaría que le asignes una incertidumbre del 1 al 10 a cada una (10 es muchísima incertidumbre). No seas tibio quiero números sin que justifiques. Esa importancia para estudiar {tema} al {anio}. Que los números estén separados por ; y en el orden de las oraciones que te di. Solo dame los valores separados por ; no le pongas comillas ni nada, ni termines en '.' porque necesito leer esa info. Como te di {len(variables_limpias)} oraciones, estoy esperando {len(variables_limpias)} números. Se que todas son inciertas, pero no tengas miedo de asignarle números bajos a algunas."

            chat_completion = client.chat.completions.create(
                messages = [
                    {
                        "role":"user",
                    "content":prompt
                    },
                ],
                model="gpt-3.5-turbo"
            )

            respuestas_incertidumbres = chat_completion.choices[0].message.content

            #Le saco el punto que aveces pone chatgpt
            respuestas_incertidumbres = respuestas_incertidumbres.replace(".","")


            # Dividir el texto en oraciones usando el punto y coma como delimitador
            variables_incertidumbres = respuestas_incertidumbres.split(';')

            # Limpiar espacios en blanco alrededor de cada oración
            variables_incertidumbres_limpias = [var.strip() for var in variables_incertidumbres]
            print(f"Comparativa: {len(variables_incertidumbres_limpias)} -- {len(variables_limpias) }")

            preguntar = not (len(variables_incertidumbres_limpias) == len(variables_limpias))

        incertidumbres_int = list(map(int, variables_incertidumbres_limpias))

        return incertidumbres_int



def matriz_normalizada_division(matriz):





      # Transformar la matriz de enteros a una matriz de punto flotante
      matriz_float = matriz.astype(float)

      # Encontrar el valor máximo de la última columna
      maximo_valor_ultima_columna = np.max(matriz_float[:, -1])


      # Dividir la última columna por el valor máximo

      matriz_float[:, -1] = matriz_float[:, -1] / maximo_valor_ultima_columna

      # Encontrar el valor máximo de la última fila
      maximo_valor_ultima_fila = np.max(matriz_float[-1])


      # Dividir la última columna por el valor máximo

      matriz_float[-1] = matriz_float[-1] / maximo_valor_ultima_fila

      return   matriz_float