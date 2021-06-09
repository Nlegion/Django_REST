import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import ProjectModelViewSet, TODOViewSet
from .models import Project, TODO

class TestProjectModelViewSet(TestCase):
    def test_get_detail(self):
        project = Project.objects.create(title='Титл', users='django@django.net', link='https://gb.ru/')
        client = APIClient()
        response = client.get(f'/api/Project/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# def test_edit_guest(self):
#     project = Project.objects.create(title='Титл', users='django@django.net', link='https://gb.ru/')
#     client = APIClient()
#     response = client.put(f'/api/authors/{project.id}/', {'name': 'Грин', 'birthday_year': 1880})
#     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class TestTODOViewSet(APITestCase):

    def test_get_list(self):
        response = self.client.get('/api/ToDo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)