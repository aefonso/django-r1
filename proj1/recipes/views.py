from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP RESPONSE

def home(request):
    return HttpResponse('HOME - Hello Django ')

def sobre(request):
    return HttpResponse('SOBRE - Hello Django')

def contato(request):
    return HttpResponse('CONTATO - Hello Django')