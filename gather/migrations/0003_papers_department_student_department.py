# Generated by Django 4.0.3 on 2022-03-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0002_hall_invigilator_student_remove_papers_pdate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='department',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
