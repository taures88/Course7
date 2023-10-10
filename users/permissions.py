from rest_framework.permissions import BasePermission

from users.models import UserRoles

"""класс проверки входа администратора"""


class IsAdmin(BasePermission):
    message = "Вы не являетесь администратором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.admin:
            return True
        return False


"""класс проверки входа владельца(пользователя)"""


class IsOwner(BasePermission):
    message = 'Вы не являетесь владельцем!'

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
