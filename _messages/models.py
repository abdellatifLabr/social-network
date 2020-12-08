from django.db import models


class Message(models.Model):
    sender = models.ForeignKey('users.User', related_name='messages_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey('users.User', related_name='messages_received', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
