import json

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from propuskaApp.models import TempPass, Worker, WorkerPass, Visitor, Passing
from datetime import date, datetime


# TODO
#   просмотр врееменных
#   отображать просроченные пропуска
#   убрать просроченные временны??????

# Create your views here.
@login_required
def Hello(request):
    return render(request, "home.html")


@login_required
def temp_pass(request):
    return render(request, "temp_pass.html", {"active_page": 1})


@login_required
def worker_pass(request):
    return render(request, "worker_pass.html", {"active_page": 2})


@login_required
def create_pass(request):
    escort_list = Worker.objects.values()
    print(escort_list[1])
    if request.POST:
        print(request.POST)
        new_visitor = Visitor(FIO=request.POST['FIO'], document=request.POST['document'],
                              organization=request.POST['organization'])
        new_visitor.save()
        new_pass = TempPass(date_start=request.POST['date_start'], date_end=request.POST['date_end'],
                            issued_by=request.user, visitor=new_visitor,
                            escort=Worker.objects.get(pk=request.POST['escort']))
        new_pass.save()
        redirect('temp')
    return render(request, 'create_pass.html', {"active_page": 3, "escort_options": escort_list})


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        return obj.isoformat(sep=' ')
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


@login_required
def load_data_to_temp_pass(request):
    # object_list1 = Request.objects.all()
    object_list2 = TempPass.objects.values('pk',
                                           'date_start',
                                           'date_end',
                                           'visitor__FIO',

                                           'escort__FIO',

                                           'issued_by__first_name',
                                           'issued_by__last_name',
                                           )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


@login_required
def load_data_to_workers(request):
    # object_list1 = Request.objects.all()
    object_list2 = WorkerPass.objects.values('pk',
                                             'worker__FIO',

                                             'worker__position__name',
                                             'worker__department__name',
                                             'date_start',
                                             'date_end',

                                             )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


@login_required
def load_data_to_pass_view(request):
    # object_list1 = Request.objects.all()
    object_list2 = Passing.objects.values('_pass_id',
                                          '_time',
                                          'location',
                                          )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


def pass_view(request, pk):
    req_pass = TempPass.objects.get(pk=pk)
    return render(request, 'pass_view.html', {'pass_id': pk})


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
