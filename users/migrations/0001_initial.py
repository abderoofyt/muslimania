# Generated by Django 4.1 on 2022-08-25 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_name', models.CharField(max_length=20)),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, choices=[('m', 'Male'), ('f', 'Female')], null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('dod', models.DateField(blank=True, null=True)),
                ('job', models.CharField(blank=True, max_length=20, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('biography', models.CharField(blank=True, max_length=20, null=True)),
                ('stories', models.TextField(blank=True, null=True)),
                ('video', models.TextField(blank=True, null=True)),
                ('profile_link', models.ManyToManyField(blank=True, to='users.linkmodel')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
