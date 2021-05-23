from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Biography, Article, Book
from rest_framework import serializers


class AuthorModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Biography
        fields = ['text', 'authors']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        fields = '__all__'

    def create(self, validated_data):
        author = Author.objects.create(validated_data['authors'])
        article = Article(name=validated_data['name'], authors=author)
        article.authors = author
        article.save()
        return article


class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'
