# Generated by Django 4.0.3 on 2022-03-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0017_invigilator_eid'),
    ]

    operations = [
        migrations.AddField(
            model_name='invigilator',
            name='hid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]