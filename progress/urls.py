from django.urls import path, include
from .views import *
from rest_framework import renderers

urlpatterns = [
    path('progress/', ProgressList.as_view()),
    path('progress/<int:pk>/', ProgressDetail.as_view()),
]
