"""Модуль разрешений для представлений приложения Api."""


from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Небезопасные методы HTTP разрешены только автору.

    В остальные случаях разрешены безопасные методы HTTP: GET, HEAD, OPTIONS.
    """
    def has_object_permission(self, request, view, obj):
        """Ограничение на уровне объекта."""
        if request.user.is_superuser:
            return True
        return request.method in SAFE_METHODS or obj.author == request.user


class IsAdmin(BasePermission):
    """Доступ разрешен только администратору,

    проверка на уровне представления.
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return (request.user.role is not None
                and request.user.role == 'admin')


class IsAdminOrReadOnly(BasePermission):
    """Небезопасные методы HTTP разрешены только администратору,

    проверка на уровне представления.
    """
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return (request.method in SAFE_METHODS
                or request.user.role is not None
                and request.user.role == 'admin')


class IsAuthorModeratorAdminOrReadonly(BaseException):
    """Небезопасные методы HTTP разрешены только

    автору, модератору или администратору.
    В остальные случаях разрешены безопасные методы HTTP: GET, HEAD, OPTIONS.
    """
    def has_object_permission(self, request, view, obj):
        """Ограничение на уровне объекта."""
        if request.user.is_superuser:
            return True
        return (request.method in SAFE_METHODS
                or (obj.author == request.user
                    or request.user.role is not None
                    and (request.user.role == 'moderator'
                         or request.user.role == 'admin')
                    )
                )