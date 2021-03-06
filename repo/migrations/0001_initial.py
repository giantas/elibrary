# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-06 17:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first_name', models.CharField(blank=True, max_length=25)),
                ('author_last_name', models.CharField(default='Unknown', max_length=25)),
                ('author_middle_name', models.CharField(blank=True, max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, default='Unknown', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=30)),
                ('lend_date', models.DateField()),
                ('expected_return_date', models.DateField()),
                ('surchages', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=60)),
                ('url', models.URLField()),
                ('department_category', models.CharField(max_length=20)),
                ('keyword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=25)),
                ('item_description', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='private', max_length=8)),
                ('cardid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Card')),
            ],
        ),
        migrations.CreateModel(
            name='LibraryBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('number_borrowed', models.IntegerField(default=0)),
                ('book_author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.BookAuthors')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.BookCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
                ('approval_status', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected')], default='rejected', max_length=10)),
                ('progress', models.CharField(choices=[('in-progress', 'In Progress'), ('resolved', 'Resolved')], default='in-progress', max_length=12)),
                ('comments', models.CharField(max_length=150)),
                ('photo', models.URLField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SingleBook',
            fields=[
                ('serial_number', models.CharField(max_length=150, primary_key=True, serialize=False)),
                ('is_available_returned', models.BooleanField(default=True)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.LibraryBook')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_name', models.CharField(max_length=100)),
                ('publicity_status', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='private', max_length=8)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=30)),
                ('user_level', models.CharField(choices=[('admin', 'Admin'), ('staff', 'Staff'), ('hof', 'Head of Facilities'), ('user', 'User')], default='user', max_length=7)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='listid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.Todo'),
        ),
        migrations.AddField(
            model_name='borrowinglog',
            name='bookid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', related_query_name='log', to='repo.LibraryBook'),
        ),
        migrations.AddField(
            model_name='borrowinglog',
            name='log_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.SingleBook'),
        ),
        migrations.AddField(
            model_name='borrowinglog',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_user', related_query_name='log', to=settings.AUTH_USER_MODEL),
        ),
    ]
