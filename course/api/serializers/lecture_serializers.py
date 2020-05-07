from rest_framework import serializers
from course.models import *


class LectureSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.author.username', read_only=True)
    course_name = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Lecture
        fields = '__all__'


class LectureCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.author.username', read_only=True)

    class Meta:
        model = Lecture
        fields = '__all__'
