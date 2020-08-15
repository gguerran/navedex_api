# Importações Python
import json
from model_mommy import mommy

# Importações DRF
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory

# Importações Django
from django.test import TestCase, Client
from django.urls import reverse

# Importações da app
from navedex_api.core.models import Naver, Project
from navedex_api.core.serializers import NaverSerializer, ProjectSerializer
from navedex_api.core.views import NaverViewSet, ProjectViewSet
from navedex_api.usuario.models import User

# API factory para as requests dos tests
factory = APIRequestFactory()


class ProjectViewsTest(TestCase):
    """ Módulo de testes do model Projeto """
    def setUp(self):
        """ Configurações da classe de testes """
        self.user = User.objects.create(
            email='test@test.com', password='testword'
        )
        self.user.is_active = True
        self.naver1 = mommy.make(Naver)
        self.naver2 = mommy.make(Naver)
        self.naver3 = mommy.make(Naver)
        
        projeto1 = Project.objects.create(
            name='Projeto 1',created_by=self.user
        )
        projeto1.navers.add(self.naver1, self.naver2)

        projeto2 = Project.objects.create(
            name='Projeto 2',created_by=self.user
        )
        projeto2.navers.add(self.naver2, self.naver3)

        projeto3 = Project.objects.create(
            name='Projeto 3',created_by=self.user
        )
        projeto3.navers.add(self.naver1, self.naver3)

    def test_get_all_project(self):
        """ Teste de retorno de todos os objetos """
        request = factory.get('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_project(self):
        """ Teste de retorno de um objeto específico """
        request = factory.get('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_project_by_name(self):
        """ Teste de filtro por nome dos objetos """
        request = factory.get('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request, name='Projeto%203')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        """ Teste de criação objetos pela rota """
        data = {
            'name': 'project_create',
            'navers': [self.naver2.pk]
        }
        request = factory.post('/project/', data)
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update(self):
        """ Teste de atualização objetos pela rota """
        data = {
            'name': 'project_update',
            'navers': [self.naver1.pk]
        }
        request = factory.post('/project/', data)
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'post':'update'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """ Teste de exclusão objetos pela rota """
        request = factory.delete('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class NaverViewsTest(TestCase):
    """ Módulo de testes do model Navers """
    def setUp(self):
        """ Configurações da classe de testes """
        self.user = User.objects.create(
            email='test@test.com', password='testword'
        )
        self.user.is_active = True
        Naver.objects.create(
            name='Gustavo', birthdate="1997-1-10", job_role="Django Developer",
            admission_date="2020-08-25", created_by=self.user
        )
        Naver.objects.create(
            name='Mateus', birthdate="1997-2-12", job_role="Frontend Developer",
             admission_date="2019-07-23", created_by=self.user
        )
        Naver.objects.create(
            name='Marcos', birthdate="1997-3-13", job_role="Backend Developer",
            admission_date="2020-01-15", created_by=self.user
        )

        Project.objects.create(name='test project',created_by=self.user)

    def test_get_all_navers(self):
        """ Teste de retorno de todos os objetos """
        request = factory.get('/naver/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        navers = Naver.objects.all()
        serializer = NaverSerializer(navers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_naver(self):
        """ Teste de retorno de um objeto específico """
        request = factory.get('/naver/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_navers_by_name(self):
        """ Teste de filtro por nome dos objetos """
        request = factory.get('/naver/?name=Gustavo')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_navers_by_admission_date(self):
        """ Teste de filtro por data de admissão dos objetos """
        request = factory.get('/naver/?admission_date=2020-1-15')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_navers_by_job_role(self):
        """ Teste de filtro por cargo dos objetos """
        request = factory.get('/naver/?job_role?Django%20Developer')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self):
        """ Teste de criação objetos pela rota """
        data = {
            "name": "Gustavo",
            "birthdate": "1997-2-15",
            "job_role": "Django Developer",
            "admission_date": "2020-8-25",
            "projects": ["1"]
        }
        request = factory.post('/naver/', data)
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_update(self):
        """ Teste de atualização objetos pela rota """
        data = {
            "name": "Gustavo",
            "birthdate": "1997-2-15",
            "job_role": "Django Developer",
            "admission_date": "2020-8-25",
            "projects": ["1"]
        }
        request = factory.post('/project/', data)
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'post':'update'})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        """ Teste de exclusão objetos pela rota """
        request = factory.delete('/project/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)