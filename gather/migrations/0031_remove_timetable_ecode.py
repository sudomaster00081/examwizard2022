# Generated by Django 4.0.3 on 2022-03-22 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0030_alter_exam_papercheck_alter_exam_studentcheck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='ecode',
        ),
    ]
