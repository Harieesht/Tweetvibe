from django.db import models
from django.conf import settings



User=settings.AUTH_USER_MODEL  #using inbuilt user model

class TweetLikes(models.Model):   #tweetlike(association class)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    tweet=models.ForeignKey("Tweet",on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    


#tweet model
class Tweet(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    content=models.TextField(blank=True,null=True)
    likes=models.ManyToManyField(User,related_name='tweet_user',blank=True,through=TweetLikes ) 
    image=models.FileField(upload_to='images/',blank=True,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['-id']
    
    def serialize(self):
        return{
            "id":self.id,
            "content":self.content,
            "likes":12
        }
    
    
        











