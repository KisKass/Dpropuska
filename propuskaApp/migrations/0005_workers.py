# Generated by Django 5.0.4 on 2024-05-06 17:26

from django.db import migrations

from propuskaApp.models import *


def populate_workers(apps, schema_editor):

   Worker(F="Иванов", I="Алексей", O="Сергеевич", position=Position.objects.get(pk=1),
          department=Department.objects.get(id=1)).save()
   Worker(F="Петрова", I="Елена", O="Андреевна", position=Position.objects.get(pk=2),
          department=Department.objects.get(id=2)).save()
   Worker(F="Смирнов", I="Иван", O="Николаевич", position=Position.objects.get(pk=3),
          department=Department.objects.get(id=3)).save()
   Worker(F="Козлова", I="Ольга", O="Ивановна", position=Position.objects.get(pk=4),
          department=Department.objects.get(id=4)).save()
   Worker(F="Морозов", I="Дмитрий", O="Владимирович", position=Position.objects.get(pk=5),
          department=Department.objects.get(id=5)).save()
   Worker(F="Васильев", I="Андрей", O="Петрович", position=Position.objects.get(pk=6),
          department=Department.objects.get(id=6)).save()
   Worker(F="Николаева", I="Мария", O="Александровна", position=Position.objects.get(pk=7),
          department=Department.objects.get(id=7)).save()
   Worker(F="Соколов", I="Артем", O="Сергеевич", position=Position.objects.get(pk=8),
          department=Department.objects.get(id=8)).save()
   Worker(F="Кузнецова", I="Наталья", O="Викторовна", position=Position.objects.get(pk=9),
          department=Department.objects.get(id=9)).save()
   Worker(F="Лебедев", I="Игорь", O="Михайлович", position=Position.objects.get(pk=10),
          department=Department.objects.get(id=10)).save()



class Migration(migrations.Migration):

    dependencies = [
        ('propuskaApp', '0004_departments'),
    ]

    operations = [
        migrations.RunPython(populate_workers, migrations.RunPython.noop),

    ]
