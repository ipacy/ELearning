from rest_framework import generics
from django.conf import settings
from Dex.restconfig.userpermissions import *
from course.models import *
from ..serializers.topic_serializers import TopicSerializer, TopicCreateSerializer


class TopicList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = TopicSerializer

    def get_queryset(self):
        queryset = Topic.objects.all()
        course = self.request.query_params.get('course')
        author = self.request.query_params.get('author')

        if course:
            queryset = queryset.filter(course=course)
        elif author:
            queryset = queryset.filter(course__author=author)

        return queryset


class TopicCreate(generics.CreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer


class TopicDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicCreateSerializer
