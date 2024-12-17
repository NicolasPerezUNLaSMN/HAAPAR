# HAAPAR: Herramienta de Automatización para Análisis Prospectivo

Proyecto diseñado a medida de la carrera de: Especialización en Prospectiva Estrategica (UCES). 
HAAPAR es un software desarrollado en Python y Django, diseñado para automatizar análisis prospectivo estratégico utilizando PostgreSQL como base de datos. Este proyecto incluye herramientas para la generación de escenarios, matrices de impacto cruzado y más, todo optimizado para implementarse en entornos virtuales.

## **Requisitos Previos**

Antes de comenzar, asegúrate de tener instalado en tu sistema:
- **Python 3.8 o superior**
- **PostgreSQL**
- **pip** (gestor de paquetes de Python)
- **virtualenv** (para crear entornos virtuales)

## **Instalación**

Sigue los pasos a continuación para configurar el proyecto en tu máquina local:

### 1. Clona este repositorio
```bash
git clone https://github.com/tuusuario/HAAPAR.git
cd HAAPAR
```

### 2. Crea y activa un entorno virtual
```bash
virtualenv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate     # Para Windows
```

### 3. Instala las dependencias del proyecto
```bash
pip install -r requirements.txt
```

### 4. Configura la base de datos PostgreSQL
1. Crea una base de datos en PostgreSQL llamada `haapar`.
2. Actualiza el archivo `settings.py` en la sección `DATABASES` con tus credenciales de PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'haapar',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Realiza las migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Ejecuta el servidor de desarrollo
```bash
python manage.py runserver
```

Accede al servidor en [http://127.0.0.1:8000](http://127.0.0.1:8000).

## **Contribuciones**

¡Las contribuciones son bienvenidas! Si encuentras un problema o deseas agregar una nueva funcionalidad, no dudes en abrir un *issue* o enviar un *pull request*.

## **Licencia**

Este proyecto se distribuye bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por usar HAAPAR! 😊

ghp_pSaPXzdop7FChhQ
XgVD5c9qjCHwe7I0zQWfP

