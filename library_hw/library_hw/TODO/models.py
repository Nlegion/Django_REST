from django.db import models
from django.contrib.auth.models import AbstractUser

import users.models
from users.models import CustomUser


# Create your models here.

class Project(models.Model):
    FULL = 9
    NORMAL = 5
    SIMPLE = 0

    RIGHTS_CHOICES = (
        (FULL, 'full'),
        (NORMAL, 'normal'),
        (SIMPLE, 'simple')
    )

    title = models.CharField(max_length=64, unique=True)
    link = models.TextField()
    project_rights = models.PositiveIntegerField(choices=RIGHTS_CHOICES, blank=True, null=True)
    author = users.models.CustomUser.email

    def __str__(self):
        return self.title


class TODO(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = Project.title
    text_fields = models.TextField()
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    author = users.models.CustomUser.email
