# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_auto_20150517_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecruitmentStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stat_name', models.CharField(unique=True, max_length=30)),
                ('stat_order', models.IntegerField(default=0, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_status',
            field=models.ForeignKey(to='hr.RecruitmentStatus'),
            preserve_default=True,
        ),
    ]
