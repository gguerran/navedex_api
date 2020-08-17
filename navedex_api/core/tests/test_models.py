# Python imports
from model_mommy import mommy

# Django imports
from django.test import TestCase

# App imports
from navedex_api.core.models import Project, Naver
from navedex_api.usuario.models import User


class ProjectTest(TestCase):
    """ Project model testing module """

    def setUp(self):
        """ Test class settings """
        self.user = mommy.make(User)
        self.naver = mommy.make(Naver)
        self.project = Project.objects.create(
            name="projeto teste", created_by=self.user
            )
        self.project.navers.add(self.naver)

    def test_create(self):
        """ Project creation test """
        self.assertTrue(Project.objects.exists())
    
    def test_str(self):
        """ Test str object return """
        self.assertEqual('projeto teste', str(self.project))

    def test_name_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = Project._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_name_cannot_be_null(self):
        """ Test name cannot be null """
        field = Project._meta.get_field('name')
        self.assertFalse(field.null)
    
    def test_navers_can_be_blank(self):
        """ Test navers can be blank """
        field = Project._meta.get_field('navers')
        self.assertTrue(field.blank)

    def test_naver_can_not_be_null(self):
        """ Test navers cannot be null """
        field = Project._meta.get_field('navers')
        self.assertFalse(field.null)
    
    def test_created_by_cannot_be_blank(self):
        """ Test created_by cannot be blank """
        field = Project._meta.get_field('created_by')
        self.assertFalse(field.blank)

    def test_created_by_can_not_be_null(self):
        """ Test created_by cannot be null """
        field = Project._meta.get_field('created_by')
        self.assertFalse(field.null)


class NaverTest(TestCase):
    """ Naver model testing module """

    def setUp(self):
        """ Test class settings"""
        self.user = mommy.make(User)
        self.naver = Naver.objects.create(
            name="gustavo guerra", birthdate='2020-1-15', created_by=self.user,
            job_role='Django developer', admission_date='2020-9-1'
            )

    def test_create(self):
        """ Project creation test """
        self.assertTrue(Naver.objects.exists())
    
    def test_str(self):
        """ Test str object return """
        self.assertEqual('gustavo guerra', str(self.naver))
    
    def test_name_cannot_be_blank(self):
        """ Test name cannot be blank """
        field = Naver._meta.get_field('name')
        self.assertFalse(field.blank)

    def test_name_cannot_be_null(self):
        """ Test name cannot be null """
        field = Naver._meta.get_field('name')
        self.assertFalse(field.null)
    
    def test_birthdate_cannot_be_blank(self):
        """ Test birthdate cannot be blank """
        field = Naver._meta.get_field('birthdate')
        self.assertFalse(field.blank)

    def test_birthdate_cannot_be_null(self):
        """ Test birthdate cannot be null """
        field = Naver._meta.get_field('birthdate')
        self.assertFalse(field.null)
    
    def test_job_role_can_not_be_blank(self):
        """ Test job_role cannot be blank """
        field = Naver._meta.get_field('job_role')
        self.assertFalse(field.blank)

    def test_job_role_cannot_be_null(self):
        """ Test job_role cannot be null """
        field = Naver._meta.get_field('job_role')
        self.assertFalse(field.null)
    
    def test_admission_date_cannot_be_blank(self):
        """ Test admission_date cannot be blank """
        field = Naver._meta.get_field('admission_date')
        self.assertFalse(field.blank)

    def test_admission_date_cannot_be_null(self):
        """ Test admission_date cannot be null """
        field = Naver._meta.get_field('admission_date')
        self.assertFalse(field.null)

    def test_created_by_cannot_be_blank(self):
        """ Test created_by cannot be blank """
        field = Naver._meta.get_field('created_by')
        self.assertFalse(field.blank)

    def test_created_by_cannot_be_null(self):
        """ Test created_by cannot be null """
        field = Naver._meta.get_field('created_by')
        self.assertFalse(field.null)