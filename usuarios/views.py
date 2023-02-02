from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def entrar(request):
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # Use a autenticação do Django
        usu = authenticate(username=email, password=senha)
        # Se tem usuario
        if usu:
            #Checa se usuario esta ativo, é necessario para o futuro, caso voce destive o usuario ele não ira mais logar
            if usu.is_active:
                # Logando.
                login(request,usu)
                # SE LOGAR,Redireciona o usuario para uma pagina , nesse caso a Index .
                return redirect('contato:inicio')
            else:
                # Envia para uma pagina dizendo:
                messages.error(request, "Usuário não ativo")
                return render(request, 'login.html')
        else:
            #essa parte é legal , mostra para o usuario uma resposta
            messages.error(request, 'Erro no email ou senha')
            #volta para pagina do login para uma nova tentativa
            return redirect('usuarios:entrar')
    else:
        return render(request, 'login.html')


def sair(request):
    logout(request)
    return redirect('contato:inicio')

def cadastrarse(request):
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usu = User.objects.filter(username=email).first()            
        if usu is None:
            usu = User.objects.create_user(username=email, email=email, password=senha)
            usu.is_active = True
            usu.first_name = nome
            usu.save()
            return redirect('usuarios:entrar')
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastrese.html')
    else:
        return render(request, 'cadastrese.html')

def recuperarsenha(request):
    return render(request, 'recuperarsenha.html')