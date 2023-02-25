from django.db import models
from apps.accounts.models import User
from django.urls import reverse

# Create your models here.
class UserPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True, null=True)
    photo =models.ImageField(upload_to="images/", blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    photo2 =models.ImageField(upload_to="images/", blank=True, null=True)
    body3 = models.TextField(blank=True, null=True)
    photo3 =models.ImageField(upload_to="images/", blank=True, null=True)
    body4 = models.TextField(blank=True, null=True)
    photo4 =models.ImageField(upload_to="images/", blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes')
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    userpost = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True,)

    def __str__(self):
        return '%s - %s' % (self.userpost.title, self.author)