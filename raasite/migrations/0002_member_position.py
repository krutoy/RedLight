# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raasite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='position',
            field=models.CharField(default='member', max_length=30),
            preserve_default=False,
        ),
    ]
