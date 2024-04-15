from django.contrib import admin

# Register your models herefrom 
from .models import Tweet,TweetLikes

class TweetLikeAdmin(admin.TabularInline):
    model=TweetLikes


class TweetAdmin(admin.ModelAdmin):
    inlines=[TweetLikeAdmin]
    list_display=['__str__','user']
    search_fields=['user__username','user__email']
    class Meta:
        model=Tweet


admin.site.register(Tweet,TweetAdmin)