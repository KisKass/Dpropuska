from django.db import models

# Create your models here.

class Person(models.Model):
    F = models.CharField(max_length=100, verbose_name='Фамилия')
    I = models.CharField(max_length=100, verbose_name='Имя')
    O = models.CharField(max_length=100, verbose_name='Отчество')

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название должности')

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название отдела')

class Visitor(Person):
    document = models.CharField(max_length=100, verbose_name='Паспорт')
    organization = models.CharField(max_length=100, verbose_name='Организация',null=True,blank=True)

class Worker(Person):
    position = models.ForeignKey(Position,on_delete=models.CASCADE )
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


class Pass(models.Model):
    date_start = models.DateField(verbose_name='Дата выдачи')
    date_end = models.DateField(verbose_name='Дата окончания')
    issued_by = models.ForeignKey(Worker,on_delete=models.CASCADE)

# class WorkerPass(Pass):
#     worker = models.ForeignKey(Worker,on_delete=models.CASCADE)
#

class TempPass(Pass):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    escort = models.ForeignKey(Worker, on_delete=models.CASCADE)

class Location(models.Model):
    location_name = models.CharField(max_length=100, verbose_name='Точка прохода')

class Permission(models.Model):
    _pass = models.ForeignKey(Pass,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

class Passing(models.Model):
    _time = models.DateTimeField(verbose_name='')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    _pass = models.ForeignKey(Pass, on_delete=models.CASCADE)

# class VisitorPassing(models.Model):
#
# class WorkerPassing(models.Model):