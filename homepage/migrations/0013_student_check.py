# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-29 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='check',
            field=models.IntegerField(default=0),
        ),
    ]