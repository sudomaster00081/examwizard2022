# Generated by Django 4.0.3 on 2022-04-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0045_alter_timetable_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallstorage',
            name='icode',
            field=models.IntegerField(default=-1),
        ),
    ]
