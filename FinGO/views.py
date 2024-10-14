from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    return render(request, 'main/dashboard.html')

def despesas(request):
    return render(request, 'main/despesas.html')

def receitas(request):
    return render(request, 'main/receitas.html')

def categorias(request):
    return render(request, 'main/categorias.html')

def metas(request):
    return render(request, 'main/relatorios.html')

def configuracoes(request):
    return render(request, 'main/configuracoes.html')



# def despesas(request):
#     return render(request, 'expenses/add_expense.html')