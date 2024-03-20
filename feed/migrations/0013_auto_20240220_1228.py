# Generated by Django 3.2.16 on 2024-02-20 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0012_auto_20240218_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_de_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
