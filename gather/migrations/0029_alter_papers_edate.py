# Generated by Django 4.0.3 on 2022-03-21 16:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0028_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='edate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
