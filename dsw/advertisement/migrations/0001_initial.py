# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=30)),
                ('data', models.DateTimeField()),
                ('disponibilidade', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
