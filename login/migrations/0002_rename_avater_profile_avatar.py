# Generated by Django 4.1.2 on 2022-11-30 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avater',
            new_name='avatar',
        ),
    ]
