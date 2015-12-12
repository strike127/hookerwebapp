# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scan',
            old_name='toi',
            new_name='toi_activity',
        ),
    ]
