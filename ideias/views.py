from django.shortcuts import render
from ideias.models import Pessoa

# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.genero = request.POST.get('genero')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        context = {'msg' : 'Parabéns :)'}
    return render(request, 'index.html', context)

def sobre(request):
    pessoa = Pessoa.objects.filter(ativo=True).all()
    context = {'pessoas' :pessoa
    }
    return render(request, 'sobre.html', context)

def contato(request):
    context = {

    }
    return render(request, 'contato.html', context)