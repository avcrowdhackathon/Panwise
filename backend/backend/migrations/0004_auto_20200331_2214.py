# Generated by Django 3.0.4 on 2020-03-31 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200331_2142'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='PastOrder',
        ),
        migrations.AlterModelTable(
            name='pastorder',
            table='PastOrder',
        ),
    ]
