# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 19:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161128_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 28, 19, 50, 20, 422140, tzinfo=utc)),
        ),
    ]