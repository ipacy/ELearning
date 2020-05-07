from rest_framework import serializers
from course.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    lang = serializers.CharField(source='get_language_display', read_only=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['author', 'rating']


class CourseCreateSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    lang = serializers.CharField(source='get_language_display', read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['author', 'duration', 'rating']
