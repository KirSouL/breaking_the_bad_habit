# Generated by Django 5.1.4 on 2024-12-22 18:43

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "place",
                    models.CharField(
                        blank=True,
                        help_text="Укажите место выполения привычки",
                        max_length=100,
                        null=True,
                        verbose_name="Место выполнения привычки",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        blank=True,
                        help_text="Время выполения привычки",
                        max_length=30,
                        null=True,
                        verbose_name="Время привычки",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        blank=True,
                        help_text="Действие, которое представляет собой привычка",
                        max_length=255,
                        null=True,
                        verbose_name="Действие привычки",
                    ),
                ),
                (
                    "pleasant_habit",
                    models.BooleanField(
                        default=False, verbose_name="Признак приятной привычки"
                    ),
                ),
                (
                    "period",
                    models.PositiveIntegerField(
                        blank=True,
                        default=1,
                        null=True,
                        verbose_name="Периодичность выполнения привычки",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="Укажите награду за выполение привычки (действия)",
                        max_length=150,
                        null=True,
                        verbose_name="Награда",
                    ),
                ),
                (
                    "time_to_compete",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        verbose_name="Время на выполнение привычки",
                    ),
                ),
                (
                    "published",
                    models.BooleanField(
                        blank=True,
                        choices=[
                            (True, "Статус привычки - публичная"),
                            (False, "Статус привычки - личная"),
                        ],
                        default=False,
                        help_text="Укажите статус привычки",
                        null=True,
                        verbose_name="Состояние публикации привычки",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Дата создания привычки",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="Укажите создателя привычки (владельца)",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычки (владелец)",
                    ),
                ),
                (
                    "related_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите связанную привычку",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]