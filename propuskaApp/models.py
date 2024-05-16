from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Person(models.Model):
    # F = models.CharField(max_length=100, verbose_name='Фамилия')
    # I = models.CharField(max_length=100, verbose_name='Имя')
    # O = models.CharField(max_length=100, verbose_name='Отчество')
    FIO = models.CharField(max_length=200, verbose_name='ФИО')

    def __str__(self):
        return f"{self.FIO}"

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название должности')
    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return f"{self.name}"

class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название отдела')
    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return f"{self.name}"

class Visitor(Person):
    document = models.CharField(max_length=100, verbose_name='Паспорт')
    organization = models.CharField(max_length=100, verbose_name='Организация', null=True, blank=True)
    class Meta:
        verbose_name = "Посетитель"
        verbose_name_plural = "Посетители"


class Worker(Person):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"



class Pass(models.Model):
    date_start = models.DateField(verbose_name='Дата выдачи')
    date_end = models.DateField(verbose_name='Дата окончания')
    issued_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Кем выдан")

    def __str__(self):
        return f"Пропуск №{self.id}  "

class WorkerPass(Pass):
    worker = models.ForeignKey(Worker,on_delete=models.CASCADE, verbose_name="Сотрудник")
    class Meta:
        verbose_name = "Пропуск сотрудника"
        verbose_name_plural = "Пропуска сотрудников"

    def __str__(self):
        return f"{self.id}  | {self.worker.FIO}"


class TempPass(Pass):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE,verbose_name='Посетитель')
    escort = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Сопровождающий')
    class Meta:
        verbose_name = "Временный пропуск"
        verbose_name_plural = "Временные пропуска"

    def __str__(self):
        return f"{self.id}  | {self.visitor.FIO}"

class Location(models.Model):
    location_name = models.CharField(max_length=100, verbose_name='Точка прохода')
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
    def __str__(self):
        return f"{self.location_name}"


class Permission(models.Model):
    _pass = models.ForeignKey(Pass, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Passing(models.Model):
    _time = models.DateTimeField(verbose_name='Время прохождения')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name='Точка прохода')
    _pass = models.ForeignKey(TempPass, on_delete=models.CASCADE, verbose_name='Пропуск')
    class Meta:
        verbose_name = "Прохождение"
        verbose_name_plural = "Прохождения"
    def __str__(self):
        return f"Пропуск №{self._pass.id} | {self._time}"

# class VisitorPassing(models.Model):
#
# class WorkerPassing(models.Model):
