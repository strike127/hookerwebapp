# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('subject', models.CharField(max_length=10)),
                ('compound', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=30, verbose_name='full name')),
                ('email', models.EmailField(max_length=120)),
                ('date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('updated_time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
