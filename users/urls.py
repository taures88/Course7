from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserListView, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='users_update'), # обновление пользователя

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # получение токена
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # обновление токена

]
