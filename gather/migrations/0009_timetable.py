# Generated by Django 4.0.3 on 2022-03-18 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0008_alter_student_pid0_alter_student_pid1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecode', models.CharField(max_length=10)),
                ('edate', models.DateField()),
                ('etime', models.TimeField()),
            ],
        ),
    ]