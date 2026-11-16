from django.urls import path
from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

def listaArticoli(request, pk=None):
    # Verifica se è stato passato il parametro pk (primary key del giornalista) nell'URL
    if pk == None:
        # Query ORM: recupera tutti i record presenti nella tabella Articolo
        articoli = Articolo.objects.all()
        # Imposta giornalista a None perché si stanno visualizzando tutti gli articoli
        giornalista = None
    else:
        # Query ORM: filtra gli articoli estraendo solo quelli associati al giornalista con id pari a pk
        articoli = Articolo.objects.filter(giornalista_id=pk)
        # Query ORM: recupera il singolo record del Giornalista per mostrarne nome e cognome nel template
        giornalista = get_object_or_404(Giornalista, pk=pk)

    # Passa al template la lista degli articoli e la variabile giornalista per gestire l'intestazione
    context = {
        'articoli': articoli,
        'giornalista': giornalista,
    }
    return render(request, 'lista_articoli.html', context)