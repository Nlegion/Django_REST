import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserModelViewSet
from .models import CustomUser


class TestUserModelViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail(self):
        user = CustomUser.objects.create(email='django@django.net')
        client = APIClient()
        response = client.get(f'/api/Project/{user.email}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_guest(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', {'email': 'test_test@test_test.ru'}, format='json')
    #     view = UserModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_create_admin(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/users/', {'email': 'django@django.com'}, format='json')
    #     admin = User.objects.create_superuser('admin', 'django@django.com', 'geekbrains')
    #     force_authenticate(request, admin)
    #     view = UserModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


