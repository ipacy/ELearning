from django.db.models import Avg
from rest_framework import generics
from Dex.restconfig.userpermissions import *
from enrollment.models import *
from .serializers import EnrollSerializer, EnrollUpdateSerializer
from progress.models import Progress
from course.models import Lecture


def is_tutor(self):
    if self.request.user.groups.filter(name='tutor').__len__() > 0:
        return 0
    elif self.request.user.groups.filter(name='student').__len__() > 0:
        return 1


def perform_save_action(self, serializer):
    new_enrol = serializer.save(student=self.request.user)
    user = self.request.user
    lectures = Lecture.objects.filter(topic__course=new_enrol.course)
    for lecture in lectures:
        Progress.objects.create(lecture=lecture, student=user)
    return new_enrol


class EnrollList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EnrollSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.all()

        course = self.request.query_params.get('course')
        student = self.request.query_params.get('student')

        if course:
            queryset = queryset.filter(course=course)
        elif student:
            queryset = queryset.filter(student=student)

        if is_tutor(self) == 0:
            queryset = Enrollment.objects.filter(course__author=self.request.user)
        elif is_tutor(self) == 1:
            queryset = Enrollment.objects.filter(student=self.request.user)

        course = self.request.query_params.get('course')
        student = self.request.query_params.get('student')

        if course:
            queryset = queryset.filter(course=course)
        elif student:
            queryset = queryset.filter(student=student)

        return queryset


class EnrollDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = EnrollUpdateSerializer

    def get_queryset(self):
        queryset = Enrollment.objects.all()
        if is_tutor(self) == 0:
            queryset = Enrollment.objects.filter(course__author=self.request.user)
        elif is_tutor(self) == 1:
            queryset = Enrollment.objects.filter(student=self.request.user)

        return queryset

    def perform_update(self, serializer):
        enrollment_saved = serializer.save(student=self.request.user)
        course_object = enrollment_saved.course
        rating_records = Enrollment.objects.filter(course=course_object.id)
        course_rating = rating_records.aggregate(Avg('rating'))
        course_object.rating = course_rating['rating__avg']
        course_object.save()


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     serializer_class = UserSerializer
#     model = User
#
#     def get_serializer_class(self):
#         serializer_class = self.serializer_class
#
#         if self.request.method == 'PUT':
#             serializer_class = SerializerWithoutUsernameField
#
#         return serializer_class
#
#     def get_permissions(self):
#         if self.request.method == 'DELETE':
#             return [IsAdminUser()]
#         elif self.request.method == 'POST':
#             return [AllowAny()]
#         else:
#             return [IsStaffOrTargetUser()]
