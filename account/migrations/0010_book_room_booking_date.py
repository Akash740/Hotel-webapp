# Generated by Django 3.1.7 on 2021-06-28 09:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_book_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_room',
            name='booking_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
