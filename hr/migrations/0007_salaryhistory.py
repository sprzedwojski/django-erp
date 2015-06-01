# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shi_salary', models.IntegerField(verbose_name=b'Salary ($)')),
                ('shi_month', models.DateField(verbose_name=b'Payday')),
                ('shi_employee', models.ForeignKey(verbose_name=b'Employee', to='hr.Employee')),
            ],
        ),
    ]
