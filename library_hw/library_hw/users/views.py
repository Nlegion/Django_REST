from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserModelSerializer
from rest_framework import mixins, viewsets


# Create your views here.

class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer
