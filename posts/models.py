from django.db import models
from django.utils.timesince import timesince


class Post(models.Model):
    user = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='img/posts/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def summary(self):
        return self.body[:200]

    @property
    def created_since(self):
        return timesince(self.created_at)
    
    class Meta:
        ordering = ['-created_at']


class Like(models.Model):
    user = models.ForeignKey('users.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey('users.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
