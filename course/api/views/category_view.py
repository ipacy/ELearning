from rest_framework import status, mixins, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from course.models import *
from ..serializers.course_serializers import CategorySerializer


class CategoryList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CategoryCreateList(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.AllowAny]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
