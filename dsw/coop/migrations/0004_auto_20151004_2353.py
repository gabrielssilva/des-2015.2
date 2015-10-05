# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0003_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='senha',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='telefone',
        ),
    ]
