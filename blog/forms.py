from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']