# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0003_auto_20151008_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('console', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('language', models.CharField(max_length=10)),
                ('desc_state', models.TextField()),
                ('user_id', models.ForeignKey(to='coop.User')),
            ],
        ),
    ]
