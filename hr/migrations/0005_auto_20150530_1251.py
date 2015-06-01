# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_jobapplicant_appl_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplicant',
            name='appl_cv',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_applicant',
            field=models.ForeignKey(verbose_name=b'Applicant', to='hr.JobApplicant'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_position',
            field=models.CharField(max_length=50, verbose_name=b'Employee position'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_salary',
            field=models.IntegerField(verbose_name=b'Salary ($)'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_address',
            field=models.CharField(max_length=200, verbose_name=b'Applicant address'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_birthdate',
            field=models.DateField(verbose_name=b'Applicant birthday'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_email',
            field=models.EmailField(max_length=100, verbose_name=b'Applicant email'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_job',
            field=models.ForeignKey(verbose_name=b'Applies for', to='hr.JobOffer'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_name',
            field=models.CharField(max_length=50, verbose_name=b'Applicant name'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_notes',
            field=models.TextField(default=b'', max_length=1500, verbose_name=b'Other notes'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_phone',
            field=models.CharField(max_length=15, verbose_name=b'Applicant phone'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_status',
            field=models.ForeignKey(verbose_name=b'Applicant status', to='hr.RecruitmentStatus'),
        ),
        migrations.AlterField(
            model_name='jobapplicant',
            name='appl_surname',
            field=models.CharField(max_length=100, verbose_name=b'Applicant surname'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_desc',
            field=models.CharField(max_length=2000, verbose_name=b'Job description'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_name',
            field=models.CharField(max_length=100, verbose_name=b'Job name'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_open_from',
            field=models.DateField(verbose_name=b'Valid from'),
        ),
        migrations.AlterField(
            model_name='joboffer',
            name='job_open_to',
            field=models.DateField(verbose_name=b'Valid to'),
        ),
    ]
