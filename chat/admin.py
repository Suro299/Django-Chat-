from django.contrib import admin
from .models import ChatMessage, Chat

admin.site.register(Chat)
admin.site.register(ChatMessage)