from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework import serializers
from .models import CustomUser

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', ]

class UserModelSerializerV1(HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', ]

class UserModelSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
