# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20180324_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.IntegerField()),
                ('Type', models.CharField(max_length=1)),
                ('descrp', models.CharField(max_length=255, null=True)),
                ('fromuser', models.CharField(max_length=255)),
                ('touser', models.CharField(max_length=255)),
            ],
        ),
    ]
