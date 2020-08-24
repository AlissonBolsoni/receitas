from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from site_receita.models import Receita


# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado')
            return redirect('cadastro')
        if User.objects.filter(username=nome).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-data_receita').filter(pessoa=id)

        dados = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        redirect('index')


def logout(request):
    auth.logout(request)
    redirect('index')

