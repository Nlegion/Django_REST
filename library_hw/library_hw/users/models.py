from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    FULL = 9
    NORMAL = 5
    SIMPLE = 0

    RIGHTS_CHOICES = (
        (FULL, 'full'),
        (NORMAL, 'normal'),
        (SIMPLE, 'simple')
    )

    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    rights = models.PositiveIntegerField(choices=RIGHTS_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.email
