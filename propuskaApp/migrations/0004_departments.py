# Generated by Django 5.0.4 on 2024-05-06 17:26

from django.db import migrations

from propuskaApp.models import Position, Department


def populate_departments(apps, schema_editor):
    objs = Department.objects.bulk_create(
        [
            Department(name="Производство"),
            Department(name="Продажи"),
            Department(name="Финансы"),
            Department(name="Логистика"),
            Department(name="Кадры"),
            Department(name="IT"),
            Department(name="Маркетинг"),
            Department(name="Финансы"),
            Department(name="Администрация"),
            Department(name="PR"),
        ]
    )

class Migration(migrations.Migration):

    dependencies = [
        ('propuskaApp', '0003_positions'),
    ]

    operations = [
        migrations.RunPython(populate_departments, migrations.RunPython.noop),

    ]
