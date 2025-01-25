Proyecto Final - Gestión de Perfiles
Este proyecto es el resultado final del curso de Python de CoderHouse, desarrollado por Julian Salas. Se trata de una aplicación web diseñada para gestionar perfiles relacionados con universidades, docentes, alumnos y envíos. Proporciona herramientas para agregar, editar y visualizar información relevante de cada perfil.

Características
Gestión de perfiles de universidades, docentes, alumnos y envíos.
Formularios para registrar y editar perfiles.
Panel de administración para configuraciones avanzadas.
Navegación intuitiva para buscar y visualizar información.
Requisitos
Python: Versión 3.8 o superior.
Django: Versión 4.1 o superior.
Dependencias adicionales especificadas en el archivo requirements.txt.
Instalación
Clona este repositorio en tu máquina local.
bash
Copy
Edit
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
Instala las dependencias necesarias:
bash
Copy
Edit
pip install -r requirements.txt
Ejecuta las migraciones para configurar la base de datos:
bash
Copy
Edit
python manage.py migrate
Inicia el servidor de desarrollo:
bash
Copy
Edit
python manage.py runserver
Uso
Acceso a la aplicación
Abre tu navegador y dirígete a:
http://localhost:8000/.

Navegación
Página de inicio: Presenta la vista principal del sitio en http://localhost:8000/inicio.
Registro de perfiles: Formularios para añadir nuevos perfiles en http://localhost:8000/registro.
Panel de administración: Gestión avanzada de perfiles y configuraciones en http://localhost:8000/admin.
Categorías:
Universidades: http://localhost:8000/universidades
Docentes: http://localhost:8000/docentes
Alumnos: http://localhost:8000/alumnos
Envíos: http://localhost:8000/envios
En cada categoría podrás buscar, visualizar y administrar información detallada.

