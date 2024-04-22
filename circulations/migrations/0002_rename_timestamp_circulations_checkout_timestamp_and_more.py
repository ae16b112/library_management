# Generated by Django 5.0.4 on 2024-04-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("circulations", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="circulations",
            old_name="timestamp",
            new_name="checkout_timestamp",
        ),
        migrations.RemoveField(
            model_name="circulations",
            name="event_type",
        ),
        migrations.AddField(
            model_name="circulations",
            name="is_returned",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="circulations",
            name="return_timeout",
            field=models.DateTimeField(auto_now=True),
        ),
    ]