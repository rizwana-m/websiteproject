# Generated by Django 4.1.7 on 2023-02-24 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newdemoapp', '0002_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='image',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
