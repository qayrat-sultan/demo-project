from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins, viewsets, generics
from rest_framework import mixins, status
from rest_framework.response import Response

from users.serializers import UserSerializer, UserTokenSerializer
from users.models import UserToken

User = get_user_model()


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"


class GenerateTokenAPIView(generics.CreateAPIView):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer


class MyTokensAPIView(generics.ListAPIView):
    queryset = UserToken.objects.all()
    serializer_class = UserTokenSerializer
    filterset_fields = ["user__id"]

    @extend_schema(
        parameters=[OpenApiParameter(name="user__id", required=True, type=int)])
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user__id')
        if not user_id:
            return Response(
                {
                    "message": _("Обязательный параметр user__id не указан.")},
                status=status.HTTP_400_BAD_REQUEST)
        return super().list(request, *args, **kwargs)

