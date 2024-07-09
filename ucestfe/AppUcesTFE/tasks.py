# tasks.py en tu aplicación Django
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def procesar_proyecto_task(tema, anio, precision, email):
    # Aquí colocas el código para procesar la información
    # generar_persistencia(request, tema, anio, precision)  # Asegúrate de adaptar este método

    # Simula un procesamiento largo
    import time
    time.sleep(10)  # Simula un proceso de 10 segundos

    # Envía un correo electrónico cuando el proceso termine
    send_mail(
        'Proceso completado',
        'Tu proceso ha sido completado con éxito.',
        'from@example.com',
        [email],
        fail_silently=False,
    )