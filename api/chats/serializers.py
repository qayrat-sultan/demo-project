from rest_framework import serializers

from chats.models import Chat, Message
from chats.tasks import send_message_to_telegram
from users.models import UserToken


class ChatSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True)
    chat_id = serializers.IntegerField(write_only=True)
    message = serializers.CharField(read_only=True)
    status = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        resp_data = {
            "status": 200,
            "message": "Успешно создан чат"
        }
        token = validated_data['token']
        chat_id = validated_data['chat_id']
        existing_token = UserToken.objects.filter(id=token)
        if not existing_token.exists():
            resp_data['message'] = 'Не найден токе пользователя'
            resp_data['status'] = 400
            return resp_data
        try:
            user = existing_token.first().user
            if hasattr(user, 'chat'):
                chat = user.chat
                chat.chat_id = chat_id
                chat.save()
                return resp_data

            Chat.objects.create(user=user, chat_id=chat_id)
            return resp_data
        except Exception as e:
            resp_data['status'] = 500
            resp_data['message'] = "Ошибка сервера: " + str(e)
            return resp_data


class SendMessageSerializer(serializers.Serializer):
    text = serializers.CharField()

    def create(self, validated_data):
        text = validated_data['text']
        user = self.context['user']  # Access the user object from the context
        try:
            chat = Chat.objects.get(user=user)
            send_message_to_telegram.delay(text, chat.chat_id)
        except Chat.DoesNotExist:
            raise ValueError("Не найден чат пользователя")
        return Message.objects.create(text=text, chat=chat)


class MessageSerializer(serializers.Serializer):
    text = serializers.CharField()
    created_at = serializers.DateTimeField()


