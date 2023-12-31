# Generated by Django 4.1.9 on 2023-07-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0005_rename_profile_supervisor_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor_profile',
            name='About',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='supervisor_profile',
            name='Address',
            field=models.CharField(default='', max_length=42),
        ),
        migrations.AddField(
            model_name='supervisor_profile',
            name='Age',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AddField(
            model_name='supervisor_profile',
            name='Degree',
            field=models.CharField(default='', max_length=42),
        ),
        migrations.AddField(
            model_name='supervisor_profile',
            name='Designation',
            field=models.CharField(default='', max_length=42),
        ),
        migrations.AddField(
            model_name='supervisor_profile',
            name='Gender',
            field=models.CharField(default='', max_length=42),
        ),
    ]
