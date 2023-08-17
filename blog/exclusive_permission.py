from rest_framework.permissions import BasePermission
from django.http import HttpRequest
from .models import Article


class IsSuperUser(BasePermission):
    def has_permission(self, request: HttpRequest, view):
        return bool(
            request.user.is_superuser
        )


class IsAuthorOrAdmin(BasePermission):

    def has_object_permission(self, request: HttpRequest, view, obj: Article):
        return bool(
            request.user.is_superuser or
            (obj.author.user == request.user)
        )
