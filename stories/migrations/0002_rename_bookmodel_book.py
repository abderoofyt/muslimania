# Generated by Django 4.1 on 2022-08-25 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookModel',
            new_name='Book',
        ),
    ]