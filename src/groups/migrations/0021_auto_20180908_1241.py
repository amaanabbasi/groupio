# Generated by Django 2.0.5 on 2018-09-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0020_category_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
        migrations.AddField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50)),
        ),
    ]
