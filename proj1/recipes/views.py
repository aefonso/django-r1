from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
# HTTP RESPONSE

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request,'sobre.html')

def contato(request):
    return render(request,'contato.html')
# Create your views here.