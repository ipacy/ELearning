from django.db import models
from .topic_model import Topic
from .course_model import Course
from home.models import UserProfile


def upload_lecture(instance, filename):
    return "lecture/{author}/{course}/{filename}".format(author=instance.topic.course.author.username,
                                                         course=instance.topic.course.title, filename=filename)


class Lecture(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=300, blank=True, null=True)
    duration = models.FloatField(max_length=300, blank=True, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='lectures')
    res_file = models.FileField(upload_to=upload_lecture, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
