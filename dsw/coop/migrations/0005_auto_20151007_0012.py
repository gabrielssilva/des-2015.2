# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0004_auto_20151004_2353'),
    ]

    operations = [
        migrations.RenameModel('User', 'Player'),

        migrations.RenameField(
            model_name='game',
            old_name='user_id',
            new_name='player_id',
        )
    ]
