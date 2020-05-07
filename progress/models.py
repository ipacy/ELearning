from django.db import models
from home.models import UserProfile
from course.models import Lecture
from django.core.validators import MaxValueValidator


class Progress(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, unique=False, related_name='progress')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, unique=False, related_name='progress')
    completion = models.IntegerField(choices=((1, 'True'), (2, "False")), default=2)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('student', 'lecture'), ]
