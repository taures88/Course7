from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView

from users.models import User
from users.serializers import UserSerializer

""" Список пользователей """


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


"""обновление пользователя"""


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return User.objects.all()
        return User.objects.filter(pk=self.request.user.id)
