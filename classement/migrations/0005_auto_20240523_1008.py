# Generated by Django 3.2.16 on 2024-05-23 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classement', '0004_club'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='Utilisateur',
        ),
    ]
