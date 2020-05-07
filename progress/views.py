from rest_framework import status, mixins, generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from Dex.restconfig.userpermissions import *

from .models import *
from .serializers import ProgressSerializer
from enrollment.models import Enrollment


class ProgressList(generics.ListCreateAPIView):
    serializer_class = ProgressSerializer

    def get_queryset(self):
        queryset = Progress.objects.filter(student=self.request.user)

        lecture = self.request.query_params.get('lecture')
        course = self.request.query_params.get('course')
        if lecture:
            queryset = queryset.filter(lecture=lecture)
        elif course:
            queryset = queryset.filter(lecture__course=course)

        return queryset


class ProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

    def perform_update(self, serializer):
        progress = serializer.save(student=self.request.user)
        course_object = progress.lecture.topic.course
        course_duration = course_object.duration
        progress_duration = progress.lecture.duration
        enroll_percentage = (progress_duration * 100) / course_duration
        enrolled_object = Enrollment.objects.filter(course=course_object.id, student=self.request.user.id)[0]
        enrolled_object.completion = enroll_percentage
        enrolled_object.save()
