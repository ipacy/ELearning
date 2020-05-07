from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'rating', 'duration', 'author', 'price', 'pub_date')


admin.site.register(Course, CourseAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')


admin.site.register(Category, CategoryAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duration', 'pub_date', 'course')


admin.site.register(Topic, TopicAdmin)


class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'duration', 'topic')


admin.site.register(Lecture, LectureAdmin)
# admin.site.register(Enroll)
