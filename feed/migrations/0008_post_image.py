# Generated by Django 4.2.6 on 2023-11-23 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0007_remove_post_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
