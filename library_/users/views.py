from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersModelSerializer


# Create your views here.

class UsersModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
