from django.shortcuts import redirect, render
from django.contrib.auth.models import User


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
        print(email, senha)
    return render(request, 'usuarios/login.html')

def logout(request):
    return render(request, 'usuarios/logout.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')