from django.urls import path
from Appbelen import views
from .views import  buscar_universidades
from . import views


urlpatterns = [
    path('',views.inicio,name='inicio' ),
    path('conoceme/',views.conoceme,name='conoceme' ),

    # BUSQUEDA DE UNIVERSIDADES FORMULARIO GET

    path('buscar_universidades/', buscar_universidades, name='buscar_universidades'),

    # AGREGAR CRUD CREATE
    
    path('agregar_universidad/',views.agregar_universidad,name='agregar_universidad' ),
    path('agregar_alumno/',views.agregar_alumno,name='agregar_alumno' ),
    path('agregar_docente/',views.agregar_docente,name='agregar_docente' ),
    path('agregar_envio/',views.agregar_envio,name='agregar_envio' ),
    
    # EDITAR CRUD UPDATE
    
    path('editar_universidad/<int:pk>/', views.UniversidadUpdateView.as_view(), name='editar_universidad'),
    path('editar_alumno/<int:pk>/', views.AlumnoUpdateView.as_view(), name='editar_alumno'),
    path('editar_docente/<int:pk>/', views.DocenteUpdateView.as_view(), name='editar_docente'),
    path('editar_envio/<int:pk>/', views.EnvioUpdateView.as_view(), name='editar_envio'),
    
    # ELIMINAR CRUD DELETE
    
    path('eliminar_universidad/<int:pk>/', views.UniversidadDeleteView.as_view(), name='eliminar_universidad'),
    path('eliminar_alumno/<int:pk>/', views.AlumnoDeleteView.as_view(), name='eliminar_alumno'),
    path('eliminar_docente/<int:pk>/', views.DocenteDeleteView.as_view(), name='eliminar_docente'),
    path('eliminar_envio/<int:pk>/', views.EnvioDeleteView.as_view(), name='eliminar_envio'),
    
    # DETALLE CRUD DETAIL
    
    path('detalle_universidad/<int:pk>/', views.UniversidadDetalle.as_view(), name='detalle_universidad'),
    path('detalle_alumno/<int:pk>/', views.AlumnoDetalle.as_view(), name='detalle_alumno'),
    path('detalle_docente/<int:pk>/', views.DocenteDetalle.as_view(), name='detalle_docente'),
    path('detalle_envio/<int:pk>/', views.EnvioDetalle.as_view(), name='detalle_envio'),
    
    
    # URLs DE TODAS LAS LISTAS
    path('lista_docente/', views.DocenteListView.as_view(), name='lista_docente'),
    path('lista_alumno/', views.AlumnoListView.as_view(), name='lista_alumno'),
    path('lista_universidad/', views.UniversidadListView.as_view(), name='lista_universidad'),
    path('lista_envio/', views.EnvioListView.as_view(), name='lista_envio'),


]