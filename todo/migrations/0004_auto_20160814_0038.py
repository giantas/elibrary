# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 21:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20160810_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='id_done',
            new_name='is_done',
        ),
    ]
