# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Saved_answers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(default=b'', max_length=100, blank=True)),
                ('level', models.CharField(default=b'', max_length=100, blank=True)),
                ('seconds', models.CharField(default=b'', max_length=100, blank=True)),
                ('answer1', models.TextField(default=b'', null=True, blank=True)),
                ('answer2', models.TextField(default=b'', null=True, blank=True)),
                ('answer3', models.TextField(default=b'', null=True, blank=True)),
                ('answer4', models.TextField(default=b'', null=True, blank=True)),
                ('answer5', models.TextField(default=b'', null=True, blank=True)),
                ('answer6', models.TextField(default=b'', null=True, blank=True)),
                ('answer7', models.TextField(default=b'', null=True, blank=True)),
                ('answer8', models.TextField(default=b'', null=True, blank=True)),
                ('answer9', models.TextField(default=b'', null=True, blank=True)),
                ('answer10', models.TextField(default=b'', null=True, blank=True)),
                ('answer11', models.TextField(default=b'', null=True, blank=True)),
                ('answer12', models.TextField(default=b'', null=True, blank=True)),
                ('answer13', models.TextField(default=b'', null=True, blank=True)),
                ('answer14', models.TextField(default=b'', null=True, blank=True)),
                ('answer15', models.TextField(default=b'', null=True, blank=True)),
                ('answer16', models.TextField(default=b'', null=True, blank=True)),
                ('answer17', models.TextField(default=b'', null=True, blank=True)),
                ('answer18', models.TextField(default=b'', null=True, blank=True)),
                ('answer19', models.TextField(default=b'', null=True, blank=True)),
                ('answer20', models.TextField(default=b'', null=True, blank=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
