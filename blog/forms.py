from django import forms
from .models import Post
from .models import Enfermedad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        labels = {'title':'Titulo', 'text':'Texto'}
        
        
class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
        
class EnfermedadForm(forms.ModelForm):
    
    class Meta:
        model =  Enfermedad
        fields = [
            'Nombre',
            'Sexo',
            'edad',
            'inicio_sintomas',
            'fin_sintomas',
            'vacunado'
        ]
        labels ={
            'nombre':'Nombre',
            'sexo':'Sexo',
            'edad':'Edad',
            'inicio_sintomas':'Fecha de inicio de sintomas',
            'fin_sintomas':'Fecha de finalizacion de sintomas',
            'vacunado':'¿Ya esta vacunado?'
        }
        widgets = {
            'inicio_sintomas':forms.DateInput(attrs={'type':'date'}),
            'fin_sintomas': forms.DateInput(attrs={'type':'date'})   
        }