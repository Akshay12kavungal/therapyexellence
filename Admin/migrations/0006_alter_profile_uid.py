# Generated by Django 4.1.9 on 2023-05-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.IntegerField(editable=False, max_length=4, unique=True),
        ),
    ]
