# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20160814_0038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ['-id']},
        ),
    ]
