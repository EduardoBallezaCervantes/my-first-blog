from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm, CustomUserForm, EnfermedadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def registrar_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #autentificar al usuario  y redirigirlo al inicio
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to = 'post_list')
        else:
            messages.error(request, 'Los campos no estan llenados correctamente y no se permiten espacios')
    return render(request,'registration/registrar.html', data)

@login_required
def enfermedad_view(request):
    data = {
        'form':EnfermedadForm
    }
    if request.method == 'POST':
        form = EnfermedadForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect(to = 'post_list')
    return render(request,'seguimiento/Enfermedad_form.html', data)