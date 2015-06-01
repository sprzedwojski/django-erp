# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoERP', '0005_auto_20150329_2335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_access_hr', 'Can access HR'), ('can_access_sales', 'Can access Sales'), ('can_access_finance', 'Can access Finance'))},
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default=datetime.datetime(2015, 3, 29, 23, 37, 41, 681613, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
