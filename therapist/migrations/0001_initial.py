# Generated by Django 4.1.9 on 2023-05-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=42)),
                ('Last_Name', models.CharField(max_length=42)),
                ('Username', models.CharField(max_length=42)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.IntegerField(default=0)),
                ('Password', models.CharField(max_length=42)),
                ('Confirm_Password', models.CharField(max_length=42)),
                ('otp', models.CharField(blank=True, editable=False, max_length=6, null=True)),
                ('token', models.CharField(blank=True, max_length=10, null=True)),
                ('uid', models.CharField(editable=False, max_length=4, unique=True)),
            ],
        ),
    ]
