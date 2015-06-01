from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login
from login.models import LoginAttempt
from login.forms import LoginForm


def get_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = request.POST.get('username')
            passw = request.POST.get('password')
            login_attempt = LoginAttempt(username=uname)
            user = authenticate(username=uname, password=passw)
            if user.groups.all().count() == 0:
                login(request, user)
                login_attempt.success = True
                login_attempt.save()
                return HttpResponseRedirect(reverse('admin:index'))
            if user is not None:
                login(request, user)
                login_attempt.success = True
                login_attempt.save()
                redir_path = user.employee.department.lower()
                return HttpResponseRedirect("../" + redir_path)
            else:
                login_attempt.success = False
                login_attempt.save()
                variables = {
                    'form': form,
                    'error_text': 'Invalid username or password'
                }
                return render(request, 'login/index.html', variables)

    else:
        form = LoginForm()
    return render(request, 'login/index.html', {'form': form})