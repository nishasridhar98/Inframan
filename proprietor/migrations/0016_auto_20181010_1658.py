# Generated by Django 2.1.1 on 2018-10-10 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proprietor', '0015_auto_20181010_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='properties',
            new_name='prop',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='tenant',
            new_name='user',
        ),
    ]
