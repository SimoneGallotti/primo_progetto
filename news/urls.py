from django.urls import path
from .views import listaArticoli

urlpatterns = [
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
]
