from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from languages.fields import LanguageField


class Language(models.Model):
    language = LanguageField(max_length=200)

    def __str__(self):
        return '{}'.format(self.language)


class UserProfile(AbstractUser):
    biography = models.TextField(blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    language = models.ManyToManyField(Language)

    def __str__(self):
        return super().username
