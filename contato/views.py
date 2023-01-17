from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Contato
from django.contrib import messages

# Create your views here.
def index(request):
    lista = Contato.objects.all()
    return render(request, 'index.html', {'lista': lista})

def novo(request):
    if request.POST:
        n = str(request.POST.get('nome'))
        e = str(request.POST.get('email'))

        c = Contato(nome = n, email = e)
        c.save()
        return redirect('contato:inicio')
    else:    
        return render(request, 'novo.html')

def editar(request, i):
    try:
        c = Contato.objects.get(pk= i)
        if request.POST:
            n = str(request.POST.get('nome'))
            e = str(request.POST.get('email'))
            c.nome = n
            c.email = e
            
            c.save()
            messages.success(request, "Objeto salvo com sucesso")
            return redirect('contato:inicio')
        else:
            return render(request, 'editar.html', {'c': c})    
    except Exception as e:
        print(e)
        messages.error(request, 'Não foi possível editar o contato')
        return redirect('contato:inicio')
    
    
    

def excluir(request, i):
    try:
        c = Contato.objects.get(pk=i)        
        print(c)
        c.delete()
        return redirect('contato:inicio')
    except Exception as e:
        messages.error(request, 'Objeto não encontrado')
        return redirect('contato:inicio')



    