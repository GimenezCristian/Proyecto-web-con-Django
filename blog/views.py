from django.shortcuts import render
from blog.models import Post
from blog.models import Categoria

# Create your views here.

def blog (request):
    
    posts=Post.objects.all()
    categoria=Categoria.objects.all()

    return render (request, "blog/blog.html", {"posts":posts,"categorias":categoria})