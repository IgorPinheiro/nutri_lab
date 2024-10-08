from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import password_is_valid
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    
    elif request.method == 'POST':
        username = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
       
        if not password_is_valid(request, senha, confirmar_senha):
            return redirect( '/auth/cadastro/' )
            
        # Teste1234
        try:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=senha,
                                            is_active=False)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário Cadastrado com sucesso')
            return redirect('/auth/login/')
        
        except:
            messages.add_message(request, constants.ERROR, 'Erro ao criar o usuario, tente novamente')
            return redirect('/auth/cadastro/')
        
    


def login(request):
    return render(request, 'login/login.html')

