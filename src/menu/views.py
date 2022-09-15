from django.shortcuts import render
from .models import Menu, MenuLateral

# Create your views here.
def menuPrincipal(request):
    return HttpResponse(Menu)
