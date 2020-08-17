# Python imports
import json
from model_mommy import mommy

# DRF imports
from rest_framework import status
from rest_framework.test import force_authenticate, APIRequestFactory

# Django imports
from django.test import TestCase, Client
from django.urls import reverse

# App imports
from navedex_api.core.models import Naver, Project
from navedex_api.core.serializers import NaverSerializer, ProjectSerializer
from navedex_api.core.views import NaverViewSet, ProjectViewSet
from navedex_api.usuario.models import User

# API factory for requests of tests
factory = APIRequestFactory()


class ProjectViewsTest(TestCase):
    """ Project view testing module """
    def setUp(self):
        """ Test class settings """
        self.user = User.objects.create(
            email='test@test.com', password='testword'
        )
        self.user.is_active = True
        self.naver1 = mommy.make(Naver)
        self.naver2 = mommy.make(Naver)
        self.naver3 = mommy.make(Naver)

        self.projeto1 = Project.objects.create(
            name='Projeto 1',created_by=self.user
        )
        self.projeto1.navers.add(self.naver1, self.naver2)

        self.projeto2 = Project.objects.create(
            name='Projeto 2',created_by=self.user
        )
        self.projeto2.navers.add(self.naver2, self.naver3)

        self.projeto3 = Project.objects.create(
            name='Projeto 3',created_by=self.user
        )
        self.projeto3.navers.add(self.naver1, self.naver3)
    
    def test_create(self):
        """ Test creating objects by route """
        self.data = {
            'name': 'project_create',
            'navers': [self.naver2.pk]
        }
        request = factory.post('/project/', self.data)
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'post':'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_project(self):
        """ Return test of all objects """
        request = factory.get('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        projects = Project.objects.filter(created_by=self.user)
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_project(self):
        """ Return test for a specific object """
        request = factory.get('/project/',)
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        projects = Project.objects.get(pk=1)
        serializer = ProjectSerializer(projects)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_project_by_name(self):
        """ Filter test by object name """
        request = factory.get('/project/', {'name': 'project_create'})
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        projects = Project.objects.filter(name='project_create')
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update(self):
        """ Test updating objects by route """
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
        """ Testing for deleting objects by route """
        request = factory.delete('/project/')
        force_authenticate(request, user=self.user)
        view = ProjectViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class NaverViewsTest(TestCase):
    """ Naver view testing module """
    def setUp(self):
        """ Test class settings """
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
    
    def test_create(self):
        """ Test creating objects by route """
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

    def test_get_all_navers(self):
        """ Return test of all objects """
        request = factory.get('/naver/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        navers = Naver.objects.filter(created_by=self.user)
        serializer = NaverSerializer(navers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_naver(self):
        """ Return test for a specific object """
        request = factory.get('/naver/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'retrieve'})
        response = view(request, pk=1)
        naver = Naver.objects.get(pk=1)
        serializer = NaverSerializer(naver)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_navers_by_name(self):
        """ Filter test by object name """
        request = factory.get('/naver/', {'name': 'Gustavo'})
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        naver = Naver.objects.filter(name='Gustavo')
        serializer = NaverSerializer(naver, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_navers_by_admission_date(self):
        """ Filter test by admission date of objects """
        request = factory.get('/naver/', {'admission_date': '2020-1-15'})
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        naver = Naver.objects.filter(admission_date='2020-1-15')
        serializer = NaverSerializer(naver, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_navers_by_job_role(self):
        """ Filter test by object position """
        request = factory.get('/naver/', {'job_role': 'Django Developer'})
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({'get': 'list'})
        response = view(request)
        naver = Naver.objects.filter(job_role='Django Developer')
        serializer = NaverSerializer(naver, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update(self):
        """ Test updating objects by route """
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
        """ Testing for deleting objects by route """
        request = factory.delete('/project/')
        force_authenticate(request, user=self.user)
        view = NaverViewSet.as_view({"delete": "destroy"})
        response = view(request, pk=1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)