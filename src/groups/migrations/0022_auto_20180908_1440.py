# Generated by Django 2.0.5 on 2018-09-08 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0021_auto_20180908_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
