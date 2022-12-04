from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.order_by('-data_receita').filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request, template_name='receitas/index.html', context=dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    
    dado = {
        'receita': receita
    }
    return render(request, template_name='receitas/receita.html', context=dado)

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST.get('nome_receita')
        ingredientes = request.POST.get('ingredientes')
        modo_preparo = request.POST.get('modo_preparo')
        tempo_preparo = request.POST.get('tempo_preparo')
        rendimento = request.POST.get('rendimento')
        categoria = request.POST.get('categoria')
        foto_receita = request.FILES.get('foto_receita')
        user = get_object_or_404(User, pk=request.user.id)

        receita = Receita.objects.create(
            pessoa=user,
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=foto_receita
        )
        receita.save()

        return redirect('dashboard')
    return render(request, 'receitas/cria_receita.html')

def deleta_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita.delete()
    return redirect('dashboard')

def edita_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_a_editar = {
        'receita': receita
    }

    return render(request, 'receitas/edita_receita.html', context=receita_a_editar)

def atualiza_receita(request):
    if request.method == 'POST':
        receita_id = request.POST.get('receita_id')
        receita = Receita.objects.get(pk=receita_id)
        receita.nome_receita = request.POST.get('nome_receita')
        receita.ingredientes = request.POST.get('ingredientes')
        receita.modo_preparo = request.POST.get('modo_preparo')
        receita.tempo_preparo = request.POST.get('tempo_preparo')
        receita.rendimento = request.POST.get('rendimento')
        receita.categoria = request.POST.get('categoria')
        if 'foto_receita' in request.FILES:
            receita.foto_receita = request.FILES.get('foto_receita')
        receita.save()
        return redirect('dashboard')