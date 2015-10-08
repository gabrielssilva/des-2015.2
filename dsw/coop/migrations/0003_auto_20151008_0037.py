# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0002_auto_20150910_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
    ]
