from django import forms
from .models import Tweet

PROHIBITED_WORDS = ['shit', 'fuck', 'bobo']

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data['content']
        for word in PROHIBITED_WORDS:
            if word.lower() in content.lower():
                raise forms.ValidationError("Your tweet contains a prohibited word.")
        return content