from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Afonso Henrique'})

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')

def receitas(request):
    return render(request, 'recipes/pages/receitas.html', context={'name': 'Afonso Henrique'})

def receitas2(request):
    return render(request, 'recipes/pages/receitas2.html', context={'name': 'Afonso Henrique'})

def receitas3(request):
    return render(request, 'recipes/pages/receitas3.html', context={'name': 'Afonso Henrique'})
# Create your views here.