from django.contrib import admin

from .models import *


class EnrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'enroll_date', 'completion')


admin.site.register(Enrollment, EnrollAdmin)
