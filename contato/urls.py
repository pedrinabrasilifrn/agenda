from django.urls import path
from . import views

app_name="contato"

urlpatterns=[
    path('', views.index, name="inicio"),
    path('novo', views.novo, name="novo"),
    path('editar/<int:i>/', views.editar, name="editar"),
    path('excluir/<int:i>/', views.excluir, name="excluir")
]