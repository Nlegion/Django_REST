from rest_framework.serializers import HyperlinkedModelSerializer
from .models import *
from users.serializers import UserModelSerializer
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        project = Project
        fields = '__all__'


class TODOSerializer(serializers.ModelSerializer):
    author = UserModelSerializer()

    class Meta:
        todo = TODO
        fields = '__all__'
