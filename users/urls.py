from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserRetrieveAPIView, UserUpdateAPIView, \
    UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('user/token/login/', TokenObtainPairView.as_view(), name='token_login'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("user/create/", UserCreateAPIView.as_view(), name="create-user"),

    path("user/view/<int:pk>", UserRetrieveAPIView.as_view(), name="view-user"),
    path("user/list/", UserListAPIView.as_view(), name="list-users"),

    path("user/update/<int:pk>", UserUpdateAPIView.as_view(), name="update-user"),

    path("user/delete/<int:pk>", UserDestroyAPIView.as_view(), name="delete-user"),
]
