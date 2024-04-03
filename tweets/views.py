from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

#homepage view
def home_page(request,*args,**kwargs):
    print(args,kwargs)
    return HttpResponse("<h1>Hello world<h1>")
    
#tweet detail view
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    tweet=get_object_or_404(Tweet,id=tweet_id)
    return HttpResponse(f"<h1>Hello {tweet_id}-{tweet.content}<h1>")