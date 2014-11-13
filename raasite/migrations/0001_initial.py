# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('photo_url', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=30)),
                ('grade', models.CharField(max_length=30)),
                ('intro', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
