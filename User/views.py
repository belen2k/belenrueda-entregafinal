from django.shortcuts import render, redirect
from .forms import UserRegisterForm , UserEditForm
from django.contrib.auth.forms import AuthenticationForm   # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Avatar




# Create your views here.

#                                 ---------------------------Vista de Inicio de Sesion---------------------------------

def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            # Obtiene las credenciales del formulario
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")

            # Intenta autenticar al usuario
            user = authenticate(username=usuario, password=clave)

            if user is not None:
                # Si la autenticación es exitosa, iniciar sesión
                login(request, user)
                return redirect("inicio")  # Redirige a la página de inicio o dashboard
            else:
                # Si la autenticación falla
                return render(request, "User/login.html", {
                    "mensaje": "Error, datos incorrectos",
                    "form": form
                })
        else:
            # Si el formulario no es válido
            return render(request, "User/login.html", {
                "mensaje": "Error, formulario inválido",
                "form": form
            })

    else:
        form = AuthenticationForm()  # Si es un GET, muestra el formulario vacío
        return render(request, "User/login.html", {"form": form})

#                               ---------------------------------Vista de registro--------------------------------------------                         
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la página de inicio después de la creación del usuario
            return redirect('inicio')  # Cambia 'inicio' al nombre de la URL correcta de tu app
    else:
        form = UserRegisterForm()

    return render(request, "User/register.html", {"form": form})

#           Vista de Cerrar sesion
@login_required
def cerrar_sesion(request):
    """
    Cierra la sesión del usuario y redirige a la página de inicio.
    """
    logout(request)  # Cierra la sesión
    return redirect('inicio')  # Redirige a la página de inicio después de cerrar sesión

#                          ------------------------ Vista de EDITAR USUARIO-------------------------

@login_required
def perfil(request):
    user = request.user
    return render(request, 'User/perfil.html', {'user': user})


@login_required
def editar_perfil(request):
    """
    Función de vista para manejar la edición del perfil de usuario.
    """
    usuario = request.user  

    # Verificar si el usuario tiene un avatar asociado
    avatar = Avatar.objects.filter(user=usuario).first()

    if request.method == 'POST':
        # Crear una instancia del formulario con los datos de la solicitud
        miFormulario = UserEditForm(request.POST, request.FILES, instance=request.user) 

        if miFormulario.is_valid():
            # Si se sube una nueva imagen
            if miFormulario.cleaned_data.get('imagen'):
                if avatar:
                    # Si ya existe un avatar, actualizarlo
                    avatar.imagen = miFormulario.cleaned_data['imagen']
                    avatar.save()
                else:
                    # Si no existe un avatar, crear uno nuevo
                    Avatar.objects.create(user=usuario, imagen=miFormulario.cleaned_data['imagen'])
            else:
                # Si no se ha subido una nueva imagen, no hacer nada con el avatar
                if avatar and not miFormulario.cleaned_data.get('imagen'):
                    avatar.delete()  # Eliminar el avatar si no se sube una nueva imagen

            # Guardar otros cambios del formulario (como el nombre y el correo)
            miFormulario.save()

            return redirect('inicio')  # Redirigir a la página del perfil o cualquier otra página que desees

    else:
        # Si es GET, prellenar el formulario con los datos actuales del usuario y su avatar
        initial_data = {'imagen': avatar.imagen if avatar else None}
        miFormulario = UserEditForm(initial=initial_data, instance=request.user)

    return render(request, "User/editar_usuario.html", {"form": miFormulario, "usuario": usuario, "avatar": avatar})


#                   -------------------------Vista de Agregar Avatar------------------------

    
#                                       ---------------------Vista de Eliminar Avatar-----------------------

@login_required
def eliminar_avatar(request):
    """
    Elimina el avatar del usuario logueado.
    """
    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).first()

    if avatar:
        avatar.delete()  # Eliminar el avatar

    return redirect('inicio')  # Redirigir a la página del perfil o a donde desees


