# Generated by Django 4.2.6 on 2023-12-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0010_remove_post_image_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
    ]
