# Generated by Django 4.0.1 on 2022-04-11 22:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_recovery_password_valid_thru'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recovery_password',
            name='valid_thru',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 22, 34, 57, 420865)),
        ),
    ]
