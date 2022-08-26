# Generated by Django 4.1 on 2022-08-26 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_rename_bookmodel_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='writer',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stories.publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
