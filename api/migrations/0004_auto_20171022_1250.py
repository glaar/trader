# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-22 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='currency',
            field=models.CharField(max_length=25),
        ),
    ]
