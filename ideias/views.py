from django.shortcuts import render
from ideias import Pessoa

# Create your views here.

def index(request):
    context = {
    if request.method == 'post':
        pessoa = Pessoa()
        pessoa.nome = request.post.get('nome')
        pessoa.sobrenome = request.post.get('sobrenome')
        pessoa.email = request.post.get('email')
        pessoa.genero = request.post.get('genero')
        pessoa.biografia = request.post.get('biografia')
        pessoa.save()
        context = {'msg', 'Parabéns :)'}
    }
    return render(request, 'index.html', context)

def sobre(request):
    pessoa = Pessoa.objects
    context = {

    }
    return render(request, 'sobre.html', context)

def contato(request):
    context = {

    }
    return render(request, 'contato.html', context)