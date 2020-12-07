from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey('users.User', related_name='followings', on_delete=models.CASCADE)
    followed = models.ForeignKey('users.User', related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
