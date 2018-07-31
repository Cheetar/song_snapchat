import os.path

from django.test import TestCase

from snapchat.yt_download import download_mp3, is_url_valid


class YtDownloadTestCase(TestCase):

    def test_validating_url(self):
        self.assertTrue(is_url_valid("https://www.youtube.com/watch?v=nky4me4NP70"))
        self.assertTrue(is_url_valid("https://www.youtube.com/watch?v=BaW_jenozKc"))
        self.assertFalse(is_url_valid("https://www.youtube.com/watch?v=BaW_jenozK"))
        self.assertFalse(is_url_valid("https://google.com/example_invalid_url"))
        self.assertFalse(is_url_valid("qwerty"))
        self.assertFalse(is_url_valid("!@#$%^&*()_+"))

    def test_downloading_songs(self):
        path = download_mp3("https://www.youtube.com/watch?v=BaW_jenozKc")
        self.assertNotEqual(path, None)
        filename = path.split('/')[-1]
        ext = filename.split('.')[-1]
        self.assertTrue(os.path.isfile(path))
        self.assertEqual(ext, "mp3")

        path = download_mp3("qwerty")
        self.assertEqual(path, None)
