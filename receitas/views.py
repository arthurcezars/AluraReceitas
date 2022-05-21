from django.shortcuts import render

# Create your views here.
def index(request):
    receitas = {
        1: 'Lasanha',
        2: 'Sopa de legumes',
        3: 'Sorvete'
    }

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request, template_name='index.html', context=dados)

def receita(request):
    return render(request, template_name='receita.html')