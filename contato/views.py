from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Contato
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    lista = Contato.objects.all()
    return render(request, 'index.html', {'lista': lista})

@login_required(login_url="/usuarios/entrar")
def novo(request):
    if request.POST:
        n = str(request.POST.get('nome'))
        e = str(request.POST.get('email'))
        i =  request.FILES['imagem']

        c = Contato(nome = n, email = e, imagem=i)
        c.save()
        return redirect('contato:inicio')
    else:    
        return render(request, 'novo.html')


@login_required(login_url="/usuarios/entrar")
def editar(request, i):
    try:
        c = Contato.objects.get(pk= i)
        if request.POST:
            n = str(request.POST.get('nome'))
            e = str(request.POST.get('email'))
            i = request.FILES['imagem']
            c.nome = n
            c.email = e
            if i != "":
                c.imagem = i
            c.save()
            messages.success(request, "Objeto salvo com sucesso")
            return redirect('contato:inicio')
        else:
            return render(request, 'editar.html', {'c': c})    
    except MultiValueDictKeyError  as e:
        messages.success(request, "Objeto salvo com sucesso")
        return redirect('contato:inicio')
    except Exception as e:
        messages.error(request, "Objeto não salvo")
        return redirect('contato:inicio')
    
@login_required(login_url="/usuarios/entrar")
def excluir(request, i):
    try:
        c = Contato.objects.get(pk=i)        
        print(c)
        c.delete()
        return redirect('contato:inicio')
    except Exception as e:
        messages.error(request, 'Objeto não encontrado')
        return redirect('contato:inicio')



    