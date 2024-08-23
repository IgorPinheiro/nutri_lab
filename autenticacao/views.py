from django.shortcuts import render
from django.http import HttpResponse


def cadastro(request):
    return render(request, 'cadastro/cadastro.html')

def login(request):
    return render(request, 'login/login.html')

