# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(default=b'', max_length=100, blank=True)),
                ('password', models.CharField(default=b'', max_length=100, blank=True)),
                ('level', models.CharField(default=b'', max_length=100, blank=True)),
                ('is_active', models.CharField(default=b'', max_length=100, blank=True)),
            ],
        ),
    ]
