# Generated by Django 3.1 on 2021-01-15 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_auto_20210115_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='user',
        ),
    ]