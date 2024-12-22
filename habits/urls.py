from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path("habit/create/", HabitCreateAPIView.as_view(), name="create-habit"),

    path("habit/view/<int:pk>", HabitRetrieveAPIView.as_view(), name="view-habit"),
    path("habit/list/", HabitListAPIView.as_view(), name="list-habits"),

    path("habit/update/<int:pk>", HabitUpdateAPIView.as_view(), name="update-habit"),

    path("habit/delete/<int:pk>", HabitDestroyAPIView.as_view(), name="delete-habit"),
]
