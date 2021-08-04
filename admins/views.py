from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from poetries.models import Post
from profiles.models import Profile
from profiles.forms import ProfileForm
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
    users = User.objects.filter(is_staff = False)
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

def delete_post_view(request, pk):
    post = Post.objects.get(pk = pk)
    post_type = post.post_type
    post.delete()
    return HttpResponseRedirect(reverse('dashboard:dashboard_posts',args=(post_type,)))

def delete_all_posts_view(request, post_type):
    if request.user.is_staff:
        posts = Post.objects.filter(post_type = post_type)
        posts.delete()
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

#CRUD Post
def dashboard_profile_view(request, pk):
    user = User.objects.get(pk = pk)
    profile = Profile.objects.get(user = user)
    context = {'object': profile}
    return render(request, 'admins\dashboard_Profile.html', context)

def delete_user_view(request, pk):
    user = User.objects.get(pk = pk)
    user.delete()
    return HttpResponseRedirect(reverse('dashboard:dashboard_users'))

def delete_all_users_view(request):
    if request.user.is_staff:
        users = User.objects.filter(is_staff = False)
        users.delete()
    return HttpResponseRedirect(reverse('dashboard:dashboard_users'))

def dashboard_update_profile_view(request, pk):
    profile = Profile.objects.get(pk = pk)
    form = ProfileForm(instance = profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES , instance = profile )
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard:dashboard_profile', args=(profile.user.id,)))
    return render(request, 'admins\dashboard_profile_edit.html', {'form': form})







