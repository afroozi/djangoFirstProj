# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrades',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=32)),
                ('UnitsNumber', models.SmallIntegerField()),
                ('Grade', models.SmallIntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
