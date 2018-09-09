# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Title', models.CharField(max_length=255)),
                ('Author', models.CharField(max_length=255)),
                ('Body', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='coursegrades',
            name='Department',
            field=models.CharField(choices=[('Mathematics department', 'Mathematics department'), ('Computer Engineering department', 'Computer Engineering department'), ('Chemistry and Petroleum Engineering', 'Chemistry and Petroleum Engineering'), ('Religous Center', 'Religous Center'), ('Language Center', 'Language Center')], max_length=56, default='Mathematics department'),
        ),
        migrations.AddField(
            model_name='coursegrades',
            name='Type',
            field=models.CharField(choices=[('General', 'general'), ('Basic', 'basic'), ('Profesional', 'profesional')], max_length=32, default='Profesional'),
        ),
        migrations.AlterField(
            model_name='coursegrades',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
