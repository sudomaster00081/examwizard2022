# Generated by Django 4.0.3 on 2022-03-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0034_alter_timetable_dornot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hall',
            name='eid',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='invigilator',
            name='eid',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='paperstorage',
            name='eid',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='paperstorage',
            name='pid',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='pid',
            field=models.IntegerField(default=-1),
        ),
    ]