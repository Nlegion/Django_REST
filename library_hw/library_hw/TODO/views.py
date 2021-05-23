from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer,HTMLFormRenderer, BrowsableAPIRenderer


# Create your views here.

class ProjectModelViewSet(ModelViewSet):
    #renderer_classes =  [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TODOViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializer

