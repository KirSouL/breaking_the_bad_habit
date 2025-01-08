from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.paginators import ListPagination
from habits.serializers import HabitPublicSerializer, HabitBaseSerializer
from users.permissions import IsOwner
from habits.models import Habit


class HabitCreateAPIView(generics.CreateAPIView):
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = HabitBaseSerializer

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Дженерик просмотра привычек пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = (IsAuthenticated, IsOwner,)
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """ Дженерик просмотра списка публичных привычек """
    serializer_class = HabitPublicSerializer
    pagination_class = ListPagination
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Habit.objects.filter(published=True)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Дженерик просмотра выбранной привычки пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = (IsAuthenticated,)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Дженерик обновления привычки пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Дженерик удаления привычки пользователя """
    queryset = Habit.objects.all()
    serializer_class = HabitBaseSerializer
    permission_classes = (IsAuthenticated, IsOwner)
