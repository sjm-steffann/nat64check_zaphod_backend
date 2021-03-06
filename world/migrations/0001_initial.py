# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#  Copyright (c) 2018, S.J.M. Steffann. This software is licensed under the BSD
#  3-Clause License. Please see the LICENSE file in the project root directory.
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Generated by Django 2.0.7 on 2018-07-07 19:36

import django.db.models.deletion
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('code', models.PositiveIntegerField(
                    primary_key=True,
                    serialize=False,
                    verbose_name='code')),
                ('level', models.PositiveSmallIntegerField(
                    verbose_name='level')),
                ('name', models.CharField(
                    max_length=100,
                    verbose_name='name')),
                ('countries', django_countries.fields.CountryField(
                    blank=True,
                    max_length=746,
                    multiple=True,
                    verbose_name='countries')),
                ('parent', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='world.Region',
                    verbose_name='parent')),
            ],
            options={
                'verbose_name': 'region',
                'verbose_name_plural': 'regions',
                'ordering': ('name',),
            },
        ),
    ]
