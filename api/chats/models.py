from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Chat(models.Model):
    user = models.OneToOneField(User, related_name="chat", on_delete=models.CASCADE)
    chat_id = models.BigIntegerField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Чат")
        verbose_name_plural = _("Чаты")

    def __str__(self):
        return _("Пользователь ID: {} | Чат ID: {}").format(self.user.username, self.chat_id)


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    text = models.CharField(max_length=1023)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Сообщение")
        verbose_name_plural = _("Сообщения")

    def __str__(self):
        return _("Чат ID: {} | Создано: {}").format(self.chat.chat_id, self.created_at)

