# Generated by Django 4.0.3 on 2022-03-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0033_paperstorage_timetable_allocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='dornot',
            field=models.CharField(default='enabled', max_length=8),
        ),
    ]