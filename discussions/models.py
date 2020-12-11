from django.db import models


class Discussion(models.Model):
    sender = models.ForeignKey('users.User', related_name='discussions_as_sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey('users.User', related_name='discussions_as_receiver', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    user = models.ForeignKey('users.User', related_name='messages', on_delete=models.CASCADE)
    discussion = models.ForeignKey(Discussion, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
