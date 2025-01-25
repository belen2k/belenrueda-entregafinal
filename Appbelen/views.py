from django.shortcuts import render , redirect
from .forms import DocenteForm , UniversidadForm , EnvioForm,AlumnoForm
from .models import Universidad , Docente , Alumno , Envio
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.



def inicio(request):
    return render(request,'appbelen/index.html')

def conoceme(req):
    return render(req,'appbelen/conoceme.html')

#                                            VISTAS (CREAR / AGREGAR)
@login_required
def agregar_universidad(request):
    if request.method == 'POST':
        form = UniversidadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_universidad')
    else:
        form = UniversidadForm()
    return render(request, 'Appbelen/agregar_universidad.html', {'form': form})


@login_required
def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_alumno')
    else:
        form = AlumnoForm()
    return render(request, 'Appbelen/agregar_alumno.html', {'form': form})
    
@login_required
def agregar_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_docente')
    else:
        form = DocenteForm()
    return render(request, 'Appbelen/agregar_docente.html', {'form': form})

    
@login_required
def agregar_envio(request):
    if request.method == 'POST':
        form = EnvioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_envio')
    else:
        form = EnvioForm()
    return render(request, 'Appbelen/agregar_envio.html', {'form': form})

#                                           ClASES BASADAS EN VISTAS (Update / Editar )

class UniversidadUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Universidad
    form_class = UniversidadForm
    template_name = "appbelenc/editar_universidad.html"
    success_url = reverse_lazy("lista_universidad")

class AlumnoUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Alumno
    form_class = AlumnoForm
    template_name = "appbelen/editar_alumno.html"
    success_url = reverse_lazy("lista_alumno")
    
class DocenteUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Docente
    form_class = DocenteForm
    template_name = "appbelen/editar_docente.html"
    success_url = reverse_lazy("lista_docente")
    
class EnvioUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Envio
    form_class = EnvioForm
    template_name = "appbelen/editar_envio.html"
    success_url = reverse_lazy("lista_envio")

#                                           ClASES BASADAS EN VISTAS (DELETE / Eliminar )

class UniversidadDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Universidad
    success_url = reverse_lazy("lista_universidad")  # URL de redirección después de eliminar un curso
    template_name = "appbelen/eliminar_universidad.html"  # Plantilla para confirmar la eliminación
    
class AlumnoDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Alumno
    success_url = reverse_lazy("lista_alumno")  # URL de redirección después de eliminar un curso
    template_name = "appbelen/eliminar_alumno.html"  # Plantilla para confirmar la eliminación
    
class DocenteDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Docente
    success_url = reverse_lazy("lista_docente")  # URL de redirección después de eliminar un curso
    template_name = "appbelen/eliminar_docente.html"  # Plantilla para confirmar la eliminación
    
class EnvioDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Envio
    success_url = reverse_lazy("lista_envio")  # URL de redirección después de eliminar un curso
    template_name = "appbelen/eliminar_envio.html"  # Plantilla para confirmar la eliminación


#                                           ClASES BASADAS EN VISTAS ( Detail / Detalles  )


class UniversidadDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Universidad
    template_name = "appbelen/detalle_universidad.html"
    
    
class AlumnoDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Alumno
    template_name = "appbelen/detalle_alumno.html"
    
    
class DocenteDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Docente
    template_name = "appbelen/detalle_docente.html"
    

class EnvioDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Envio
    template_name = "appbelen/detalle_envio.html"

#                                           ClASES BASADAS EN VISTAS ( List /Listas  )

class UniversidadListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Universidad  # Modelo con el que trabaja esta vista
    template_name = "appbelen/lista_universidad.html"  # Plantilla para renderizar la lista
    
class AlumnoListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Alumno  # Modelo con el que trabaja esta vista
    template_name = "appbelen/lista_alumno.html"  # Plantilla para renderizar la lista
    
class DocenteListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Docente  # Modelo con el que trabaja esta vista
    template_name = "appbelen/lista_docente.html"  # Plantilla para renderizar la lista
    
class EnvioListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Envio  # Modelo con el que trabaja esta vista
    template_name = "appbelen/lista_envio.html"  # Plantilla para renderizar la lista


#                                                 -------LISTAS-----------

# def lista_docente(request):
#     docente = Docente.objects.all()  # Obtiene todos los docentes
#     return render(request, 'appbelen/lista_docente.html', {'docentes': docente})

# def lista_alumno(request):
#     alumno = Alumno.objects.all()
#     return render(request, 'appbelen/lista_alumno.html',{'alumnos':alumno})


# def lista_universidad (request):
#     universidad = Universidad.objects.all()
#     return render(request,'appbelen/lista_universidad.html',{'universidades':universidad})


# def lista_envio(request):
#     envio = Envio.objects.all()
#     return render(request, 'appbelen/lista_envio.html',{'envios':envio})


#                       ----- BUSQUEDA DE UNIVERSIDADES METODO GET------
@login_required
def buscar_universidades(request):
    """
    Vista para buscar universidades en la base de datos.
    Si el usuario proporciona un nombre, filtra por ese criterio.
    Si no hay búsqueda, muestra todas las universidades.
    """
    # Obtener el parámetro 'q' desde la URL. Si no existe, usar una cadena vacía por defecto.
    query = request.GET.get('q', '')

    # Si hay un término de búsqueda, buscar universidades cuyo nombre coincida parcialmente.
    if query:
        universidades = Universidad.objects.filter(nombre__icontains=query)  # Búsqueda insensible a mayúsculas/minúsculas
    else:
        universidades = Universidad.objects.all()  # Si no hay consulta, mostrar todas las universidades.

    # Renderizar la plantilla y enviar las universidades y la consulta como contexto.
    return render(request, 'appbelen/buscar_universidades.html', {'universidades': universidades, 'query': query})
