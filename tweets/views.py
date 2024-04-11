from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse,Http404
from .models import *
from .forms import TweetForm
from django.conf import settings
from .serializers import TweetSerializer
 

ALLOWED_HOSTS=settings.ALLOWED_HOSTS

#homepage view
def home_page(request,*args,**kwargs):
    return render(request,'pages/home.html',{},status=200)




#tweetlistview(Returns tweets in json data)
def tweet_list_view(request,*args,**kwargs):
    queryset=Tweet.objects.all()
    tweets_list=[tweet.serialize() for tweet in queryset]
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

#usermade is_ajax function because it didnt work on my machine
def is_ajax(request):
  #return request.headers['X-Requested-With'] == 'XMLHttpRequest'
  return True

#tweet creation view
#rendering form in homepage instead seperate "form.html" page
#next_url indicates current homepage url
#pure django view
def tweet_create_view_pure_django(request,*args,**kwargs):
    user=request.user
    if not request.user.is_authenticated:
        user=None
        if is_ajax(request):
            return JsonResponse({},status=401)
        return redirect(settings.LOGIN_URL)
    form=TweetForm(request.POST or None)
    next_url=request.POST.get('next') or None
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user=user 
        obj.save()
        if is_ajax(request):
            return JsonResponse(obj.serialize(),status=201)
        if next_url != None:
            return redirect(next_url)
        form=TweetForm()
    if form.errors:
        if is_ajax(request):
            return JsonResponse(form.errors,status=400)
    return render(request,'components/form.html',context={"form":form})



def tweet_create_view(request,*args,**kwargs):
    data=request.POST or None
    serializer=TweetSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data,status=201)
    return JsonResponse({},status=400)
















