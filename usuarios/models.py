from django.db import models
from django.core import validators
import re
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Create your models here.
class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="usuarios")
    email = models.EmailField('E-mail', unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'O e-mail não pode conter espaços', 'invalid')])
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É administrador?', blank=True, default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
   