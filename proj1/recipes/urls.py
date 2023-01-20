from django.urls import path
from recipes.views import home, sobre, contato, receitas, receitas2, receitas3

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),
    path('receita/', receitas, name='receitas'),
    path('receita2/', receitas2, name='receitas2'),
    path('receita3/', receitas3, name='receitas3')

]