from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


class Biography(models.Model):
    text = models.TextField()
    authors = models.OneToOneField(Author, on_delete=models.CASCADE)


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ForeignKey(Author, models.PROTECT)
