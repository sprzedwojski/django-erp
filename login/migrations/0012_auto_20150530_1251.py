# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20150517_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginattempt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 30, 12, 51, 3, 16467, tzinfo=utc)),
        ),
    ]
