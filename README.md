🏫 Proyecto Django – Trabajo Final Coder
📘 Descripción

Este proyecto fue desarrollado como trabajo final del curso de Django.
El sistema representa un sitio institucional para un colegio, donde se gestionan estudiantes, profesores y cursos.
Además, incluye funcionalidades de autenticación y una sección especial para cursos de verano.

El proyecto está construido con Django, usando templates con Bootstrap para un diseño moderno y responsivo.

⚙️ Estructura de Aplicaciones
1️⃣ core

Contiene las secciones principales del sitio:

index: página de inicio con el logo institucional (en /static/img/logo.png).

estudiantes: CRUD completo (crear, editar, eliminar y listar estudiantes).

profesores: CRUD completo (crear, editar, eliminar y listar profesores).

cursos: listado general de cursos del colegio.

2️⃣ accounts

Maneja la autenticación de usuarios (login, logout y registro).
Permite acceder al panel principal solo a usuarios autenticados.

3️⃣ cursosverano

Aplicación adicional donde se gestionan los Cursos de Verano.
Incluye formulario de alta y listado, utilizando el modelo CursoVerano.

🧩 Funcionalidades CRUD en core
👨‍🏫 Profesores

Crear nuevo profesor mediante formulario.

Editar datos existentes.

Eliminar profesor.

Listado con nombre, apellido y correo electrónico.

🎓 Estudiantes

Crear estudiante desde formulario.

Editar información.

Eliminar registro.

Listado con los datos completos y botones de acción (editar y eliminar).

Ambos CRUD usan plantillas con Bootstrap para mantener una interfaz uniforme, moderna y clara.


        .Estructura del proyecto

trabajo-coder/
│
├── manage.py
├── requirements.txt
│
├── core/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── core/
│   │   │   ├── index.html
│   │   │   ├── estudiantes.html
│   │   │   ├── profesor.html
│   │   │   ├── curso_list.html
│   │   │   ├── estudiante_form.html
│   │   │   ├── profesor_form.html
│   │   │   └── ...
│   └── static/
│       └── img/
│           └── logo.png
│
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── login.html
│           ├── logout.html
│           └── register.html
│
├── cursosverano/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── forms.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── cursosverano/
│           ├── curso_list.html
│           ├── curso_form.html
│           └── ...
│
└── proyecto/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


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

🔐 Usuario de Prueba

Para ingresar a la aplicación:

Usuario: usuario1
Contraseña: coder123