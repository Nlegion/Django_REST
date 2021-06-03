from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .serializers import UserModelSerializer
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
    # permission_classes = [CustomPermission]
