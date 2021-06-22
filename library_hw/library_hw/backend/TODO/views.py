from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import mixins, viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import *
from rest_framework.authtoken.models import Token


# Create your views here.


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    page_size = 20


class TODOLimitOffsetPagination(LimitOffsetPagination):
    page_size = 10


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes =  [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    page_size = ProjectLimitOffsetPagination

    def get_queryset(self):
        name = self.request.query_params.get('title', '')
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project


@api_view(['GET'])
def project_view(request):
    token = Token.objects.filter(key=request.headers)
    token.delete()


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer
    page_size = TODOLimitOffsetPagination

    # renderer_classes =  [JSONRenderer, BrowsableAPIRenderer]

    def offline(self, request, pk=None):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
