from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, generics
from rest_framework.permissions import IsAuthenticated

from chats.serializers import ChatSerializer, MessageSerializer, SendMessageSerializer
from chats.models import Chat, Message

User = get_user_model()


class CreateChatAPIView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class SendMessageAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = SendMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context


class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        try:
            chat = Chat.objects.get(user=self.request.user)
        except Chat.DoesNotExist:
            return None
        return qs.filter(chat=chat)
