# Generated by Django 4.1.4 on 2023-01-20 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_accountmodel_mysharings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountmodel',
            name='mySharings',
        ),
    ]
