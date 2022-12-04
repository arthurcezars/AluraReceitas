from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome = request.GET.get('buscar')
        if nome:
            receitas = receitas.filter(nome_receita__icontains=nome)
    
    dados = {
        'receitas': receitas
    }
    return render(request, template_name='receitas/buscar.html', context=dados)