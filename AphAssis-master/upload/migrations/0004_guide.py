# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-14 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_auto_20180413_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('right_answer', models.CharField(max_length=30, null=True)),
                ('wrong_answer', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
