# Generated by Django 2.1.1 on 2018-09-30 11:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proprietor', '0008_auto_20180930_1558'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tenants',
            new_name='Tenant',
        ),
    ]