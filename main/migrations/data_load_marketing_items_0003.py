# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


#start with a list of all the data we want to add.
init_marketing_data = [
    {
        "img":"yoda.jpg",
        "heading":"Hone your Jedi Skills",
        "caption":"All members have access to our unique"
        " training and achievements latters. Progress through the "
        "levels and show everyone who the top Jedi Master is!",
        "button_title":"Sign Up Now"
    },
    {
        "img":"clone_army.jpg",
        "heading":"Build your Clan",
        "caption":"Engage in meaningful conversation, or "
        "bloodthirsty battle! If it's related to "
        "Star Wars, in any way, you better believe we do it.",
        "button_title":"Sign Up Now"
    },
    {
        "img":"leia.jpg",
        "heading":"Find Love",
        "caption":"Everybody knows Star Wars fans are the "
        "best mates for Star Wars fans. Find your "
        "Princess Leia or Han Solo and explore the "
        "stars together.",
        "button_title":"Sign Up Now"
    },
]
def create_marketing_items(apps, schema_editor):

    MarketingItem = apps.get_model("main", "MarketingItem")
    
    #stare data in database
    [MarketingItem(**d).save() for d in init_marketing_data]


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_statusreport'),
    ]

    operations = [
        migrations.RunPython(create_marketing_items)
    ]
