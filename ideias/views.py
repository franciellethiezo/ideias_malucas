from django.shortcuts import render

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context)

def sobre(request):
    context = {

    }
    return render(request, 'sobre.html', context)

def contato(request):
    context = {

    }
    return render(request, 'contato.html', context)