from rest_framework import permissions


class IsActive(permissions.BasePermission):
    """
    Класс для разрешения доступа только активным пользователям"
    """

    def has_permission(self, request, view):
        """
        Проверяет, является ли текущий пользователь активным
        """
        return request.user.is_active