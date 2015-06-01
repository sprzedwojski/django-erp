from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_login_failed
from django.db import models

# Create your models here.
from django.http import HttpResponseRedirect
from login.models import LoginAttempt


class Employee(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ("can_access_hr", "Can access HR"),
            ("can_access_sales", "Can access Sales"),
            ("can_access_finance", "Can access Finance"),
        )


# def on_login_failed(sender, credentials, *args, **kwargs):
#     print("Login failed")
#     attempt = LoginAttempt(username=credentials['username'])
#     attempt.success = False
#     attempt.save()
#
#
# def on_login_succeeded(sender, user, *args, **kwargs):
#     print("Login succeeded")
#     # kwargs['request']['GET']
#     attempt = LoginAttempt(username=user)
#     attempt.success = True
#     attempt.save()
#
#
# user_login_failed.connect(on_login_failed)
# user_logged_in.connect(on_login_succeeded)
