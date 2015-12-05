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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=10)),
                ('compound', models.CharField(max_length=3)),
                ('current_status', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30, verbose_name='full name')),
                ('email', models.EmailField(max_length=120)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('request_time', models.TimeField(auto_now_add=True)),
                ('updated_time', models.TimeField(auto_now=True)),
                ('date_for_scan', models.CharField(max_length=30)),
                ('time_for_scan', models.CharField(max_length=30)),
            ],
        ),
    ]
