from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('recipes.urls')),
    path('admin/', admin.site.urls),
]


# handler404 = 'posts.views.page_not_found' # noqa
# handler500 = 'posts.views.server_error' # noqa
#
#
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)