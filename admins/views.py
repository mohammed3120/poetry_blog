from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from poetries.models import Post
from profiles.models import Profile
from django.views.generic import DetailView
from poetries.forms import PostForm
from django.urls import reverse
from django.template.loader import render_to_string
from django.contrib.auth.models import User

# Create your views here.

def dashboard_view(request):
    context ={}
    return render(request,'admins\dashboard.html', context)

def dashboard_posts_view(request,post_type):
    posts = Post.objects.filter(post_type = post_type)
    sentiments = ['happy', 'sad', 'normal', 'action', 'romance']
    context ={'posts':posts, 'sentiments':sentiments, 'post_type': post_type}
    return render(request, 'admins\dashboard_posts.html',context)



def dashboard_users_view(request):
    users = User.objects.all()
    context ={'users':users}
    return render(request,'admins\dashboard_users.html', context)
#CRUD Post
class PostDetailView(DetailView):
    model = Post
    template_name = "admins\dashboard_Post.html"

def create_post_view(request, post_type):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        author = Profile.objects.get(user=request.user)
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = author
            instance.post_type = post_type
            instance.save()
            return HttpResponseRedirect(reverse('dashboard:dashboard_posts', args=(post_type,)))
    return render(request, 'admins\dashboard_create.html', {'form': form})

def update_post_view(request, pk):
    post = Post.objects.get(pk = pk)
    form = PostForm(instance = post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:dashboard_posts', args=(post.post_type,)))
    return render(request, 'admins\dashboard_create.html', {'form': form})

def delete_post_view(self, pk):
    post = Post.objects.get(pk = pk)
    post_type = post.post_type
    post.delete()
    return HttpResponseRedirect(reverse('dashboard:dashboard_posts',args=(post_type,)))





def dashboard_filter_data_view(request,post_type):
    sentiments = request.GET.getlist('sentiment[]')
    title = request.GET['title']
    posts = Post.objects.filter(post_type = post_type)
    if len(sentiments)>0:
        posts = posts.filter(sentiment_type__in = sentiments).distinct()
    if title != "":
        posts = posts.filter(title__contains=title)
    t=render_to_string('admins\dashboard_post_list.html',{'data':posts})
    return JsonResponse({'data': t})

def dashboard_filter_user_view(request):
    username = request.GET['username']
    users = User.objects.all()
           
    if username != "":
        users = users.filter(username__contains = username).distinct()
    t=render_to_string('admins\dashboard_user_list.html',{'users':users})
    return JsonResponse({'users': t})






