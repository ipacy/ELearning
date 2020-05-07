from django.db import models
from home.models import UserProfile
from course.models import Course
from django.core.validators import MaxValueValidator, MinValueValidator


class EnrollManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(student=self.sup)


class Enrollment(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE, unique=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, unique=False)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, null=True,
                                       default=0)
    enroll_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    completion = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)], blank=True, null=True,
                                   default=0)

    class Meta:
        unique_together = [('student', 'course'), ]
