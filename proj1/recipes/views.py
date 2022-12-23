from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP RESPONSE

def home(request):
    return HttpResponse('home.html')

def sobre(request):
    return HttpResponse('<h1>SOBRE - Hello Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Hello Django</h1>')