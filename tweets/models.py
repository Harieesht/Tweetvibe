from django.db import models


#tweet model
class Tweet(models.Model):
    content=models.TextField(blank=True,null=True)
    image=models.FileField(upload_to='images/',blank=True,null=True)
    












