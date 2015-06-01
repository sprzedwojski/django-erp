# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoERP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 29, 22, 59, 46, 977601, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=False,
        ),
    ]
