# Generated by Django 2.0.7 on 2018-07-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapchat', '0006_auto_20180712_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='token',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
