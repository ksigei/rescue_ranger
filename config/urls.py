from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('lostperson/', include('lostperson.urls')),
    # path('accounts/', include('accounts.urls')),
    path('', include('sightings.urls')),
    # path('locations/', include('locations.urls')),
    # path('contacts/', include('contacts.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
