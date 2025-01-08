from django.db import models
from django.utils import timezone

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    CHOICES_PUBLISHED = (
        (True, "Статус привычки - публичная"),
        (False, "Статус привычки - личная"),
    )

    owner = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Создатель привычки (владелец)",
        help_text="Укажите создателя привычки (владельца)",
        **NULLABLE
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место выполения привычки",
        **NULLABLE
    )
    time = models.TimeField(
        max_length=30,
        verbose_name="Время привычки",
        help_text="Время выполения привычки",
        **NULLABLE
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие привычки",
        help_text="Действие, которое представляет собой привычка",
        **NULLABLE
    )
    pleasant_habit = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
        **NULLABLE
    )
    period = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность выполнения привычки",
        **NULLABLE
    )
    reward = models.CharField(
        max_length=150,
        verbose_name="Награда",
        help_text="Укажите награду за выполение привычки (действия)",
        **NULLABLE
    )
    time_to_complete = models.PositiveIntegerField(
        default=0,
        verbose_name="Время на выполнение привычки",
        **NULLABLE
    )
    published = models.BooleanField(
        default=False,
        verbose_name="Состояние публикации привычки",
        help_text="Укажите статус привычки",
        choices=CHOICES_PUBLISHED,
        **NULLABLE
    )
    created_at = models.DateField(
        default=timezone.now(),
        verbose_name="Дата создания привычки",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"
