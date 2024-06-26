"""
URL configuration for Dpropuska project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from propuskaApp import views

urlpatterns = [
    path('admin/', admin.site.urls,),
    path('', views.Hello, name='home'),
    path('temp_pass', views.temp_pass, name='temp'),
    path('worker_pass', views.worker_pass, name='workers'),
    path('create', views.create_pass, name='new_pass'),
    path('view/<int:pk>/', views.pass_view, name='view'),
    path('stats', views.stats_view, name='stats'),

    path('login', views.login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('load_data_to_temp_pass', views.load_data_to_temp_pass, name='load_data_to_temp_pass'),
    path('load_data_to_workers', views.load_data_to_workers, name='load_data_to_workers'),
    path('load_data_to_pass_view', views.load_data_to_pass_view, name='load_data_to_pass_view'),

]
