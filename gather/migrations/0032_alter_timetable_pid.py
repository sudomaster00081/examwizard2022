# Generated by Django 4.0.3 on 2022-03-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0031_remove_timetable_ecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='pid',
            field=models.IntegerField(default=0),
        ),
    ]
