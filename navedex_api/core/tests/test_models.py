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
        self.project = Project.objects.create(
            name="projeto teste", created_by=self.user
            )
        self.project.navers.add(self.naver)

    def test_create(self):
        """ Teste de criação de objeto """
        self.assertTrue(Project.objects.exists())
    
    def test_str(self):
        """ Teste retorno str do objeto """
        self.assertEqual('projeto teste', str(self.project))

    def test_name_can_not_be_blank(self):
        field = Project._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_name_can_not_be_null(self):
        field = Project._meta.get_field('name')
        self.assertFalse(field.null)
    
    def test_naver_can_be_blank(self):
        field = Project._meta.get_field('navers')
        self.assertTrue(field.blank)

    def test_naver_can_not_be_null(self):
        field = Project._meta.get_field('navers')
        self.assertFalse(field.null)
    
    def test_created_by_can_not_be_blank(self):
        field = Project._meta.get_field('created_by')
        self.assertFalse(field.blank)

    def test_created_by_can_not_be_null(self):
        field = Project._meta.get_field('created_by')
        self.assertFalse(field.null)


class NaverTest(TestCase):
    """ Módulo de testes do model Naver """

    def setUp(self):
        """ Configurações da classe de testes """
        self.user = mommy.make(User)
        self.naver = Naver.objects.create(
            name="gustavo guerra", birthdate='2020-1-15', created_by=self.user,
            job_role='Django developer', admission_date='2020-9-1'
            )

    def test_create(self):
        """ Teste de criação de objeto """
        self.assertTrue(Naver.objects.exists())
    
    def test_str(self):
        """ Teste retorno str do objeto """
        self.assertEqual('gustavo guerra', str(self.naver))
    
    def test_name_can_not_be_blank(self):
        field = Naver._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_name_can_not_be_null(self):
        field = Naver._meta.get_field('name')
        self.assertFalse(field.null)
    
    def test_birthdate_can_not_be_blank(self):
        field = Naver._meta.get_field('birthdate')
        self.assertFalse(field.blank)

    def test_birthdate_can_not_be_null(self):
        field = Naver._meta.get_field('birthdate')
        self.assertFalse(field.null)
    
    def test_job_role_can_not_be_blank(self):
        field = Naver._meta.get_field('job_role')
        self.assertFalse(field.blank)

    def test_job_role_can_not_be_null(self):
        field = Naver._meta.get_field('job_role')
        self.assertFalse(field.null)
    
    def test_admission_date_can_not_be_blank(self):
        field = Naver._meta.get_field('admission_date')
        self.assertFalse(field.blank)

    def test_admission_date_can_not_be_null(self):
        field = Naver._meta.get_field('admission_date')
        self.assertFalse(field.null)

    def test_created_by_can_not_be_blank(self):
        field = Naver._meta.get_field('created_by')
        self.assertFalse(field.blank)

    def test_created_by_can_not_be_null(self):
        field = Naver._meta.get_field('created_by')
        self.assertFalse(field.null)