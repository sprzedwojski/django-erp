from django.db import models


class RecruitmentStatus(models.Model):
    stat_name = models.CharField(max_length=30, unique=True)
    stat_order = models.IntegerField(default=0, unique=True)

    def __str__(self):
        return self.stat_name + " (" + self.stat_order.__str__() + ")"

    @staticmethod
    def get_max_id():
        statuses = RecruitmentStatus.objects.all()
        max_id = 0
        for status in statuses:
            if status.stat_order > max_id:
                max_id = status.stat_order
        return max_id


class JobOffer(models.Model):
    job_name = models.CharField(max_length=100, verbose_name="Job name")
    job_desc = models.CharField(max_length=2000, verbose_name="Job description")
    job_open_from = models.DateField(verbose_name="Valid from")
    job_open_to = models.DateField(verbose_name="Valid to")

    def __unicode__(self):
        return self.job_name


class JobApplicant(models.Model):
    appl_name = models.CharField(max_length=50, verbose_name="Applicant name")
    appl_surname = models.CharField(max_length=100, verbose_name="Applicant surname")
    appl_email = models.EmailField(max_length=100, verbose_name="Applicant email")
    appl_address = models.CharField(max_length=200, verbose_name="Applicant address")
    appl_phone = models.CharField(max_length=15, verbose_name="Applicant phone")
    appl_birthdate = models.DateField(verbose_name="Applicant birthday")
    appl_submitted = models.DateTimeField(auto_now=True)
    appl_status = models.ForeignKey(RecruitmentStatus, verbose_name="Applicant status")
    appl_job = models.ForeignKey(JobOffer, verbose_name="Applies for")
    appl_notes = models.TextField(default="", max_length=1500, verbose_name="Other notes", blank=True, null=True)

    def get_string(self):
        return self.appl_name + " " + self.appl_surname

    def __unicode__(self):
        return self.get_string()

    def __str__(self):
        return self.get_string()


class Employee(models.Model):
    emp_applicant = models.ForeignKey(JobApplicant, verbose_name="Applicant")
    emp_salary = models.IntegerField(verbose_name="Salary ($)")
    emp_position = models.CharField(max_length=50, verbose_name="Employee position")

    def get_string(self):
        return self.emp_applicant.appl_name + " " + self.emp_applicant.appl_surname

    def __unicode__(self):
        return self.emp_applicant.__str__()


class SalaryHistory(models.Model):
    shi_employee = models.ForeignKey(Employee, verbose_name="Employee", on_delete=models.SET_NULL, null=True)
    shi_salary = models.IntegerField(verbose_name="Salary ($)")
    shi_month = models.DateField(verbose_name="Payday")

    def __str__(self):
        return self.shi_employee.get_string()