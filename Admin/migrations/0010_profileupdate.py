# Generated by Django 4.1.9 on 2023-05-31 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Admin.profile')),
            ],
        ),
    ]
