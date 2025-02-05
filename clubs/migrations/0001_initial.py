# Generated by Django 3.2.16 on 2024-04-16 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clubs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('banniere', models.ImageField(upload_to='clubs/')),
                ('photo', models.ImageField(upload_to='clubs/')),
                ('president', models.CharField(max_length=50)),
                ('vp1', models.CharField(max_length=50)),
                ('vp2', models.CharField(max_length=50)),
                ('vp3', models.CharField(max_length=50)),
                ('secretaire', models.CharField(max_length=50)),
                ('secretaire2', models.CharField(max_length=50)),
                ('tresorier', models.CharField(max_length=50)),
                ('tresorier2', models.CharField(max_length=50)),
            ],
        ),
    ]
