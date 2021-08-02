from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from profiles.models import Profile
# Create your models here.
POST_TYPE_CHOICES = (
    ('poetry', 'poetry'),
    ('reflection', 'reflection'),
    ('real_story', 'real_story'),
    ('I_read_you', 'I_read_you'),
)
SENTIMENT_TYPE_CHOICES = (
    ('happy','happy'),
    ('sad','sad'),
    ('normal','normal'),
    ('action','action'),
    ('romance','romance'),
)
CHECKED= (
    ('checked','checked'),
    ('',''),
)

BG_COLORS =(
    ('default_color_bg','default_color_bg'),
    ('purple_color_bg', 'purple_color_bg'),
)    
THEME_COLORS = (
    ('default_colors_theme','default_colors_theme'),
    ('green_colors_theme','green_colors_theme'),
    ('golden_colors_theme','golden_colors_theme'),
    ('bold_brown_colors_theme','bold_brown_colors_theme'),
    ('light_blue_colors_theme','light_blue_colors_theme'),
    ('black_colors_theme','black_colors_theme'),
    ('light_green_colors_theme','light_green_colors_theme'),
    ('oily_colors_theme','oily_colors_theme'),
    ('blue_colors_theme','blue_colors_theme'),
    ('blue_colors_theme','blue_colors_theme'),
)
class Color(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    bg_color = models.CharField(
        max_length= 50,
        choices=BG_COLORS,
        default='default_color_bg',
    )
    theme_color = models.CharField(
        max_length= 50,
        choices=THEME_COLORS,
        default='default_colors_theme',
    )

 
class Sentiment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    filterPostsType = models.CharField(
        max_length= 20,
        choices=POST_TYPE_CHOICES,
        default='default_color_bg',
    )
    happy = models.CharField(max_length= 20,
        choices=CHECKED,
        default='',
        blank = True,
    )
    sad = models.CharField(max_length= 20,
        choices=CHECKED,
        default='',
        blank = True,
    )
    normal = models.CharField(max_length= 20,
        choices=CHECKED,
        default='',
        blank = True,
    )
    action = models.CharField(max_length= 20,
        choices=CHECKED,
        default='',
        blank = True,
    )
    romance = models.CharField(max_length= 20,
        choices=CHECKED,
        default='',
        blank = True,
    )
class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    post_type = models.CharField(
        max_length= 20,
        choices=POST_TYPE_CHOICES,
        default='poetry',
    )
    sentiment_type = models.CharField(
        max_length= 20,
        choices=SENTIMENT_TYPE_CHOICES,
        default='normal',
    )
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    def get_comments(self):
        comments = self.comment_set.all()
        return comments
    def get_likes(self):
        likes = self.like_set.all()
        return likes 
    def get_users(self):
        users = []
        likes = self.like_set.all()
        for like in likes:
            users.append(like.profile.user.username)
        return users  

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.profile)
    
    def get_replies(self):
        replies = self.reply_set.all()
        return replies
    
    


class Reply(models.Model):
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.profile)


class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{} like  {}'.format(self.profile.user.username, self.post.title)

    class Meta:
        unique_together = ('post', 'profile',)

    

