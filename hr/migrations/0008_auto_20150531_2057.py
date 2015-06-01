# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_salaryhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_notes',
            field=models.TextField(default=b'', max_length=1500, null=True, verbose_name=b'Other notes', blank=True),
        ),
        migrations.AlterField(
            model_name='salaryhistory',
            name='shi_employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'Employee', to='hr.Employee', null=True),
        ),
    ]
