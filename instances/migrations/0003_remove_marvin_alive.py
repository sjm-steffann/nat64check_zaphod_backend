# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••
#  Copyright (c) 2018, S.J.M. Steffann. This software is licensed under the BSD
#  3-Clause License. Please see the LICENSE file in the project root directory.
# ••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••

# Generated by Django 2.0.7 on 2018-07-15 15:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('instances', '0002_trillian_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marvin',
            name='alive',
        ),
    ]
