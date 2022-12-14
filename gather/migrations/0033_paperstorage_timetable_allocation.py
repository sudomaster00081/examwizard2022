# Generated by Django 4.0.3 on 2022-03-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0032_alter_timetable_pid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paperstorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(default=0)),
                ('edate', models.DateField()),
                ('etime', models.CharField(max_length=5)),
                ('pid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='timetable',
            name='allocation',
            field=models.CharField(default='Allocate', max_length=10),
        ),
    ]
