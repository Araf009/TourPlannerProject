
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('planner/', include('planner.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('RegLogin.urls')),
    path('login/', include('RegLogin.urlsLogin')),
    path("", include('RegLogin.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)