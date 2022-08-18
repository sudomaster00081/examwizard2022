# Generated by Django 4.0.3 on 2022-03-21 09:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0022_papers_edate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='papers',
            name='edate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='papers',
            name='pcode',
            field=models.CharField(max_length=10),
        ),
    ]
