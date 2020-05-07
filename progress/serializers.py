from rest_framework import serializers
from .models import *
from course.api.serializers import CourseSerializer, TopicSerializer


class ProgressSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='lecture.topic', read_only=True)
    course_name = serializers.CharField(source='lecture.topic.course', read_only=True)
    lecture_name = serializers.CharField(source='lecture', read_only=True)
    student_name = serializers.CharField(source='student.username', read_only=True)
    duration = serializers.FloatField(source='lecture.duration', read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'student', 'lecture', 'completion', 'time_stamp', 'topic_name', 'course_name', 'lecture_name',
                  'student_name', 'duration']
        read_only_fields = ['time_stamp', 'lecture', 'student']
