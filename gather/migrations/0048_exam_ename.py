# Generated by Django 4.0.3 on 2022-04-29 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gather', '0047_rename_icode_hallstorage_iid'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='ename',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
