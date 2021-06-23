from django.urls import path
from .views import AuthorModelViewSet

app_name = 'authors'
urls = [
    path('', AuthorModelViewSet.as_view({'get': 'list'}))
]
