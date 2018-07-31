from django.test import TestCase
from django.urls import reverse

from snapchat.models import Snap, Song
from snapchat.utils import generate_token


class SnapTestCase(TestCase):

    @classmethod
    def setUpTestData(self):
        video_url_1 = 'https://www.youtube.com/watch?v=BaW_jenozKc'
        video_url_2 = 'https://www.youtube.com/watch?v=nky4me4NP70'

        snap = Snap(name='test snap', token=generate_token(),
                    finished_editing=True)
        song1 = Song(name='song1', token=generate_token(), snap=snap,
                     youtube_url=video_url_1)
        song2 = Song(name='song2', token=generate_token(), snap=snap,
                     youtube_url=video_url_1)
        song3 = Song(name='song3', token=generate_token(), snap=snap,
                     youtube_url=video_url_2)

        snap.save()
        song1.save()
        song2.save()
        song3.save()

    def test_token_length(self):
        snap = Snap.objects.get(name='test snap')
        songs = Song.objects.filter(snap=snap)
        self.assertEqual(len(snap.token), 32)
        for song in songs:
            self.assertEqual(len(song.token), 32)

    def test_song_not_available_after_listening(self):
        snap = Snap.objects.get(name='test snap')
        songs = Song.objects.filter(snap=snap)
        for song in songs:
            self.assertFalse(song.visited)
            url = reverse('song', args=[song.token])
            response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'snapchat/song.html')
            self.assertContains(response, "gramophone")

            song.refresh_from_db()
            self.assertTrue(song.visited)
            url = reverse('song', args=[song.token])
            response = self.client.get(url, follow=True)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'snapchat/song.html')
            self.assertContains(response, "Song was already played")

    def test_index(self):
        url = reverse('index')
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertContains(response, "Please insert your token")

    def test_token_properly_redirects_to_snap(self):
        snap = Snap.objects.get(name='test snap')
        snap_token = snap.token
        url = reverse('snap', args=[snap_token])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snapchat/snap.html')
        self.assertContains(response, "song1")
        self.assertContains(response, "song2")
        self.assertContains(response, "song3")
