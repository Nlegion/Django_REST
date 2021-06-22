from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserModelSerializerV1, UserModelSerializerV2, UserModelSerializer
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, BasePermission


# Create your views here.
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserModelViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer


class UserModelViewSet1(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializerV1


class UserModelViewSet2(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializerV2


# permission_classes = [CustomPermission]


class CustomUserModelViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializerV1
