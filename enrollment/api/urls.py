from django.urls import path, include
from .views import EnrollList, EnrollDetail

urlpatterns = [
    path('enrolls/', EnrollList.as_view()),
    path('enrolls/<int:pk>/', EnrollDetail.as_view()),
]
