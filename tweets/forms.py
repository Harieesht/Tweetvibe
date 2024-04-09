from django import forms
from. models import Tweet
MAX_TWEET_LENGTH=300
#Forms for creating a tweet
class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['content']

    def clean_content(self):
        content=self.cleaned_data.get('content')
        if len(content)>MAX_TWEET_LENGTH:
            raise forms.ValidationError("This tweet is too big.")
        return content