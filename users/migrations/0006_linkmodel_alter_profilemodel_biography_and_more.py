# Generated by Django 4.1 on 2022-08-24 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_profile_profilemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='biography',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='ethnicity',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='job',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
