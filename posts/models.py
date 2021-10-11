from django.db import models
from django.utils.timesince import timesince

from .utils import post_files_upload_path


class Post(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    image = models.ImageField(
        upload_to='img/posts/image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def created_since(self):
        return timesince(self.created_at)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Section(models.Model):
    class SectionType(models.TextChoices):
        TEXT = ('TEXT', 'Text')
        IMAGE = ('IMAGE', 'Image')
        VIDEO = ('VIDEO', 'Video')
        YOUTUBE = ('YOUTUBE', 'Youtube')

    post = models.ForeignKey(
        Post, related_name='sections', on_delete=models.CASCADE)
    order = models.PositiveIntegerField()
    type = models.CharField(max_length=30, choices=SectionType.choices)
    content = models.TextField(blank=True, null=True)
    file = models.FileField(
        upload_to=post_files_upload_path, blank=True, null=True)

    class Meta:
        ordering = ['order']


class Like(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes',
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Rating(models.Model):
    user = models.ForeignKey(
        'users.User', related_name='ratings', on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='ratings', on_delete=models.CASCADE)
    value = models.FloatField()
