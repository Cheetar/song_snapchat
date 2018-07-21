import binascii
import os

from django.db import models


def generate_token():
    return binascii.hexlify(os.urandom(16)).decode()


class Snap(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name is None:
            return self.token
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        return super(Snap, self).save(*args, **kwargs)


class Song(models.Model):

    def get_random_song_path(instance, filename):
        # song will be uploaded to MEDIA_ROOT/songs/<random-32-hex>.<ext>
        ext = filename.split(".")[-1]
        token = generate_token()
        return 'songs/{0}.{1}'.format(token, ext)

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    token = models.CharField(max_length=32, blank=True)
    snap = models.ForeignKey('Snap', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField(default=False)
    listened_on = models.DateTimeField(blank=True, null=True)
    # song will be uploaded to MEDIA_ROOT/songs
    upload = models.FileField(upload_to=get_random_song_path)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        return super(Song, self).save(*args, **kwargs)
