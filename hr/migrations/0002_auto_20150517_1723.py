# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_salary', models.IntegerField()),
                ('emp_position', models.CharField(max_length=50)),
                ('emp_applicant', models.ForeignKey(to='hr.JobApplicant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='jobapplicant',
            name='appl_cv',
            field=models.FileField(null=True, upload_to=b''),
            preserve_default=True,
        ),
    ]
