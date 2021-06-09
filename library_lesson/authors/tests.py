import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author, Book, Article, Bibliography


class TestAuthorViewSet(APITestCase):

    # def test_post(self):
    #     factory = APIRequestFactory()
    #     request = factory.post('/api/authors/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
    #     view = AuthorModelViewSet.as_view({'post': 'create'})
    #     response = view(request)
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_post_admin(self):
    #     User.objects.create_superuser('admin', 'admin@admin.com', 'qwerty')
    #     self.client.login(username='admin', password='qwerty')
    #     response = self.client.post('/api/authors/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(response.data.get('first_name'), 'Александр')
    #     self.client.logout()
    #     response = self.client.post('/api/authors/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_detail(self):
        bibliography = mixer.blend(Bibliography)
        # author = mixer.blend(Author, birthday_year=1799)
        # article = mixer.blend(Article, author__birthday_year=1799)
        # author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
        response = self.client.get(f'/api/article/{bibliography.article.id}/')
        print(response.data)
        response = self.client.get(f'/api/authors/{bibliography.article.author.id}/')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_edit_guest(self):
    #     author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
    #     client = APIClient()
    #     response = client.put(f'/api/authors/{author.id}/', {'name':'Грин', 'birthday_year': 1880})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def test_edit_admin(self):
    #     author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)# class TestAuthorViewSet(APITestCase):
#     def test_edit_guest(self):
#         # article = mixer.blend(Article, author__name='Грин')
#         author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
#         # client = APIClient()
#         response = self.client.put(f'/api/authors/{author.id}/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

#     client = APIClient()
#     admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
#     client.login(username='admin', password='admin123456')
#     response = client.put(f'/api/authors/{author.id}/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
#     self.assertEqual(response.status_code, status.HTTP_200_OK)
#     author = Author.objects.get(id=author.id)
#     self.assertEqual(author.last_name, 'Грин')
#     self.assertEqual(author.birthday_year, 1880)
#     client.logout()

# class TestMath(APISimpleTestCase):
#     def test_sqrt(self):
#         import math
#         self.assertEqual(math.sqrt(4), 2)


# class TestAuthorViewSet(APITestCase):
#     def test_edit_guest(self):
#         # article = mixer.blend(Article, author__name='Грин')
#         author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
#         # client = APIClient()
#         response = self.client.put(f'/api/authors/{author.id}/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# def test_edit_guest(self):
#     #     author = Author.objects.create(first_name='Александр', last_name='Пушкин', birthday_year=1799)
#     # client = APIClient()
#     response = self.client.post(f'/api/authors/', {'first_name': 'Александр', 'last_name': 'Грин', 'birthday_year': 1880})
#     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     author = Author.objects.get(id=response.data.get('id'))
#     print(author.last_name)
