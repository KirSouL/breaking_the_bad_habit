# Generated by Django 5.1.4 on 2025-01-07 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="habit",
            old_name="time_to_compete",
            new_name="time_to_complete",
        ),
    ]
