from django.db import models
from languages.fields import LanguageField
from home.models import UserProfile
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300, blank=True, null=True)

    def __str__(self):
        return 'id{} title{}'.format(self.id, self.title)


def upload_lecture(instance, filename):
    return "lecture/{author}/{course}/{filename}".format(author=instance.author.username,
                                                         course=instance.title, filename=filename)


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300, blank=True, null=True)
    duration = models.FloatField(max_length=300, blank=True, null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, null=True,
                                 default=0)
    ico = models.FileField(upload_to=upload_lecture, blank=True, null=True)
    language = LanguageField(max_length=20, default='en')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'id{} title{}'.format(self.id, self.title)
