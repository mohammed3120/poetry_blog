from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from profiles.models import Profile
# Create your models here.
POST_TYPE_CHOICES = (
    ('poetry', 'poetry'),
    ('reflection', 'reflection'),
    ('real story', 'real story'),
    ('I read you', 'I read you'),
)
SENTIMENT_TYPE_CHOICES = (
    ('happy','happy'),
    ('sad','sad'),
    ('normal','normal'),
    ('action','action'),
    ('romance','romance'),
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
    created = models.DateTimeField(blank=True)
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

    

