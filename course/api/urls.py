from django.urls import path, include
from .views import *
from rest_framework import renderers

user_list = UserViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('categories/', CategoryList .as_view()),

    path('courses/', CourseList.as_view()),
    path('courses/create/', CourseCreate.as_view()),
    path('courses/<int:pk>/', CourseDetail.as_view()),

    path('topics/', TopicList.as_view()),
    path('topics/create/', TopicCreate.as_view()),
    path('topics/<int:pk>/', TopicDetail.as_view()),

    path('lectures/', LectureList.as_view()),
    path('lectures/create/', LectureCreate.as_view()),
    path('lectures/<int:pk>/', LectureDetail.as_view()),

    path('xxx/', user_list, name='user-list'),

    path('nested/', NestedTopicList.as_view()),
    path('nested/create/', NestedTopicCreate.as_view()),
]
