
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('',include('django.contrib.auth.urls')),
    #path('search/',include('app.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#customzing admin site

admin.site.site_header="Contacts"
admin.site.index_title="Welcome to Contacts"
admin.site.site_title="Administrator"
