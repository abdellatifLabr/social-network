from django.db import models
from django.utils.timesince import timesince


class Post(models.Model):
    user = models.ForeignKey('users.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='img/posts/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_since(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

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
