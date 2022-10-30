from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, template_name='index.html', context=dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    dado = {
        'receita': receita
    }
    return render(request, template_name='receita.html', context=dado)

def buscar(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome = request.GET.get('buscar')
        if nome:
            receitas = receitas.filter(nome_receita__icontains=nome)
    
    dados = {
        'receitas': receitas
    }
    return render(request, template_name='buscar.html', context=dados)