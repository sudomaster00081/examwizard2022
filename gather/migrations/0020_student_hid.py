# Generated by Django 4.0.3 on 2022-03-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0019_student_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='hid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]