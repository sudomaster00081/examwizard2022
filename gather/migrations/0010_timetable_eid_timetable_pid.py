# Generated by Django 4.0.3 on 2022-03-19 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0009_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='eid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetable',
            name='pid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
