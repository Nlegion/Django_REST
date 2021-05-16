from rest_framework.serializers import HyperlinkedModelSerializer

from .models import CustomUser


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',)
