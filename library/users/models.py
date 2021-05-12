from django.db import models

# Create your models here.

class Users (models.Model):
    user_name = models.CharField(max_length=64, null=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(max_length=200,unique=True)

    def __str__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)