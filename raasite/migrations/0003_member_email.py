# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raasite', '0002_member_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(default='default@xxx.com', max_length=30),
            preserve_default=False,
        ),
    ]
