from rest_framework import serializers
from enrollment.models import *


class EnrollSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    course_name = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['completion', 'student', 'rating']


class EnrollUpdateSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    course_name = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['completion', 'student', 'course']
