import json

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from propuskaApp.models import TempPass, Worker, WorkerPass
from datetime import date, datetime


# Create your views here.
def Hello(request):
    return render(request, "home.html")


def temp_pass(request):
    return render(request, "temp_pass.html")


def worker_pass(request):
    return render(request, "worker_pass.html")


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


@login_required
def load_data_to_temp_pass(request):
    # object_list1 = Request.objects.all()
    object_list2 = TempPass.objects.values('pk',
                                           'date_start',
                                           'date_end',
                                           'visitor__F',
                                           'visitor__I',
                                           'visitor__O',
                                           'escort__F',
                                           'escort__I',
                                           'escort__O',
                                           'issued_by__F',
                                           'issued_by__position__name',
                                           )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


@login_required
def load_data_to_workers(request):
    # object_list1 = Request.objects.all()
    object_list2 = WorkerPass.objects.values('pk',
                                             'worker__F',
                                             'worker__I',
                                             'worker__O',
                                             'worker__position__name',
                                             'worker__department__name',
                                             'date_start',
                                             'date_end',

                                             )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


def login(request):
    if request.POST:
        print(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    logout(request)
    return redirect('home')
