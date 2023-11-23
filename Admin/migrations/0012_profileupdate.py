# Generated by Django 4.1.9 on 2023-05-31 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0011_delete_profileupdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUpdate',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('First_Name', models.CharField(max_length=42)),
                ('Last_Name', models.CharField(max_length=42)),
                ('Username', models.CharField(max_length=42)),
                ('Email', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Admin.profile')),
            ],
        ),
    ]