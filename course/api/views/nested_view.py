from rest_framework import generics

from Dex.restconfig.userpermissions import *
from course.models import *
from ..serializers.nested_serializers import TopicBatchSerializer


class NestedTopicList(generics.ListAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = TopicBatchSerializer

    # queryset = Topic.objects.all()

    def get_queryset(self):
        queryset = Topic.objects.all()
        course = self.request.query_params.get('course')
        if course:
            queryset = queryset.filter(course=course)

        return queryset


class NestedTopicCreate(generics.CreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicBatchSerializer
