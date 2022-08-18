# Generated by Django 4.0.3 on 2022-03-19 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0010_timetable_eid_timetable_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='ecode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='hall',
            name='hcode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='hall',
            name='hname',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='invigilator',
            name='icode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='pcode',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='scode',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='pid',
            field=models.IntegerField(unique=True),
        ),
    ]
