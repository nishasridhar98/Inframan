# Generated by Django 2.1.1 on 2018-09-30 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proprietor', '0006_auto_20180930_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proprietor.Profile'),
        ),
    ]
