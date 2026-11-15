from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Разрешение для модераторов.
    Проверяет, состоит ли пользователь в группе 'Модераторы'.
    """
    def has_permission(self, request, view):
        # Проверяем, авторизован ли пользователь и есть ли он в группе
        return request.user.is_authenticated and request.user.groups.filter(name='Модераторы').exists()


class IsOwner(permissions.BasePermission):
    """
    Разрешение для владельцев объектов.
    Разрешает доступ только если пользователь является владельцем объекта (obj.owner == request.user).
    """
    def has_object_permission(self, request, view, obj):
        # Для безопасности проверяем, что у объекта есть атрибут owner
        if hasattr(obj, 'owner'):
            return obj.owner == request.user
        return False