from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает просмотр (GET) любому авторизованному пользователю.
    Редактирование и удаление (PUT, PATCH, DELETE) — только владельцу профиля.
    """
    def has_object_permission(self, request, view, obj):
        # Чтение разрешено всем авторизованным (по умолчанию глобальный IsAuthenticated)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Редактирование разрешено только самому пользователю
        return obj == request.user