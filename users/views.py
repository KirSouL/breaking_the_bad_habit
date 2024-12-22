from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.paginators import ListPagination
from users.models import User
from users.permissions import IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Дженерик создания пользователя"""
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Дженерик получения всех пользователей"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    pagination_class = ListPagination


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """Дженерик получения одного пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """Дженерик обновления пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner,]


class UserDestroyAPIView(generics.DestroyAPIView):
    """Дженерик удаления пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner,]
