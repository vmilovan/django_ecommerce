# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PollItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=300)),
                ('votes', models.IntegerField(default=0)),
                ('percentage', models.DecimalField(max_digits=5, decimal_places=2, default=0.0)),
                ('poll', models.ForeignKey(to='djangular_polls.Poll', related_name='items')),
            ],
            options={
                'ordering': ['-text'],
            },
        ),
    ]
