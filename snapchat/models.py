from django.db import models


class Profile(models.Model):
    token = models.CharField(max_length=32, primary_key=True)

    def __str__(self):
        return self.token


class Song(models.Model):
    token = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=150)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    visited = models.BooleanField(default=False)
    # song will be uploaded to MEDIA_ROOT/songs
    upload = models.FileField(upload_to='songs/')

    def __str__(self):
        return self.name
