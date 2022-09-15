from django.shortcuts import render
from .models import blocoConteudo, tipoDeConteudo

# Create your views here.
def blocoConteudo(request):
    return HttpResponse(blocoConteudo)
