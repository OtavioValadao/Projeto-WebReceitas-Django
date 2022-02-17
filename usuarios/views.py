from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from receitas.models import Receita



#cria as funçoes para as urls
def cadastro(request):
    if request.method == 'POST':  # capitura as informaçoes digitadas no cadastro do usuari, lá do html aonde está os input, lembrando que o input é o mesmo com o nome do http
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')
        if senha != senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists(): #verifica se já existe um email cadastrado no banco de dados
            print('Usuário já cadastrado')
            return redirect('cadastro') #redireciona para pagina de cadastro
        user = User.objects.create_user(username=nome, email=email, password=senha) #cria os objetos na base de dados
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login') #redireciona para pagina de login
    else:
        return render(request,'usuarios/cadastro.html') #cria as def para aparecer na pagina

def login(request):
    if request.method == 'POST':  # capitura as informaçoes digitadas no cadastro do usuari, lá do html aonde está os input, lembrano que o input é o mesmo com o nome do http
        email = request.POST['email'] # observa sempre o input
        senha = request.POST['senha'] # observa sempre o input
        if email == "" or senha == "":
            print('Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists(): #verifica se já existe um email cadastrado no banco de dados pois o django usa como metodo apenas ''usuario'' e não email
            nome = User.objects.filter(email=email).values_list('username', flat=True).get() #altera o get de email para usuario
            user = auth.authenticate(request, username=nome, password=senha) #autenticando o usuario e senha
            if user is not None:
                auth.login(request,user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated: # se o usuario estiver autenticado 
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa = id).first() 
        # mostra as receitas apenas com as pessoas com o id especifico

        dados = {
            'receita' : receitas
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita'] # observa sempre o input
        ingredientes = request.POST['ingredientes'] # observa sempre o input
        modo_preparo = request.POST['modo_preparo'] # observa sempre o input
        tempo_preparo = request.POST['tempo_preparo'] # observa sempre o input
        rendimento = request.POST['rendimento'] # observa sempre o input
        categoria = request.POST['categoria'] # observa sempre o input
        foto_receita = request.FILES['foto_receita'] # aqui é um tipo 'file' pois é imagem
        user = get_object_or_404(User, pk=request.user.id) #na requisição, trazemos o id do usuario e passamos esse id para a variavel user
        receita = Receita.objects.create(pessoa = user,nome_receita = nome_receita, ingredientes = ingredientes, modo_preparo = modo_preparo,tempo_preparo = tempo_preparo, rendimento = rendimento,categoria = categoria, foto_receita = foto_receita) # fazendo com que a pessoa seja o usuario, pois o djanfo aceita apenas usuarios e não 'emails'
        receita.save() # salva no banco de dados 
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')