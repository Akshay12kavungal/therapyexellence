# Generated by Django 4.1.9 on 2023-07-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supervisor', '0006_supervisor_profile_about_supervisor_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supervisor_profile',
            name='Experience',
            field=models.CharField(default='', max_length=3),
        ),
    ]