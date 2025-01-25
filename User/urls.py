from django.urls import path
from Appbelen import views
from User import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('login/',views.login_request, name='login'),
    path('perfil/',views.perfil, name='perfil'),
    path('register/',views.register, name='register'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('editar_usuario/', views.editar_perfil, name="editar_usuario"),
    path('eliminar_avatar/', views.eliminar_avatar, name='eliminar_avatar'),


    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)