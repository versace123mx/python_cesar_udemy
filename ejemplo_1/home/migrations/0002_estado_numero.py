# Generated by Django 3.0.5 on 2024-02-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estado',
            name='numero',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
