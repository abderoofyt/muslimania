# Generated by Django 4.1 on 2022-08-29 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='story',
            old_name='story',
            new_name='text',
        ),
    ]
