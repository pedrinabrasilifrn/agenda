from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate, login
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.models import User


# Create your views here.
def entrar(request):
    if request.POST:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        # Use a autenticação do Django
        usu = authenticate(email=email, password=senha)
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
        foto = None
        if 'foto' in  request.FILES:
            foto =  request.FILES['foto']
        usu = Usuario.objects.filter(email=email).first()            
        if usu is None:
            u = Usuario(nome=nome, email=email)
            u.set_password(senha)
            u.is_active = True
            u.foto = foto
            u.save()
            return redirect('usuarios:entrar')
        else:
            messages.error(request, "Usuário já cadastrado")
            return render(request, 'cadastrese.html')
    else:
        return render(request, 'cadastrese.html')

def recuperarsenha(request):
    return render(request, 'recuperarsenha.html')

def meuperfil(request):
    usu = Usuario.objects.filter(email=request.user.email).first()
    if request.POST:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        foto = None
        if 'foto' in  request.FILES:
            foto =  request.FILES['foto']
        

        if usu is not None:
            usu.nome = nome
            usu.email = email
            if foto is not None:
                usu.foto = foto
            usu.save()
            return redirect('usuarios:meuperfil')
        else:
            messages.error(request, "Usuário não cadastrado")
            return render(request, 'cadastrese.html')
    return render(request, 'meuperfil.html', {'usu':usu})

def altrarsenha(request):
    usu = Usuario.objects.filter(email=request.user.email).first()
    if request.POST:
        antiga = request.POST.get('senha_ant')
        nova = request.POST.get('senha_nova')
        if usu.check_password(antiga):  
            usu.set_password(nova)
            usu.save()
            messages.success(request, "Senha alterada com sucesso")
        else:
            messages.error(request, "Senha antiga inválida")
    return render(request, 'alterarsenha.html')