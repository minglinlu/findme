# Generated by Django 3.2.5 on 2021-09-01 09:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('opportunity', '0011_auto_20210901_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedjob',
            name='applied_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 1, 9, 44, 22, 329281, tzinfo=utc), verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='savedjob',
            name='saved_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 1, 9, 44, 22, 329743, tzinfo=utc), verbose_name='Start Date'),
        ),
    ]
