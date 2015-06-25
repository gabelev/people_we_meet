# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('peer_app', '0002_auto_20150614_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
