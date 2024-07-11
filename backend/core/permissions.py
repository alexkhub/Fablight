from rest_framework import permissions


class UserObjectPermission(permissions.BasePermission):
    '''Проверка ролей пользователя'''
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id or request.user.is_staff:
            return True
        return False