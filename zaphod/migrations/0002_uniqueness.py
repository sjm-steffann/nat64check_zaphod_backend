# Generated by Django 2.0b1 on 2017-11-05 20:59

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zaphod', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testresult',
            unique_together={('testrun', 'trillian')},
        ),
        migrations.AlterUniqueTogether(
            name='testschedule',
            unique_together={('owner', 'name')},
        ),
    ]
