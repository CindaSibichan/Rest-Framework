# Generated by Django 5.0.6 on 2024-06-07 07:06

import myapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_personuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='personuser',
            managers=[
                ('objects', myapp.models.PersonUserManager()),
            ],
        ),
       
    ]
