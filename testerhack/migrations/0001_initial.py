# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyticsOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.IntegerField(default=0)),
                ('buy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AnalyticsTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hit', models.IntegerField(default=0)),
                ('buy', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField(default=50)),
                ('org_site', models.URLField()),
                ('new_site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='UsersRedirect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('site', models.IntegerField(default=0)),
            ],
        ),
    ]
