import binascii
import os

from django.db import models


def generate_token():
    return binascii.hexlify(os.urandom(16)).decode()


def restart_songs():
    for song in Song.objects.all():
        song.visited = False
        song.save()


class Snap(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.name is None:
            return self.token
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        return super(Snap, self).save(*args, **kwargs)


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=500, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True)
    snap = models.ForeignKey('Snap', on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    listened_on = models.DateTimeField(blank=True, null=True)
    # song will be uploaded to MEDIA_ROOT/songs
    upload = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        return super(Song, self).save(*args, **kwargs)
