# Generated by Django 3.2.16 on 2024-04-17 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_rename_clubs_info_clubs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_clubs',
            name='secretaire2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='info_clubs',
            name='tresorier2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='info_clubs',
            name='vp3',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
