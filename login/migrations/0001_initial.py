# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAttempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 29, 21, 38, 7, 874115, tzinfo=utc))),
                ('success', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
