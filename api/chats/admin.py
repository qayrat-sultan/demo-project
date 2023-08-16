from django.contrib import admin

from chats.models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    ...


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    ...
