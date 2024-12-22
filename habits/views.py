from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.paginators import ListPagination
from users.permissions import IsOwner
from habits.models import Habit


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)


class HabitListAPIView(generics.ListAPIView):
    queryset = Habit.objects.all()
    permission_classes = (AllowAny,)
    pagination_class = ListPagination


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Дженерик удаления привычки пользователя """
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
