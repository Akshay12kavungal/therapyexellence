# Generated by Django 4.1.9 on 2023-06-09 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0004_support'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='Therapist_Profile',
        ),
    ]
