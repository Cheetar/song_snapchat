from django.core.files import File
from django.db import models

from .utils import generate_token
from .validators import FileValidator
from .yt_download import download_mp3

MAX_SONG_SIZE_MB = 20


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
                                              'audio/basic',
                                              'auido/L24',
                                              'audio/mid',
                                              'audio/mp4',
                                              'audio/x-aiff',
                                              'audio/x-mpegurl',
                                              'audio/vnd.rn-realaudio',
                                              'audio/vorbis',
                                              'audio/vnd.wav',
                                              ))


class Snap(models.Model):
    token = models.CharField(max_length=32, blank=True, unique=True,
                             primary_key=True)
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

    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=500, blank=True)
    token = models.CharField(max_length=32, blank=True, unique=True,
                             primary_key=True)
    snap = models.ForeignKey('Snap', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    visited = models.BooleanField(default=False)
    listened_on = models.DateTimeField(blank=True, null=True)
    # song will be uploaded to MEDIA_ROOT/songs
    upload = models.FileField(upload_to=get_random_song_path,
                              validators=[song_validator])
    youtube_url = models.CharField(max_length=150, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = generate_token()

        if self.youtube_url and not self.upload:
            path = download_mp3(self.youtube_url)
            filename = path.split('/')[-1]

            song = open(path, encoding='utf-8')
            x = File(song)
            self.upload.save(filename, x)
            song.close()

        return super(Song, self).save(*args, **kwargs)
