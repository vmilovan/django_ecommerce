# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', 'data_load_marketing_items_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusreport',
            name='when',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
