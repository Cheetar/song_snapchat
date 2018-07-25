import binascii
import os

from django.db import models

from .validators import FileValidator

MAX_SONG_SIZE_MB = 20


def generate_token():
    return binascii.hexlify(os.urandom(16)).decode()


class Snap(models.Model):
    token = models.CharField(max_length=32, blank=True, unique=True, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    finished_editing = models.BooleanField(default=False)

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

    song_validator = FileValidator(max_size=1024 * 1024 * MAX_SONG_SIZE_MB,
                                   content_types=('application/mp3',
                                                  'application/x-mp3',
                                                  'audio/aac',
                                                  'audio/mpeg',
                                                  'audio/mp3',
                                                  'audio/wav',
                                                  'audio/x-wav',
                                                  'audio/ogg',
                                                  'audio/webm',
                                                  'audio/3gpp',
                                                  'audio/3gpp2',
                                                  ))

    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=500, blank=True)
    token = models.CharField(max_length=32, blank=True, unique=True, primary_key=True)
    snap = models.ForeignKey('Snap', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField(default=False)
    listened_on = models.DateTimeField(blank=True, null=True)
    # song will be uploaded to MEDIA_ROOT/songs
    upload = models.FileField(upload_to=get_random_song_path,
                              validators=[song_validator])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()
        return super(Song, self).save(*args, **kwargs)
