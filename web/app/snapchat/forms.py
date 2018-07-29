from django import forms

from .models import Song
from .yt_download import is_url_valid


class SongAddForm(forms.ModelForm):

    name = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    upload = forms.FileField(required=False)
    youtube_url = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'size': '40', 'placeholder': 'http://www.youtube.com/watch?v='}))

    class Meta:
        model = Song
        fields = ('name', 'description', 'upload', 'youtube_url')

    def clean_youtube_url(self):
        url = self.cleaned_data['youtube_url']
        if url != '' and not is_url_valid(url):
            raise forms.ValidationError("Invalid url")

        return url

    def clean(self):
        cleaned_data = super().clean()
        upload = cleaned_data.get("upload")
        url = cleaned_data.get("youtube_url")

        if not url and not upload:
            # If user didn't enter youtube_url nor uploaded a file.
            raise forms.ValidationError(
                "Please either enter a valid youtube url or upload a file"
            )

        if url and upload:
            """ If user entered both youtube_url and uploaded a file, we don't
                which one should we use.
            """
            raise forms.ValidationError("Enter youtube url OR upload a file")
