from django import forms
from .models import Envio,Docente, Universidad,Alumno

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = '__all__'    
        
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'
class EnvioForm(forms.ModelForm):
    class Meta:
        model = Envio
        fields = '__all__'  


