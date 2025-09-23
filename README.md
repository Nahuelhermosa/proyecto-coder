        .Proyecto Colegio Superior Belgrano

Este proyecto es una aplicación web desarrollada con Django que permite gestionar estudiantes, cursos y profesores de manera sencilla.

.Incluye un menú principal, páginas de listado y creación de registros, y un diseño responsivo con Bootstrap 5.

        .Funcionalidades principales

Página de inicio con logo y mensaje de bienvenida.

Gestión de estudiantes:

Listado de estudiantes.

Creación de nuevos estudiantes.

Gestión de profesores:

Listado de profesores.

Creación de nuevos profesores.

Gestión de cursos:

Listado de cursos.

Creación de nuevos cursos.

Navegación clara mediante una barra de menú.

        .Tecnologías utilizadas

Python 3.12

Django 5.2.6

Bootstrap 5 (para el diseño responsivo)

SQLite (base de datos por defecto de Django)

        .Estructura del proyecto

trabajo-coder/
│
├─ core/                # Aplicación principal
│   ├─ migrations/
│   ├─ static/          # Archivos estáticos (logo, css, js)
│   ├─ templates/       # Templates HTML
│   │   └─ index.html
│   ├─ urls.py          # Rutas de la app
│   └─ views.py         # Vistas de la app
│
├─ coder/               # Configuración del proyecto
│   ├─ settings.py
│   ├─ urls.py
│   └─ wsgi.py
│
├─ manage.py
└─ README.md

        .Instalación y ejecución

git clone <url-del-repo>
cd trabajo-coder

python -m venv .venv
.venv\Scripts\activate     # En Windows
source .venv/bin/activate  # En Linux/Mac

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

http://127.0.0.1:8000/
