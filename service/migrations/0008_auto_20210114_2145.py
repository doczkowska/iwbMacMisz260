# Generated by Django 3.1 on 2021-01-14 20:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0007_notice_user'),
    ]

    operations = [
#         migrations.AlterField(
#             model_name='notice',
#             name='user',
#             field=models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Zadanie dla'),
#       ),
    ]
