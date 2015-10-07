# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0006_auto_20151007_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='user',
        ),
        migrations.AddField(
            model_name='player',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='player',
            name='password',
            field=models.CharField(default=12345, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
