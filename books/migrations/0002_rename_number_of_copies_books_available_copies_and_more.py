# Generated by Django 5.0.4 on 2024-04-22 05:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="books",
            old_name="number_of_copies",
            new_name="available_copies",
        ),
        migrations.AddField(
            model_name="books",
            name="total_copies",
            field=models.IntegerField(default=0),
        ),
    ]
