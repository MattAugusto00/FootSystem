# Generated by Django 4.2.5 on 2023-11-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='destiny_club',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='origin_club',
            field=models.CharField(max_length=255),
        ),
    ]
