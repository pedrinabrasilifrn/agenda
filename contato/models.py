from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=250)
    email = models.EmailField()
    imagem = models.ImageField(upload_to = "contatos/", null=True)
    def __str__(self):
        return self.nome