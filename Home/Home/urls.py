from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Home.school.urls")),
    path('student/', include("Home.student.urls")),
    path('authentication/', include("Home.home_auth.urls")),
]

# ✅ This serves uploaded images during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
