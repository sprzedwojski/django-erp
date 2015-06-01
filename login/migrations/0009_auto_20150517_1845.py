# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20150517_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 17, 18, 45, 2, 702206, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
