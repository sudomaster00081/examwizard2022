# Generated by Django 4.0.3 on 2022-04-29 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0048_exam_ename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendancestored',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(default=-1)),
                ('pid', models.IntegerField(default=-1)),
                ('edate', models.DateField()),
                ('etime', models.CharField(max_length=5)),
                ('hid', models.IntegerField(default=-1)),
                ('seatno', models.IntegerField(default=-1)),
            ],
        ),
    ]