from rest_framework.generics import *
from rest_framework.mixins import *
from rest_framework.viewsets import *
from .models import Author, Biography, Book, Article
from .serializers import *
from rest_framework.renderers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import *


# Create your views here.
#
# class AuthorModelViewSet(ModelViewSet):
#     # renderer_classes =  [JSONRenderer, BrowsableAPIRenderer]
#     queryset = Author.objects.all()
#     serializer_class = AuthorModelSerializer
#
#
# class BiographyModelViewSet(ModelViewSet):
#     queryset = Biography.objects.all()
#     serializer_class = BiographySerializer
#
#
# class BookModelViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# # class ArticleModelViewSet(ModelViewSet):
# #     queryset = Article.objects.all()
# #     serializer_class = ArticleSerializer
#
#
# class ArticleListModelView(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # class ArticleModelViewSet(CreateModelMixin,ListModelMixin, RetrieveModelMixin, GenericViewSet ):
# #     queryset = Article.objects.all()
# #     serializer_class = ArticleSerializer
#
# class ArticleModelViewSet(ModelViewSet):
#     def list(self, request):
#         articles = Article.objects.all()
#         serializers = ArticleSerializer(articles, many=True)
#         return Response(serializers.data)
#
#     def retrieve(self, request, pk=None):
#         article = get_object_or_404(Article, pk=pk)
#         serializers = ArticleSerializer(article)
#         return Response(serializers.data)
#
#     @action(detail=True, methods=['GET'])
#     def article_name(self, request, pk=None):
#         article = get_object_or_404(Article, pk=pk)
#         return Response({'name': article.name})
#
#
# class ArticleCreateModelView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleCreateModelView(UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleRetrieveModelView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# # class ArticleModelView(APIView):
# # def get(self, request):
# #     articles = Article.objects.all()
# #     serializers = ArticleSerializer(articles, many=True)
# #     return Response(serializers.data)
#
# @api_view(['GET'])
# def article_view(request):
#     articles = Article.objects.all()
#     serializers = ArticleSerializer(articles, many=True)
#     return Response(serializers.data)

class ArticleModelViewSet(ModelViewSet):
    # queryset = Article.objects.all()
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['id']

    # def get_queryset(self):
    #     id_ = self.request.query_params.get('id')
    #     if id_ is not None:
    #         return Article.objects.filter(id=self.request.query_params.get('id'))
    #     else:
    #         return Article.objects.all()
