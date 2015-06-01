# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_auto_20150517_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplicant',
            name='appl_notes',
            field=models.TextField(default=b'', max_length=1500),
        ),
    ]
