from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse,Http404
from .models import *

#homepage view
def home_page(request,*args,**kwargs):
    return render(request,'pages/home.html',{},status=200)




#tweetlistview(Returns tweets in json data)
def tweet_list_view(request,*args,**kwargs):
    queryset=Tweet.objects.all()
    tweets_list=[{"id":tweet.id,"content":tweet.content} for tweet in queryset]
    data={
        "isUser":False,
        "response":tweets_list
    }
    return JsonResponse(data)




#tweet detail view
#REST API VIEW{Returning tweet in json data}
def tweet_detail_view(request,tweet_id,*args,**kwargs):
    data={
        "id":tweet_id,
    }
    status=200
    try:
        tweet=Tweet.objects.get(id=tweet_id)
        data['content']=tweet.content
    except:
        data['content']='Tweet doesnt exist'
        status=404
    return JsonResponse(data,status=status)

