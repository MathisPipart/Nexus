# Generated by Django 4.2.6 on 2023-11-23 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
