import re
from django.contrib import messages
from django.contrib.messages import constants

def password_is_valid(request, senha, confirmar_senha):
    if len(senha) < 6:
        messages.add_message(request, constants.ERROR, 'Sua senha deve conter 6 ou mais caractertes')
        return False

    if not senha == confirmar_senha:
        messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
        return False
    
    if not re.search('[A-Z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
        return False

    if not re.search('[a-z]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
        return False

    if not re.search('[1-9]', senha):
        messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
        return False

    return True