# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-12 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailysurprise',
            name='user',
            field=models.ManyToManyField(to='app.User'),
        ),
    ]
