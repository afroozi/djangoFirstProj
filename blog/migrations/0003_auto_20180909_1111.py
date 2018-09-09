# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180909_1030'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseName', models.CharField(max_length=32)),
                ('UnitsNumber', models.SmallIntegerField()),
                ('Type', models.CharField(default='Profesional', max_length=32, choices=[('General', 'general'), ('Basic', 'basic'), ('Profesional', 'profesional')])),
                ('Department', models.CharField(default='Mathematics department', max_length=56, choices=[('Mathematics department', 'Mathematics department'), ('Computer Engineering department', 'Computer Engineering department'), ('Chemistry and Petroleum Engineering', 'Chemistry and Petroleum Engineering'), ('Religous Center', 'Religous Center'), ('Language Center', 'Language Center')])),
                ('Grade', models.SmallIntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
        migrations.DeleteModel(
            name='CourseGrades',
        ),
    ]
