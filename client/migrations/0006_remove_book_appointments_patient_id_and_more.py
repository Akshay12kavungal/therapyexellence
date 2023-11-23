# Generated by Django 4.1.9 on 2023-06-12 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_book_appointments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_appointments',
            name='Patient_id',
        ),
        migrations.AlterField(
            model_name='book_appointments',
            name='Appointment_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
