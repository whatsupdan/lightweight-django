# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_task_due'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='competed',
            new_name='completed',
        ),
    ]
