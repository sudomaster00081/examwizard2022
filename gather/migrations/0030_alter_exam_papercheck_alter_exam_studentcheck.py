# Generated by Django 4.0.3 on 2022-03-22 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0029_alter_papers_edate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='papercheck',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exam',
            name='studentcheck',
            field=models.IntegerField(default=0),
        ),
    ]