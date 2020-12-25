from django.contrib import admin

from .models import Post, Like, Comment, Section

admin.site.register(Post)
admin.site.register(Section)
admin.site.register(Like)
admin.site.register(Comment)
