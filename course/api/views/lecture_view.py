from django.db.models import Sum
from rest_framework import status, mixins, generics, permissions
from rest_framework.permissions import IsAuthenticated

from Dex.restconfig.userpermissions import *
from course.models import *
from ..serializers.lecture_serializers import LectureSerializer, LectureCreateSerializer


class LectureList(generics.ListAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.all()
        course = self.request.query_params.get('course')
        author = self.request.query_params.get('author')
        topic = self.request.query_params.get('topic')
        if course:
            queryset = queryset.filter(course=course)
        elif author:
            queryset = queryset.filter(course__author=author)
        elif topic:
            queryset = queryset.filter(topic=topic)
        return queryset


def perform_duration_action(self, serializer):
    new_lecture = serializer.save()
    lectures_by_author = Lecture.objects.filter(topic__course__author=self.request.user)
    lectures_duration = lectures_by_author.aggregate(Sum('duration'))
    new_lecture.topic.course.duration = lectures_duration['duration__sum']
    new_lecture.topic.course.save()


class LectureCreate(generics.CreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Lecture.objects.all()
    serializer_class = LectureCreateSerializer

    def perform_create(self, serializer):
        perform_duration_action(self, serializer)


class LectureDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
    queryset = Lecture.objects.all()
    serializer_class = LectureCreateSerializer

    def perform_update(self, serializer):
        perform_duration_action(self, serializer)
