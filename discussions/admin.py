from django.contrib import admin

from .models import Message, Discussion

admin.site.register(Message)
admin.site.register(Discussion)
