# Importações Python
from model_mommy import mommy

# Importações Django
from django.test import TestCase

# Importações da app
from navedex_api.core.models import Project, Naver
from navedex_api.usuario.models import User


class ProjectTest(TestCase):
    """ Módulo de testes do model Projeto """

    def setUp(self):
        """ Configurações da classe de testes """
        self.user = mommy.make(User)
        self.naver = mommy.make(Naver)
        self.project = Project.objects.create(name="projeto teste",
                                              created_by=self.user)
        self.project.navers.add(self.naver)

    def test_create(self):
        """ Teste de criação de objeto """
        self.assertTrue(Project.objects.exists())
    
    def test_str(self):
        """ Teste retorno str do objeto """
        self.assertEqual('projeto teste', str(self.project))


class NaverTest(TestCase):
    """ Módulo de testes do model Naver """

    def setUp(self):
        """ Configurações da classe de testes """
        self.user = mommy.make(User)
        self.naver = Naver.objects.create(name="gustavo guerra",
                                              birthdate='2020-1-15',
                                              job_role='Django developer',
                                              admission_date='2020-9-1',
                                              created_by=self.user)

    def test_create(self):
        """ Teste de criação de objeto """
        self.assertTrue(Naver.objects.exists())
    
    def test_str(self):
        """ Teste retorno str do objeto """
        self.assertEqual('gustavo guerra', str(self.naver))