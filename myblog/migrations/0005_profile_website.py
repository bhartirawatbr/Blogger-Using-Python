# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_auto_20151204_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]
