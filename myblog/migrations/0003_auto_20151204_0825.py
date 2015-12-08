# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20151204_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.SmallIntegerField(default=0, choices=[(0, 'Female'), (1, 'Male')]),
        ),
    ]
