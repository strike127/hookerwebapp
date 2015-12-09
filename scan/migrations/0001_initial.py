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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=10)),
                ('current_status', models.CharField(max_length=20)),
                ('compound', models.CharField(max_length=3, choices=[('C11', 'C11'), ('F18', 'F18')])),
                ('name', models.CharField(max_length=30, verbose_name='full name')),
                ('email', models.EmailField(max_length=120)),
                ('date_for_scan', models.CharField(max_length=30)),
                ('time_for_scan', models.CharField(max_length=30)),
                ('request_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('request_time', models.TimeField(auto_now_add=True)),
                ('updated_time', models.TimeField(auto_now=True)),
                ('init_activity', models.DecimalField(decimal_places=3, null=True, max_digits=5)),
                ('synthesize_time', models.CharField(max_length=30)),
                ('synthesize_time_auto', models.TimeField(auto_now=True)),
                ('toi', models.DecimalField(decimal_places=3, null=True, max_digits=5)),
                ('scan_time', models.CharField(max_length=30)),
                ('scan_time_auto', models.TimeField(auto_now=True)),
            ],
        ),
    ]
