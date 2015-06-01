# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoERP', '0004_auto_20150329_2331'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_access_hr', 'Can access HR'), ('can_access_sales', 'Can access Sales'), ('can_access_financial', 'Can access Financial'))},
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
    ]
