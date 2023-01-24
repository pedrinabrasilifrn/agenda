from django.urls import path
from . import views

app_name="usuarios"

urlpatterns = [
    path("entrar", views.entrar, name="entrar"),
    path("sair", views.sair, name="sair"),
    path("cadastrese", views.cadastrarse, name="cadastrese"),
    path("recuperarsenha", views.recuperarsenha, name="recuperarsenha")
]