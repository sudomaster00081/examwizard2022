# Generated by Django 4.0.3 on 2022-04-10 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0037_studentstored_alter_student_hid_alter_student_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexambydate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scode', models.CharField(max_length=15)),
                ('edate', models.DateField()),
                ('etime', models.CharField(max_length=5)),
                ('pid', models.IntegerField(default=-1)),
                ('pcode', models.CharField(max_length=10)),
            ],
        ),
    ]
