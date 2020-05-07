from django.contrib import admin

from .models import *


class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'lecture', 'completion', 'time_stamp')


admin.site.register(Progress, ProgressAdmin)
