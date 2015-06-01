# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoERP', '0002_employee_create_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='create_date',
        ),
    ]
