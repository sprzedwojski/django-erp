from django.db import models
from django.utils import timezone

# Create your models here.


class LoginAttempt(models.Model):
    username = models.CharField(max_length=50)
    date = models.DateTimeField(default=timezone.now())
    success = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args)
        self.username = kwargs.get('username', '')
        self.date = timezone.now()

    def __str__(self):
        now = self.date.strftime('%Y/%m/%d %H:%M:%S')
        return self.username + " " + str(self.success) + " " + now
