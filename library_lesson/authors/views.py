from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.viewsets import *
from rest_framework.permissions import AllowAny, BasePermission
from .models import Author, Biography, Book, Article
from .serializers import *
from rest_framework.renderers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import *
from rest_framework.authtoken.models import Token


# Create your views here.
#

class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [CustomPermission]


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(['GET'])
def article_view(request):
    token = Token.objects.filter(key=request.headers)
    token.delete()
