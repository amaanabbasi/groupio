# Generated by Django 2.1 on 2018-08-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20180830_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='groupAdmin',
        ),
        migrations.AlterField(
            model_name='groupadmin',
            name='adminName',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
