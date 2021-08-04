from django.shortcuts import render,redirect
from .models import Post,Comment,Like,Reply,Sentiment,Color
from profiles.models import Profile
from profiles.forms import ProfileForm
from django.db.models import Count
from django.template.loader import render_to_string
from django.http import JsonResponse
from accounts.forms import CreateUserForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('poetries:home')
    else:
        form = CreateUserForm()
        if request.method =="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('poetries:login')
        context ={'form':form}
        return render(request, 'accounts\signup.html',context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('poetries:home')
    else:
        if request.method =="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username,password)
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect('poetries:home')
            else:
                # messages.info(request,'User name or password is incorect !!')
                print(user)
    context ={}
    return render(request, 'accounts\login.html',context)

@login_required(login_url='poetries:login')
def logout_view(request):
    logout(request)
    return redirect('poetries:login')
@login_required(login_url='poetries:login')
def home(request):
    maxLikesPosts = Post.objects.annotate(like_count=Count('like')).order_by('-like_count')   
    maxLikesPost = maxLikesPosts[0]
    latestPosts = Post.objects.order_by('-created')[:4]
    posts_count = maxLikesPosts.count()
    commnets_count = Comment.objects.count()
    likes_count = Like.objects.count()
    profiles_count = Profile.objects.count()
    #Colors
    profile = Profile.objects.get(user = request.user)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    
    bg = usercolors.bg_color
    theme = usercolors.theme_color
    print(bg)
    print(theme)
    #context
    context ={'maxLikesPosts':maxLikesPosts[:4], 'maxLikesPost':maxLikesPost, 'data':latestPosts,
    'posts_count':posts_count, 'commnets_count':commnets_count,
     'likes_count': likes_count, 'profiles_count':profiles_count,
     'bg':bg, 'theme':theme}
    return render(request, 'poetries\home.html',context)

@login_required(login_url='poetries:login')
def posts_view(request,post_type):
    posts = Post.objects.filter(post_type = post_type)
    profile = Profile.objects.get(user = request.user)
    sentimentss = Sentiment.objects.get_or_create(profile = profile, filterPostsType = post_type)[0]
    print(sentimentss.happy,sentimentss.sad, sentimentss.normal, sentimentss.action, sentimentss.romance)
    sents = []
    if sentimentss.happy !='':
        sents.append('happy')
    if sentimentss.sad !='':
        sents.append('sad')
    if sentimentss.normal !='':
        sents.append('normal')
    if sentimentss.action !='':
        sents.append('action')
    if sentimentss.romance !='':
        sents.append('romance')
    if len(sents)>0:
        posts = posts.filter(sentiment_type__in = sents).distinct()
    #Colors
    profile = Profile.objects.get(user = request.user)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    
    bg = usercolors.bg_color
    theme = usercolors.theme_color
    print(bg)
    print(theme)

    sentiments = {'happy':sentimentss.happy, 'sad':sentimentss.sad, 'normal':sentimentss.normal, 'action':sentimentss.action, 'romance':sentimentss.romance}
    context ={'data':posts, 'sentiments':sentiments, 'post_type': post_type,'userFilter':sentimentss, 'bg':bg, 'theme':theme}
    return render(request, 'poetries\posts.html',context)



@login_required(login_url='poetries:login')
@csrf_exempt
def filter_data(request,post_type):
    sentiments = request.GET.getlist('sentiment[]')
    profile = Profile.objects.get(user = request.user)
    sentimentss = Sentiment.objects.get_or_create(profile = profile, filterPostsType = post_type)[0]
    if 'happy' in sentiments:
        sentimentss.happy = 'checked'
    else:
        sentimentss.happy = ''
    if 'sad' in sentiments:
        sentimentss.sad = 'checked'
    else:
        sentimentss.sad = ''
    if 'normal' in sentiments:
        sentimentss.normal = 'checked'
    else:
        sentimentss.normal = ''
    if 'action' in sentiments:
        sentimentss.action = 'checked'
    else:
        sentimentss.action = ''
    if 'romance' in sentiments:
        sentimentss.romance = 'checked'
    else:
        sentimentss.romance = ''
    sentimentss.save()
    posts = Post.objects.filter(post_type = post_type)
    if len(sentiments)>0:
        posts = posts.filter(sentiment_type__in = sentiments).distinct()
    t=render_to_string('poetries\post_list.html',{'data':posts})
    return JsonResponse({'data': t})

@csrf_exempt
def likeTogle(request,pk):
    print("pk",pk)
    liked = request.GET['liked']
    print(liked) 
    profile = Profile.objects.get(user = request.user)
    post = Post.objects.get(pk = pk)
    like = Like.objects.filter(post = post, profile = profile)
    print(like)
    if  like.exists():
        # user likes post
        like.delete()
        print("ddddddddddddddddddddddddddddddddddddddddddddddddd")
        liked = "Like"
        
    else:
        # user likes post
        like = Like.objects.create(post = post, profile = profile)
        like.save()
        print('sssssssssssssssssssssssssssssssssssssss')
        liked = "Liked"
        
    likeData = {'liked':liked}   
    return JsonResponse({'likeData':likeData})


#CRUD Comment
@csrf_exempt
def add_comment_view(request, pk):
    post = Post.objects.get(pk = pk)
    profile = Profile.objects.get(user=request.user)
    commentValue =  request.GET['comment']
    if commentValue != "":
        comment = Comment.objects.create(post = post, profile = profile, body = commentValue)
        comment.save()
        t=render_to_string('poetries\one_comment.html',{'comment':comment})
        return JsonResponse({'comment': t})
    else:
        return JsonResponse({})

#CRUD Reply
@csrf_exempt
def add_reply_view(request, pk):
    comment = Comment.objects.get(pk = pk)
    profile = Profile.objects.get(user=request.user)
    replyValue =  request.GET['reply']
    if replyValue != "":
        reply = Reply.objects.create(comment = comment, profile = profile, body = replyValue)
        reply.save()
        t=render_to_string('poetries\one_reply.html',{'reply':reply})
        return JsonResponse({'reply': t})
    else:
        return JsonResponse({})

def change_colors(request,theme):
    color = request.GET[theme]
    profile = Profile.objects.get(user = request.user)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    if theme =="bg":
        usercolors.bg_color = color
        usercolors.save()
    elif theme == "theme":
        usercolors.theme_color = color
        usercolors.save()
    else:
        pass
    
    return JsonResponse({})
    # profile = Profile.objects.get(user = request.user)

#CRUD Post
def profile_view(request, pk):
    user = User.objects.get(pk = pk)
    profile = Profile.objects.get(user = user)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    
    bg = usercolors.bg_color
    theme = usercolors.theme_color
    context = {'profile': profile, 'bg': bg, 'theme':theme}
    return render(request, 'poetries\profile.html', context)


def update_profile_view(request, pk):
    profile = Profile.objects.get(pk = pk)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    
    bg = usercolors.bg_color
    theme = usercolors.theme_color
    form = ProfileForm(instance = profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES , instance = profile )
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('poetries:profile_view', args=(profile.user.id,)))
    return render(request, 'poetries\profile_update.html', {'form': form, 'bg': bg, 'theme':theme})


def writer_profile_view(request,pk):
    super_user = User.objects.filter(is_staff = True)[0]
    super_user_profile = Profile.objects.get(user = super_user)
    user = User.objects.get(pk = pk)
    profile = Profile.objects.get(user = user)
    usercolors = Color.objects.get_or_create(profile = profile)[0]
    
    bg = usercolors.bg_color
    theme = usercolors.theme_color
    context = {'profile': super_user_profile, 'bg': bg, 'theme':theme}
    return render(request, 'poetries\writer_profile.html', context)

