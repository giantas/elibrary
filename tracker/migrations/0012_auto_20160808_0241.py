# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-07 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20160808_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintainer',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
