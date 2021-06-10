from .models import Author, Biography, Article
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'authors']


class ArticleSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['first_name', 'last_name']


class ArticleSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
