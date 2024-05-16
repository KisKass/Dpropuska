import json

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect

from propuskaApp.models import TempPass, Worker, WorkerPass, Visitor, Passing, Department
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
    return render(request, "temp_pass.html", {"active_page": 1,'title':'Временные пропуска'})


@login_required
def worker_pass(request):
    return render(request, "worker_pass.html", {"active_page": 2,'title':'Пропуска сотрудников'})


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
    return render(request, 'create_pass.html', {"active_page": 3, "escort_options": escort_list,'title':'Новый пропуск'})


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
    object_list2 = Passing.objects.values(
                                          '_time',
                                          'location__location_name',
                                          )
    serialized_q = json.dumps(list(object_list2), default=json_serial)

    return HttpResponse(serialized_q, content_type='application/json')


def pass_view(request, pk):
    req_pass = TempPass.objects.filter(pk=pk).values('visitor__FIO', 'visitor__document', 'visitor__organization',
                                                     'escort__FIO', 'escort__department__name', 'id')
    return render(request, 'pass_view.html', {'pass_id': pk, 'req_pass': req_pass,"active_page": 1,'title':f"Просмотр пропуска №{pk}"})

def stats_view(request):
    department_visits = Department.objects.annotate(
        visit_count=Count('worker__temppass')
    ).values('name', 'visit_count')

    # Prepare data for the chart
    department_names = [department['name'] for department in department_visits]
    visit_counts = [department['visit_count'] for department in department_visits]

    context = {
        'department_names': department_names,
        'visit_counts': visit_counts,
        'active_page':4,'title':'Статистика посещения'
    }

    return render(request,'stats.html',context)

def login(request):
    if request.POST:
        print(request.POST)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'login.html',{'title':'Авторизация'})


def logout_user(request):
    logout(request)
    return redirect('home')
