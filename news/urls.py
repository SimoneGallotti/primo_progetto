from django.urls import path
from .views import listaArticoli, queryBase, articoloDetailView
app_name="news"

urlpatterns = [
    path('lista_articoli/', listaArticoli, name="lista_articoli"),
    path('lista_articoli/<int:pk>', listaArticoli, name="lista_articoli_giornalista"),
    path('query_base/', queryBase, name="query_base"),
    path('articoli/<int:pk>',articoloDetailView, name="articolo_detail")
]
