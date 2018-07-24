from django import forms

from .models import Song


class SongAddForm(forms.ModelForm):

    name = forms.CharField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Song
        fields = ('name', 'description', 'upload',)
