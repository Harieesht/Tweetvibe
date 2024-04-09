from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,Http404
from .models import *
from .forms import TweetForm
from django.conf import settings

ALLOWED_HOSTS=settings.ALLOWED_HOSTS

#homepage view
def home_page(request,*args,**kwargs):
    return render(request,'pages/home.html',{},status=200)




#tweetlistview(Returns tweets in json data)
def tweet_list_view(request,*args,**kwargs):
    queryset=Tweet.objects.all()
    tweets_list=[{"id":tweet.id,"content":tweet.content,"likes":12} for tweet in queryset]
    data={
        "isUser":False,
        "response":tweets_list,
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

#tweet creation view
#rendering form in homepage instead seperate "form.html" page
#next_url indicates current homepage url
def tweet_create_view(request,*args,**kwargs):
    form=TweetForm(request.POST or None)
    next_url=request.POST.get('next') or None
    print(next_url)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect(next_url)
        form=TweetForm()
    return render(request,'components/form.html',context={"form":form})