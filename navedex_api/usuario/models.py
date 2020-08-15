# Importações Django
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Cria e salva o usuário com o email e senha.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e salva o usuário com o email e senha.
        """
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom model de usuário para que seja usado apenas email e senha como
    campos obrigatórios
    """
    email = models.EmailField('e-mail', unique=True)
    is_active = models.BooleanField('active', default=True, blank=True)
    is_staff = models.BooleanField('staff', default=True, blank=True)
    objects = UserManager()

    # Definição de nome de usuário como o email
    USERNAME_FIELD = 'email'

    class Meta:
        """
        Meta classe do model
        Define o nome no singular e no plural exibidos do model
        """
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        """Retorna o email do usuário."""
        return self.name