# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('console', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=30)),
                ('linguagem', models.CharField(max_length=10)),
                ('estado', models.TextField()),
                ('player_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
