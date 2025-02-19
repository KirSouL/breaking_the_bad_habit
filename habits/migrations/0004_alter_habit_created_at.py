# Generated by Django 5.1.4 on 2025-01-08 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_alter_habit_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="created_at",
            field=models.DateField(
                blank=True,
                default=datetime.date(2025, 1, 8),
                null=True,
                verbose_name="Дата создания привычки",
            ),
        ),
    ]
