# Generated by Django 2.0.7 on 2018-07-24 21:27

from django.db import migrations, models
import django.db.models.deletion
import snapchat.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snap',
            fields=[
                ('token', models.CharField(blank=True, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('finished_editing', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('token', models.CharField(blank=True, max_length=32, primary_key=True, serialize=False, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('visited', models.BooleanField(default=False)),
                ('listened_on', models.DateTimeField(blank=True, null=True)),
                ('upload', models.FileField(upload_to=snapchat.models.Song.get_random_song_path)),
                ('snap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snapchat.Snap')),
            ],
        ),
    ]
