from django.db import models
from .course_model import Course


class Topic(models.Model):
    title = models.CharField(max_length=300)
    duration = models.FloatField(max_length=300, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return '{}'.format(self.title)
