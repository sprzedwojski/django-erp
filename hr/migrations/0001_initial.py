# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appl_name', models.CharField(max_length=50)),
                ('appl_surname', models.CharField(max_length=100)),
                ('appl_email', models.EmailField(max_length=100)),
                ('appl_address', models.CharField(max_length=200)),
                ('appl_phone', models.CharField(max_length=15)),
                ('appl_birthdate', models.DateField()),
                ('appl_submitted', models.DateTimeField(auto_now=True)),
                ('appl_status', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=100)),
                ('job_desc', models.CharField(max_length=2000)),
                ('job_open_from', models.DateField()),
                ('job_open_to', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='appl_job',
            field=models.ForeignKey(to='hr.JobOffer'),
            preserve_default=True,
        ),
    ]
