# Dango imports
from django.db import models


class Naver(models.Model):
    """
    Model Naver.
    """
    name = models.CharField(verbose_name='Nome', max_length=100)
    birthdate = models.DateField(verbose_name='Data de nascimento')
    job_role = models.CharField(verbose_name='Cargo', max_length=50)
    admission_date = models.DateField(verbose_name='Data de admissão')
    created_by = models.ForeignKey(
        'usuario.User', on_delete=models.CASCADE, verbose_name='criado por'
    )
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='Modificado em', auto_now=True
    )

    class Meta:
        """
        Meta model class
        Defines the displayed singular and plural name of the model
        """
        verbose_name = "naver"
        verbose_name_plural = "navers"

    def __str__(self):
        """ Returns the name of the naver. """
        return self.name


class Project(models.Model):
    """
    Model Project.
    """
    name = models.CharField(verbose_name='Nome', max_length=100)
    navers = models.ManyToManyField(
        'core.Naver', verbose_name='Navers', blank=True,
        related_name='projects'
    )
    created_by = models.ForeignKey(
        'usuario.User', on_delete=models.CASCADE, verbose_name='criado por'
    )
    created = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Modificado em', auto_now=True)

    class Meta:
        """
        Meta model class
        Defines the displayed singular and plural name of the model and the
        default listing order
        """
        verbose_name = "projeto"
        verbose_name_plural = "projetos"
        ordering = ('name',)

    def __str__(self):
        """ Returns the name of the project. """
        return self.name