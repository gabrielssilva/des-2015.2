# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_advertisement_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='games',
        ),
        migrations.DeleteModel(
            name='Advertisement',
        ),
    ]
