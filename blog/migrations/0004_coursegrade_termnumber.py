# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180909_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursegrade',
            name='TermNumber',
            field=models.SmallIntegerField(default='1'),
        ),
    ]
