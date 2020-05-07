from rest_framework import permissions
from rest_framework.permissions import (DjangoModelPermissions)
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.__module__ == 'course.models.lecture_model':
            auth_x = obj.topic.course.author
        elif obj.__module__ == 'course.models.topic_model':
            auth_x = obj.course.author
        else:
            auth_x = obj.author

        return auth_x == request.user or request.user.is_staff


class ReadDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%       (model_name)s']
