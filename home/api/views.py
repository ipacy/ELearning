from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.http import Http404
from rest_framework import status, mixins, generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import *
from .serializers import UserProfileSerializer

class UserList(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    def get_queryset(self):
        queryset = UserProfile.objects.filter(username=self.request.user)
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)

        return queryset

class UserList1(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request, format=None):
        articles = UserProfile.objects.all()
        serializer = UserProfileSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMixinList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [permissions.AllowAny]
    permission_classes = [permissions.DjangoModelPermissions]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        queryset = UserProfile.objects.filter(username=self.request.user)
        username = self.request.query_params.get('username')
        if username:
            queryset = queryset.filter(username=username)

        return queryset

class UserMixinDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
