from django.db import models


class Notification(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)
    follow = models.ForeignKey('follows.Follow', related_name='notifications', on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey('posts.Comment', related_name='notifications', on_delete=models.CASCADE, blank=True, null=True)
    like = models.ForeignKey('posts.Like', related_name='notifications', on_delete=models.CASCADE, blank=True, null=True)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
