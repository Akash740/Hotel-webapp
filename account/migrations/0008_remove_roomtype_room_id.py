# Generated by Django 3.1.7 on 2021-03-23 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210323_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomtype',
            name='room_id',
        ),
    ]
