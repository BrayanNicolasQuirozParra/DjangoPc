from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniciopc/', include('pc.urls', namespace='inicio')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
