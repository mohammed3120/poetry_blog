from django.shortcuts import render
from .models import Post,Comment,Like,Reply
# Create your views here.
def home(request):
    context ={}
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
