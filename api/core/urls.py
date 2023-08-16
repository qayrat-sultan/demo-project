from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView, \
    SpectacularJSONAPIView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("v1/", include("core.api_router"), name="v1"),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
    path('api/schema/json/', SpectacularJSONAPIView.as_view(), name='json'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title = "Dashboard"
admin.site.site_header = "Dashboard"
admin.site.site_url = "https://t.me/" + settings.BOT_USERNAME
admin.site.index_title = "Dopaminevoice.kz"
