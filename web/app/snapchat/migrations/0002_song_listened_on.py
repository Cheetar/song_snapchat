# Generated by Django 2.0.7 on 2018-07-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapchat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listened_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
