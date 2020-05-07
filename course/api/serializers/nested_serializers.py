from rest_framework import serializers
from course.models import *
from django.db.models import Sum


class LectureBatchSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Lecture
        fields = ['id','title', 'duration', 'duration', 'author_name']


class TopicBatchSerializer(serializers.ModelSerializer):
    lectures = LectureBatchSerializer(many=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'duration', 'course', 'lectures']

    def create(self, validated_data):
        lectures_data = validated_data.pop('lectures')
        topic = Topic.objects.create(**validated_data)
        for lecture_data in lectures_data:
            Lecture.objects.create(topic=topic, **lecture_data)

        lecture_author = Lecture.objects.filter(topic__course__author=topic.course.author)
        lec_total = lecture_author.aggregate(Sum('duration'))
        topic.course.duration = lec_total['duration__sum']
        topic.course.save()
        return topic
