from django.contrib import admin
from .models import Post,Comment,Reply,Like,Sentiment,Color
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Like)
admin.site.register(Sentiment)
admin.site.register(Color)