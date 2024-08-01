from django.shortcuts import render, redirect
from .models import Produto, Venda, ItensVenda, Cliente, Fornecedor, Vendedor
from .forms import ClienteForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Função para renderizar a página inicial
def home(request):
    return render(request, 'trade/home.html')


# Função para cadastrar clientes
def cadastro_clientes(request):
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados do POST
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Salva o cliente se o formulário for válido
            form.save()
            return redirect('home')
    else:
        # Cria um formulário vazio para o método GET
        form = ClienteForm()
    # Renderiza o template de cadastro de clientes com o formulário
    return render(request, 'trade/cadastro_clientes.html', {'form': form})


# Função para exibir tabelas demonstrativas
def demonstrativo_tabelas(request):
    # Obtém todos os registros das tabelas relevantes
    clientes = Cliente.objects.all()
    fornecedores = Fornecedor.objects.all()
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    # Renderiza o template com os dados das tabelas
    return render(request, 'trade/demonstrativo_tabelas.html', {
        'clientes': clientes,
        'fornecedores': fornecedores,
        'produtos': produtos,
        'vendas': vendas,
    })


# Função para exibir a galeria de produtos
def galeria_produtos(request):
    # Obtém todos os produtos
    produtos = Produto.objects.all()
    # Renderiza o template com a lista de produtos
    return render(request, 'trade/galeria_produtos.html', {'produtos': produtos})


# Função para realizar uma venda
def realizar_venda(request):
    if request.method == 'POST':
        # Lógica simplificada para processar a venda
        cliente_id = request.POST.get('cliente')
        produto_id = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        cliente = Cliente.objects.get(idcli=cliente_id)
        produto = Produto.objects.get(idprod=produto_id)
        vendedor = Vendedor.objects.first()  # Supondo que há um vendedor padrão
        fornecedor = produto.idforn

        valor_venda = produto.valorprod * int(quantidade)
        # Cria uma nova venda
        venda = Venda.objects.create(
            codivend='12345',  # Código de venda gerado automaticamente
            idcli=cliente,
            idforn=fornecedor,
            idvende=vendedor,
            valorvend=valor_venda,
            descvend=0,
            totalvend=valor_venda,
            datavend='2023-07-19',  # Data atual
            valorcomissao=valor_venda * vendedor.porcvende / 100
        )

        # Adiciona os itens da venda
        ItensVenda.objects.create(
            idvend=venda,
            idprod=produto,
            valoritvend=produto.valorprod,
            qtditvend=quantidade,
            descitvend=0
        )

        return redirect('home')

    # Obtém clientes e produtos para o formulário de venda
    clientes = Cliente.objects.all()
    produtos = Produto.objects.all()
    # Renderiza o template de realizar venda com clientes e produtos
    return render(request, 'trade/realizar_venda.html', {
        'clientes': clientes,
        'produtos': produtos,
    })


# Função para exibir a página de login
def login_view(request):
    if request.method == 'POST':
        # Cria uma instância do formulário de autenticação com os dados do POST
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # Autentica o usuário
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        # Cria um formulário de autenticação vazio para o método GET
        form = AuthenticationForm()
    # Renderiza o template de login com o formulário
    return render(request, 'trade/login.html', {'form': form})


# Função para registrar um novo usuário
def register_view(request):
    if request.method == 'POST':
        # Cria uma instância do formulário de registro com os dados do POST
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        # Cria um formulário de registro vazio para o método GET
        form = UserRegisterForm()
    # Renderiza o template de registro com o formulário
    return render(request, 'trade/register.html', {'form': form})


# Função para fazer logout do usuário
def logout_view(request):
    logout(request)
    return redirect('login')


# Função para renderizar a página de boas-vindas, disponível apenas para usuários autenticados
@login_required
def welcome_view(request):
    return render(request, 'trade/home.html')
