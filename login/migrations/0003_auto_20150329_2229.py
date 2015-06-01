# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20150329_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 29, 22, 29, 29, 164086, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='loginattempt',
            name='success',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
