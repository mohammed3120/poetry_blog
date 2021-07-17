from django.shortcuts import render
from .models import Post,Comment,Like,Reply
from profiles.models import Profile
from django.db.models import Count
# Create your views here.
def home(request):
    maxLikesPosts = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')   
    maxLikesPost = maxLikesPosts[0]
    latestPosts = Post.objects.order_by('-created')[:4]
    posts_count = maxLikesPosts.count()
    commnets_count = Comment.objects.count()
    likes_count = Like.objects.count()
    profiles_count = Profile.objects.count()
    context ={'maxLikesPosts':maxLikesPosts[:4], 'maxLikesPost':maxLikesPost, 'latestPosts':latestPosts,
    'posts_count':posts_count, 'commnets_count':commnets_count, 'likes_count': likes_count, 'profiles_count':profiles_count}
    return render(request, 'poetries\home.html',context)

def poetry_view(request):
    poetries = Post.objects.filter(post_type = 'poetry')
    context ={'poetries':poetries}
    return render(request, 'poetries\poetry.html',context)

def p_reflections(request):
    reflections = Post.objects.filter(post_type = 'reflection')
    context ={'reflections':reflections}
    return render(request, 'poetries\p_reflections.html',context)


def stories(request):
    stories = Post.objects.filter(post_type = 'real story')
    context ={'stories':stories}
    return render(request, 'poetries\stories.html',context)

def i_read_you_view(request):
    posts = Post.objects.filter(post_type = 'I read you')
    context ={'posts':posts}
    return render(request, 'poetries\i_read_you.html',context)
