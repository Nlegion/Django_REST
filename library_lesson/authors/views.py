from rest_framework.viewsets import ModelViewSet
from .models import Author, Biography, Book, Article
from .serializers import *
from rest_framework.renderers import JSONRenderer,HTMLFormRenderer, BrowsableAPIRenderer


# Create your views here.

class AuthorModelViewSet(ModelViewSet):
    renderer_classes =  [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
