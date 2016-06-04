# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rss', '0003_rssinput_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssinput',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]