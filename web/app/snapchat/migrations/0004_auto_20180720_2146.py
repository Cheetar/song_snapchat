# Generated by Django 2.0.7 on 2018-07-20 21:46

from django.db import migrations, models
import snapchat.models


class Migration(migrations.Migration):

    dependencies = [
        ('snapchat', '0003_auto_20180718_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload',
            field=models.FileField(upload_to=snapchat.models.Song.get_random_song_path),
        ),
    ]
