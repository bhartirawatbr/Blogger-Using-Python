# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.SmallIntegerField(default=0, choices=[(b'female', 'Female'), (b'male', 'Male')]),
        ),
    ]
