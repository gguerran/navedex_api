# Django imports
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    """
    User management class
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """ Create and save the user with the email and password. """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """ Create and save the user with the email and password. """
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model so that only email and password are used as required
    fields
    """
    email = models.EmailField('e-mail', unique=True)
    is_active = models.BooleanField('active', default=True, blank=True)
    is_staff = models.BooleanField('staff', default=True, blank=True)
    objects = UserManager()

    # Setting username as email
    USERNAME_FIELD = 'email'

    class Meta:
        """
        Model Meta class
        Defines the displayed singular and plural name of the model
        """
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    
    def __str__(self):
        """ Returns the user's email. """
        return self.email