# Proyecto Inventario de Productos - Inacap

Este es un proyecto web de Inventario de Productos desarrollado con Python y Django.

## Instalación

### Prerrequisitos

Asegúrate de tener instalado lo siguiente:

- Python (versión 3.8 o superior)
- pip
- mysql

### Pasos de Instalación

1. Clona el repositorio en tu máquina local:

```
git clone https://github.com/EnriAnC/project-inventory-django.git
```

2. Ve al directorio del proyecto:

```
cd project-inventory-django
```

3. Crea un entorno virtual para el proyecto:

```
python -m venv venv
```

4. Activa el entorno virtual:

```
(Linux/Mac): source venv/bin/activate
(Window): .venv\Scripts\activate
(git bash): source venv/Scripts/activate
```

5. Instala las dependencias del proyecto:

```
pip install -r requirements.txt
```

6. Define las variables de entorno y un archivo .env:

```
DJANGO_DB_ENGINE= django.db.backends.mysql
DJANGO_DB_NAME= -----
DJANGO_DB_USER= -----
DJANGO_DB_PASSWORD= -----
DJANGO_DB_HOST= -----
DJANGO_DB_PORT= -----
```

Asegúrate de reemplazar los valores con las configuraciones correctas para tu entorno.

7. Inicia el servidor de desarrollo:

```
py manage.py runserver
```

El servidor de desarrollo se iniciará en `http://localhost:8000`.
