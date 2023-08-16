from django.conf import settings
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from users.views import UserViewSet, GenerateTokenAPIView, MyTokensAPIView
from chats.views import CreateChatAPIView, MessageListAPIView, SendMessageAPIView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# USERS
router.register("users", UserViewSet)

app_name = "v1"
urlpatterns = router.urls
urlpatterns += [
    path("generate-token/", GenerateTokenAPIView.as_view(), name="generate-token"),
    path("my-tokens/", MyTokensAPIView.as_view(), name="my-tokens"),
    path("create-chat/", CreateChatAPIView.as_view(), name="create-chat"),
    path("send-message/", SendMessageAPIView.as_view(), name="send-message"),
    path("my-messages/", MessageListAPIView.as_view(), name="my-messages"),
]