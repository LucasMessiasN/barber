from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Barbeiro, Atendimento, User
from .forms import ClienteForm, BarbeiroForm, AtendimentoForm

@login_required
def lista_users(request):
    users = User.objects.all()
    return render(request, 'lista_users.html', {'users': users})

@login_required
def deletar_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return render(request, 'lista_users.html', {'users': User.objects.all(), 'sucesso': True})

@login_required
def cadastro_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('lista_users')
    else:
        form = UserCreationForm()
    return render(request, 'cadastro_user.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def cadastro_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes.html')
    else:
        form = ClienteForm()
    return render(request, 'cadastro_cliente.html', {'form': form})

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

@login_required
def deletar_cliente(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    cliente.delete()
    return render(request, 'lista_clientes.html', {'clientes': Cliente.objects.all(), 'sucesso': True})

@login_required
def lista_barbeiros(request):
    barbeiros = Barbeiro.objects.all()
    return render(request, 'lista_barbeiros.html', {'barbeiros': barbeiros})

@login_required
def cadastro_barbeiros(request):
    if request.method == 'POST':
        form = BarbeiroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_barbeiros')
    else:
        form = BarbeiroForm()
    return render(request, 'cadastro_barbeiros.html', {'form': form})

@login_required
def deletar_barbeiro(request, barbeiro_id):
    barbeiro = Barbeiro.objects.get(id=barbeiro_id)
    barbeiro.delete()
    return render(request, 'lista_barbeiros.html', {'barbeiros': Barbeiro.objects.all(), 'sucesso': True})

@login_required
def cadastro_atendimento(request):
    if request.method == 'POST':
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_atendimentos')
    else:
        form = AtendimentoForm()
    return render(request, 'cadastro_atendimento.html', {'form': form})

@login_required
def lista_atendimentos(request):
    atendimentos_ativos = Atendimento.objects.filter(status__in=['aguardando', 'andamento'])
    print("ACHEI ESSES ATENDIMENTOS NO BANCO:", atendimentos_ativos)
    return render(request, 'lista_atendimentos.html', {'atendimentos': atendimentos_ativos})

@login_required
def concluir_atendimento(request, atendimento_id):
    atendimento = get_object_or_404(Atendimento, id=atendimento_id)
    atendimento.status = 'concluido'
    atendimento.save()
    return redirect('lista_atendimentos')

@login_required
def historico_atendimentos(request):
    historico = Atendimento.objects.filter(status='concluido')

    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    if data_inicio:
        historico = historico.filter(data_hora__date__gte=data_inicio)

    if data_fim:
        historico = historico.filter(data_hora__date__lte=data_fim)

    return render(request, 'historico_atendimentos.html', {'historico': historico})