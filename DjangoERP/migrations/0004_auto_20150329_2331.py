# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoERP', '0003_remove_employee_create_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': (('can_drive', 'Can drive'), ('can_vote', 'Can vote in elections'), ('can_drink', 'Can drink alcohol'))},
        ),
    ]
