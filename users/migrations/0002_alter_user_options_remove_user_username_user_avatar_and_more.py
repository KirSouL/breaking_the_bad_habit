# Generated by Django 5.1.4 on 2024-12-22 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True,
                help_text="Загрузите Ваше фото",
                null=True,
                upload_to="users/avatars",
                verbose_name="Фото пользователя",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True,
                help_text="Укажите город",
                max_length=100,
                null=True,
                verbose_name="Город",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="patronymic",
            field=models.CharField(
                blank=True,
                help_text="Введите отчество пользователя (при наличии)",
                max_length=150,
                null=True,
                verbose_name="Отчество пользователя",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="phone",
            field=models.CharField(
                blank=True,
                help_text="Укажите номер телефона",
                max_length=25,
                null=True,
                verbose_name="Телефон пользователя",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Token"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                help_text="Введите почту пользователя",
                max_length=254,
                unique=True,
                verbose_name="Почта пользователя",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                help_text="Введите имя пользователя",
                max_length=150,
                verbose_name="Имя пользователя",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                help_text="Введите фамилию пользователя",
                max_length=150,
                verbose_name="Фамилия пользователя",
            ),
        ),
    ]
