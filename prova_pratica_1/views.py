from django.shortcuts import render
import random

from primo_progetto.prima_app.views import lista 
# Create your views here.

def index (request):
    return render (request, "prova_pratica_1/index.html") 

def somma(request):
    context = {
        'var1': random.randint(1,10),
        'var2': random.randint(1,10),
        'somma': 'var1' + 'var2',
    }
    return render(request, 'somma.html', context)

def media(request):
    lista = [random.randint(1,10) for i in range(0, 30)]
    somma = 0 
    for i in range(len(lista)):
        somma += lista[i]
    media = somma / len(lista)

    context = {
        'lista': lista,
        'somma': somma,
        'media': media,
    }
    return render(request, 'media.html', context)

def voti(request):
    context = {
        'var1',
        'var2',
    }
    return render(request, 'media.html', context)
