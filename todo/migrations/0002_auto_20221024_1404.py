# Generated by Django 3.0.14 on 2022-10-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
