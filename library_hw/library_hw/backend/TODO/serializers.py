from .models import *
from rest_framework.serializers import ModelSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TODOSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
