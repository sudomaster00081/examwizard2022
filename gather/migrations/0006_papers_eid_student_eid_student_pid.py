# Generated by Django 4.0.3 on 2022-03-18 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0005_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='papers',
            name='eid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='eid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='pid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
