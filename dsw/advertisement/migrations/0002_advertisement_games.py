# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20151120_0151'),
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='games',
            field=models.ManyToManyField(to='game.Game'),
        ),
    ]
