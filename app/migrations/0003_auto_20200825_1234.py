# Generated by Django 3.0.4 on 2020-08-25 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200825_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='engineer',
            old_name='firstname',
            new_name='CUSTOMER',
        ),
    ]
