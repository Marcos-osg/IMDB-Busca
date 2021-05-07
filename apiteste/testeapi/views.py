from django.shortcuts import render,HttpResponse
import requests
from django.views.generic import CreateView
import json


def index(request):
    return render(request, 'testeapi/index.html')


def busca_filmes(request):
    url = 'http://www.omdbapi.com/?t='
    filme = str(request.POST.get('nome'))
    key = '&apikey='  ##### INSIRA SUA API KEY AQUI #####
    busca = url + filme + key
    resposta = requests.get(busca)
    api = resposta.json()
    print(api)
    try:
        nome_filme = api['Title']
        descricao = api['Plot']
        ano = api['Year']
        imdb = api['imdbRating']
        dados = {'filme':nome_filme,'descricao':descricao,'ano':ano,'nota':imdb}
        return render(request,'testeapi/filmes.html', context=dados) 
    except:
        return render(request,'testeapi/erro.html')


