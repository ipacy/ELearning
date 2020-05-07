from rest_framework import status, mixins, generics, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from Dex.restconfig.userpermissions import *

from course.models import *
from ..serializers.course_serializers import CourseSerializer, CourseCreateSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        author = self.request.query_params.get('author')
        if author:
            queryset = queryset.filter(author=author)

        return queryset


class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        queryset = Course.objects.all()
        author = self.request.query_params.get('author')
        category = self.request.query_params.get('category')
        if author:
            queryset = queryset.filter(author=author)
        elif category:
            queryset = queryset.filter(category__title__icontains=category)

        return queryset


class CourseCreate(mixins.CreateModelMixin,
                   generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]

    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer

    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly, IsOwnerOrReadOnly]
