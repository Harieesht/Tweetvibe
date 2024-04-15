from django.conf import settings
from rest_framework import serializers
from .models import Tweet

TWEET_ACTION_OPTIONS=settings.TWEET_ACTION_OPTIONS

class TweetActionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    action=serializers.CharField()


    def validate_action(self,value):
        value=value.lower().strip() #"LIKE "->"like"
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action")
        return value



MAX_TWEET_LENGTH=settings.MAX_TWEET_LENGTH
class TweetSerializer(serializers.ModelSerializer):
    likes=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Tweet
        fields=['id','content','likes']
    def get_likes(self,tweet):
        return tweet.likes.count()
        
    def validate_content(self,value):
        if len(value)>MAX_TWEET_LENGTH:
            raise serializers.ValidationError("This tweet is too big.")
        return value
         