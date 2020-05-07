from rest_framework import serializers
from course.models import *


class TopicSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='course.author.username', read_only=True)
    author_id = serializers.IntegerField(source='course.author.id', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
        # read_only_fields = ['author']


class TopicCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = '__all__'
        # read_only_fields = ['author']
