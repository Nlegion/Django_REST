from django.db import models
from django.contrib.auth.models import AbstractUser

from users.models import CustomUser


# Create your models here.

class Project(models.Model):
    # FULL = 9
    # NORMAL = 5
    # SIMPLE = 0
    #
    # RIGHTS_CHOICES = (
    #     (FULL, 'full'),
    #     (NORMAL, 'normal'),
    #     (SIMPLE, 'simple')
    # )

    title = models.CharField(max_length=64, unique=True)
    users = models.ManyToManyField(CustomUser)
    link = models.URLField(blank=True)

    # project_rights = models.PositiveIntegerField(choices=RIGHTS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title


class TODO(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text_fields = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

