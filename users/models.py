from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Почта пользователя",
        help_text="Введите почту пользователя"
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя"
    )
    patronymic = models.CharField(
        max_length=150,
        verbose_name="Отчество пользователя",
        help_text="Введите отчество пользователя (при наличии)",
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Фамилия пользователя",
        help_text="Введите фамилию пользователя"
    )
    phone = models.CharField(
        max_length=25,
        verbose_name="Телефон пользователя",
        help_text="Укажите номер телефона",
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="Фото пользователя",
        help_text="Загрузите Ваше фото",
        **NULLABLE
    )
    city = models.CharField(
        max_length=100,
        verbose_name="Город",
        help_text="Укажите город",
        **NULLABLE
    )

    token = models.CharField(
        max_length=255,
        verbose_name="Token",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Почта - {self.email}, Имя - {self.first_name}, Фамилия - {self.last_name}"
