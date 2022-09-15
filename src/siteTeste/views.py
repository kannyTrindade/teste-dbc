from django.http import HttpResponse
from django.shortcuts import render
from menu.models import Menu
from conteudo.models import blocoConteudo
from header.models import itemsHeader

def home(request):
    menus = Menu.objects.all()
    blocosDeConteudo = blocoConteudo.objects.all()
    header = itemsHeader.objects.all()
    context = { 'menus': menus, 'conteudo' : blocosDeConteudo, 'header': header }
    return render(request, 'index.html', context)