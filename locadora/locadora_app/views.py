from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from locadora.locadora_app.models import Filme


def filme(requisicao, indice):
    filme = Filme.objects.order_by('id')[indice - 1]
    contexto = {'indice': indice, 'filme': filme}
    return render(requisicao, 'locadora/filme.html', contexto)


def filmes(requisicao):
    filmes = Filme.objects.all().order_by('ano')
    contexto = {'filmes': filmes}
    return render(requisicao, 'locadora/index.html', contexto)
